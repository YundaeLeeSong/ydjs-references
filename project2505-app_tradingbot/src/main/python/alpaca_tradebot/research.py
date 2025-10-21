import os
import yfinance as yf
import pandas as pd

from datetime import datetime

HIGH_DIV_RATIO=1.10




def reset_research_file(filepath):
    headers = [
        "asset", "rank","sector", "company", 
        "price", "datetime", "dividends",
        "div_ratio", "is_high_yield"
    ]
    with open(filepath, 'w') as f:
        f.write(','.join(headers) + '\n')
    print(f"Reset file: {filepath}")

def append_to_research_file(filepath, data, unique=True):
    df_new = pd.DataFrame([data])

    if unique and os.path.exists(filepath):
        df_existing = pd.read_csv(filepath)
        is_duplicate = (
            (df_existing['asset'] == data['asset']) &
            (df_existing['datetime'] == data['datetime'])
        ).any()

        if is_duplicate:
            print(f"Skipped duplicate entry for {data['asset']} on {data['datetime']}")
            return

    df_new.to_csv(filepath, mode='a', header=False, index=False)
    print(f"Appended data for {data['asset']} to {filepath}")

def sort_research_file(filepath):
    df = pd.read_csv(filepath)
    df_sorted = df.sort_values(by=["sector", "datetime"], ascending=[True, True])
    df_sorted.to_csv(filepath, index=False)
    print(f"Sorted research file: {filepath}")

def fetch_and_save_dividends(assets, save_dir="./alpaca_data"):
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "research.csv")

    current_year = datetime.now().year

    for asset in assets:
        try:
            print(f"Processing {asset} ...")
            ticker = yf.Ticker(asset)

            # Fetch metadata
            info = ticker.info
            price = info.get("currentPrice")
            sector = info.get("sector", "Unknown")
            company = info.get("longName", asset)

            # Get dividends and set default values if missing
            dividends = ticker.dividends
            if price is None:
                print(f"No price data for {asset}, skipping.")
                continue

            # print(dividends)

            if dividends.empty:
                latest_date = pd.Timestamp("1999-01-01")
                latest_dividend = 0.0
            else:
                latest_date = dividends.index[-1]
                if latest_date.year != current_year:
                    latest_date = pd.Timestamp("1999-01-01")
                latest_dividend = dividends.iloc[-1]

            div_ratio = (latest_dividend / price) * 100
            is_high_yield = div_ratio >= HIGH_DIV_RATIO

            row_data = {
                "asset": f"'{asset}',",
                "rank": "#",
                "sector": sector,
                "company": company,
                "price": price,
                "datetime": latest_date.strftime("%Y-%m-%d"),
                "dividends": latest_dividend,
                "div_ratio": round(div_ratio, 2),
                "is_high_yield": is_high_yield
            }

            append_to_research_file(filepath, row_data, unique=True)

        except Exception as e:
            print(f"Warning: Could not fetch data for '{asset}'. Skipping. Reason: {e}")



def do_research(stat_assets,dyna_assets,fixed_assets):
    save_path = "./alpaca_data/research.csv"
    reset_research_file(save_path)
    fetch_and_save_dividends(stat_assets)
    fetch_and_save_dividends(dyna_assets)
    fetch_and_save_dividends(fixed_assets)
    sort_research_file(save_path)

def _print_assets(assets):
    for asset in assets:
        ticker = yf.Ticker(asset)
        dividends = ticker.dividends
        print(dividends)