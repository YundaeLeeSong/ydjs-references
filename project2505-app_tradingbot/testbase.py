"""
testbase.py

Usage:

    python testbase.py

"""
import json
import yfinance as yf
import csv
import time
from urllib.error import HTTPError

def convert_json_to_assets():
    # Read the JSON file
    with open('alpaca_data2/assets.json', 'r') as file:
        data = json.load(file)
    
    # Open output file for writing
    with open('alpaca_data2/assets_sorted.txt', 'w') as output_file:
        # Write each symbol in the desired format
        for item in data:
            symbol = item.get('symbol')
            if (
                symbol and
                len(symbol) <= 6 and
                '.' not in symbol and
                '_' not in symbol and
                item.get('class') == 'us_equity' and
                item.get('exchange') in ['NASDAQ', 'NYSE', 'BATS', 'ARCA']
                # item.get('exchange') in ['ARCA']
            ):
                output_file.write(f"Buy 1 {symbol}\n")



def main2():
    convert_json_to_assets()





if __name__ == "__main__":
    main2()