#!/usr/bin/env python3
"""
transaction.py

Given a CSV of buy/sell transactions (with columns: Description, Type, Qty, Amount, Date),
compute, for each asset symbol, the total bought/sold quantities, net position, cash spent, cash received, and net cash flow.

Usage:

    python report/transaction.py "report/transaction-Jaehoon.xlsx"
    python report/transaction.py "report/transaction-Tae.xlsx"
    

    -- for divend research
    python report/transaction.py "report/analysis-base.xlsx"
    python report/transaction.py "report/analysis-base-inverse.xlsx"

""" 

import sys
import pandas as pd
import re
from pathlib import Path
import openpyxl
import xlrd  # Ensure xlrd is imported for .xls support



def get_latest_price(symbol: str) -> float:
    import yfinance as yf
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d", interval="1m")
    if not data.empty: return round(float(data["Close"].iloc[-1]), 2)  # last available close
    else: raise ValueError(f"No data available for symbol: {symbol}")


def safe_get_latest_price(symbol: str) -> float:
    try:
        return get_latest_price(symbol)
    except Exception as e:
        print(f"Warning: could not fetch price for {symbol}: {e}")
        return float("nan")


def get_dividend_info(symbol: str) -> tuple:
    """
    Get dividend information for a symbol:
    - latest dividend per share
    - latest dividend date
    Returns (dividend_per_share, dividend_date)
    """
    import yfinance as yf
    from datetime import datetime, timedelta
    try:
        ticker = yf.Ticker(symbol)
        
        # Get dividend history
        div_history = ticker.dividends
        if not isinstance(div_history, pd.Series) or div_history.empty:
            return 0.0, None, None
            
        # Get the latest dividend
        latest_div = div_history.iloc[-1]
        latest_date = div_history.index[-1].strftime('%Y-%m-%d')
        
        # Calculate next expected dividend date (assuming quarterly)
        last_date = div_history.index[-1]
        next_date = (last_date + timedelta(days=90)).strftime('%Y-%m-%d')
        
        return round(float(latest_div), 2), latest_date, next_date
            
    except Exception as e:
        print(f"Warning: could not fetch dividend info for {symbol}: {str(e)}")
        return 0.0, None, None


def parse_amount(amount_str):
    """
    Convert Amount strings like "$206.20", "($1,631.25)", "$4,751.28 " into a signed float.
    - Parentheses indicate a negative amount (a cash outflow, e.g., a Buy).
    - Dollar signs and commas are removed.
    - Also handles float inputs directly.
    """
    if pd.isna(amount_str):
        return 0.0
        
    # If it's already a float, return it
    if isinstance(amount_str, (float, int)):
        return float(amount_str)

    amt = amount_str.strip().replace('"', '').replace(' ', '')
    negative = False

    # Check for parentheses indicating a negative value
    if amt.startswith('(') and amt.endswith(')'):
        negative = True
        amt = amt[1:-1]

    # Remove any leading $ and commas
    amt = amt.replace('$', '').replace(',', '')

    try:
        val = float(amt)
    except ValueError:
        # If parsing fails, return 0.0 and warn
        print(f"Warning: could not parse Amount '{amount_str}' → treating as 0.0")
        return 0.0

    return -val if negative else val

def extract_symbol_and_action(description):
    """
    From Description like "Sell 1 AMZN" or 'Buy 0.01 WEN', extract:
      - action: either "Buy" or "Sell"
      - symbol: the ticker at the end (e.g. "AMZN", "WEN")
    Treats any 'Sell_short', 'Sell Short', etc. as 'Sell'.
    """
    parts = description.strip().split()
    if len(parts) < 3:
        return None, None

    action = parts[0].lower()
    if action.startswith("sell"):
        action = "Sell"
    elif action == "buy":
        action = "Buy"
    else:
        return None, None

    symbol = parts[-1]
    return action, symbol


