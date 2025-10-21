"""
testdemo.py

Usage:

    python testdemo.py

"""
from pathlib import Path
import json
import csv
from typing import List

def gen():

    # 1. Define paths
    json_path = Path("alpaca_data2/assets.json")
    csv_path  = Path("alpaca_data2/assets.csv")

    # 2. Load JSON data
    with json_path.open("r", encoding="utf-8") as f:
        assets = json.load(f)

    # 3. Write only symbol & fractionable to CSV
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # header
        writer.writerow(["symbol", "fractionable"])
        # rows
        for asset in assets:
            writer.writerow([asset.get("symbol"), asset.get("fractionable")])






def get_nonfract_assets(csv_path: Path) -> List[str]:
    """
    Read a CSV of assets (with columns 'symbol' and 'fractionable') and
    return a list of symbols that are not fractionable.
    
    Args:
      csv_path: Path to the CSV file (expects a header with 'symbol' and 'fractionable').
    
    Returns:
      A list of symbols (strings) for which fractionable == False.
    """
    nonfract_symbols: List[str] = []
    
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # CSV stores booleans as text, so normalize and check
            frac = row["fractionable"].strip().lower()
            if frac in ("false", "0", ""):
                nonfract_symbols.append(row["symbol"])
    
    return nonfract_symbols

# Example usage:
# csv_path = Path("alpaca_data2/assets.csv")
# print(get_nonfract_assets(csv_path))
assets = [
    "AAPL",
    "GOOG",
    "MSFT",
    "TSLA",
    "AMZN",
    "NFLX",
    "ICOI",  # 4th week
    "HOOY",  # 4th week
    "AMDY",  # 4th week
    "CONY",  # 4th week
    "CVNY",  # 4th week
    "IMRA",  # 4th week
    "IMST",  # 4th week
    "SPXL", # S&P 500
    "HIBL", # S&P 500 (High Beta)
    "TNA",  # Russell 2000 (Small Cap) 
    "WEBL", # Dow Jones  
    "TQQQ", # NASDAQ 100

    #### 3x leveraged ETFs (extra for Libra behavior)
    "SOXL",
    "NAIL", #****int
    "PILL", #****int
    
    #### 2x leveraged ETFs (extra for Libra behavior)
    "AMZU", #****int
    "MSFU", #****int
    "GGLL", #****int
    "AMUU", #****int
    # "MSTU", #****int
    # "MUU",  #****int
    "ORCX",  #****int
]
NONFRACT_ASSETS=get_nonfract_assets(Path("alpaca_data2/assets.csv"))

for asset in assets:
    print(f"{asset} is {"nonfractional" if asset in NONFRACT_ASSETS else "fractional"}")