def generate_tax_report(excel_path):
    try:
        # Use openpyxl engine and specify encoding
        df = pd.read_excel(excel_path, engine='openpyxl')
    except Exception as e:
        print(f"Error reading '{excel_path}': {e}")
        print("\nTrying alternative method...")
        try:
            # Try with xlrd engine as fallback
            df = pd.read_excel(excel_path, engine='xlrd')
        except Exception as e2:
            print(f"Error with alternative method: {e2}")
            return  # Exit function if both methods fail

    # Ensure required columns exist
    for col in ["Description", "Qty", "Amount"]:
        if col not in df.columns:
            print(f"Error: expected column '{col}' in Excel file but not found.")
            return

    # Parse Amount → signed float
    df["Amount_float"] = df["Amount"].apply(parse_amount)

    # Extract Action (Buy/Sell) and Symbol
    df[["Action", "Symbol"]] = df["Description"].apply(
        lambda desc: pd.Series(extract_symbol_and_action(desc))
    )

    # Drop any rows where we couldn't detect symbol or action
    df = df.dropna(subset=["Action", "Symbol"])

    # Convert Qty to numeric (in case it's a string)
    df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce").fillna(0.0)

    # Groupby Symbol and Action
    grouped = df.groupby(["Symbol", "Action"])

    summary_rows = []
    for (symbol, action), sub in grouped:
        total_qty = sub["Qty"].sum()
        total_cash = sub["Amount_float"].sum()

        summary_rows.append({
            "Symbol": symbol,
            "Action": action,
            "Total_Qty": round(total_qty, 2),
            "Total_Cash": round(total_cash, 2)
        })

    summary_df = pd.DataFrame(summary_rows)

    # Pivot so we have one row per Symbol
    pivot_qty = summary_df.pivot_table(
        index="Symbol",
        columns="Action",
        values="Total_Qty",
        fill_value=0.0
    ).rename(columns={"Buy": "Qty_Bought", "Sell": "Qty_Sold"})

    pivot_cash = summary_df.pivot_table(
        index="Symbol",
        columns="Action",
        values="Total_Cash",
        fill_value=0.0
    ).rename(columns={"Buy": "Cash_Spent", "Sell": "Cash_Received"})

    # Combine both
    combined = pivot_qty.join(pivot_cash, how="outer").fillna(0.0)

    # Add calculated columns
    combined["Net_Qty"] = round(combined["Qty_Bought"] - combined["Qty_Sold"],2)
    combined["Net_Cash"] = round(combined["Cash_Received"] + combined["Cash_Spent"],2)
    # Add real-time price using yfinance
    print("\nFetching latest prices and dividend information...")
    combined["Latest_Price"] = combined.index.map(safe_get_latest_price)
    
    # Add dividend information
    print("Fetching dividend information (this may take a moment)...")
    dividend_info = combined.index.map(get_dividend_info)
    combined["Latest_Dividend"] = [info[0] for info in dividend_info]
    combined["Last_Dividend_Date"] = [info[1] for info in dividend_info]
    combined["Anticipated_Ex_Date"] = [info[2] for info in dividend_info]

    # Calculate Net_Profit first (without dividend)
    combined["Net_Profit"] = round(combined["Net_Cash"] + combined["Net_Qty"] * combined["Latest_Price"], 2)

    # Filter out outdated dividend data (more than a year old)
    mask = pd.to_datetime(combined["Last_Dividend_Date"]) >= (pd.Timestamp.now() - pd.Timedelta(days=365))
    combined.loc[~mask, ["Latest_Dividend", "Last_Dividend_Date", "Anticipated_Ex_Date"]] = [0.0, None, None]

    # Filter out stocks where anticipated ex-date is in the past
    mask2 = pd.to_datetime(combined["Anticipated_Ex_Date"]) > pd.Timestamp.now()
    combined.loc[~mask2, ["Latest_Dividend", "Last_Dividend_Date", "Anticipated_Ex_Date"]] = [0.0, None, None]

    # Calculate dividend yield only for stocks with recent dividend data
    combined["Div_Yield_Pct"] = combined.apply(
        lambda row: round(row["Latest_Dividend"] / row["Latest_Price"] * 100, 2) 
        if pd.notna(row["Last_Dividend_Date"]) else 0.0, 
        axis=1
    )

    # Reorder columns
    combined = combined[
        [
            "Qty_Bought",
            "Qty_Sold",
            "Net_Qty",
            "Cash_Spent",
            "Cash_Received",
            "Net_Cash",
            "Latest_Price",
            "Net_Profit",
            "Anticipated_Ex_Date",
            "Div_Yield_Pct",
            "Latest_Dividend",
            "Last_Dividend_Date"
        ]
    ]

    # Print to console, sorted alphabetically by Symbol
    combined = combined.sort_index()

    # # sort it by Net_Qty
    # combined = combined.sort_values(by="Net_Qty", ascending=False)
    # # Save to CSV with dividend information
    # combined.to_csv("report/report-by_qty.csv")

    # Save by Net_Profit, separating "in" (Net_Qty != 0) and "out" (Net_Qty == 0)
    combined_by_profit = combined.sort_values(by="Net_Profit", ascending=False)
    # combined_in = combined_by_profit[combined_by_profit["Net_Qty"] != 0]
    # combined_out = combined_by_profit[combined_by_profit["Net_Qty"] == 0]
    # combined_in.to_csv("report/report-in-by_profit.csv")
    # combined_out.to_csv("report/report-out-by_profit.csv")
    # sort it by Net_Profit
    combined = combined_by_profit
    combined.to_csv("report/report-by_profit.csv")

    # combined = combined.sort_values(by="Div_Yield_Pct", ascending=False)
    # combined.to_csv("report/report-by_div_yield.csv")


def main():
    if len(sys.argv) != 2:
        print("Usage: python transaction.py path/to/transactions.xlsx")
        sys.exit(1)
    excel_path = sys.argv[1]
    generate_tax_report(excel_path)

if __name__ == "__main__":
    main()
