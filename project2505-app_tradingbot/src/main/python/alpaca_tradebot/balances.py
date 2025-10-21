# import os
# import json
# import csv
# import requests
# from datetime import datetime
# from dotenv import load_dotenv

# from pvm import get_resource

# # ─── 0) load .env ─────────────────────────────────────────────────────────────
# load_dotenv(get_resource(".env"))

# PURCHASING_POWER = int(os.getenv("PURCHASING_POWER", 240))
# BASE_URL   = os.getenv("APCA_API_BASE_URL")
# API_KEY    = os.getenv("APCA_API_KEY_ID")
# API_SECRET = os.getenv("APCA_API_SECRET_KEY")

# if not (API_KEY and API_SECRET):
#     BASE_URL="https://paper-api.alpaca.markets"
#     API_KEY="PKD7M8VMC1D6YOQ6CW57"
#     API_SECRET="4Euz3jubAEwIvboqeWcJRkbuROGqCFNJ7OzNPLUe"

# HEADERS = {
#     "APCA-API-KEY-ID":     API_KEY,
#     "APCA-API-SECRET-KEY": API_SECRET,
#     "Content-Type":        "application/json"
# }








# # ─── helper to GET & print JSON ────────────────────────────────────────────────
# def get_and_print(endpoint):
#     """
#     GET /v2/{endpoint}, raise on error, and pretty-print the JSON result.
#     """
#     url = f"{BASE_URL}/v2/{endpoint}"
#     resp = requests.get(url, headers=HEADERS)
#     resp.raise_for_status()
#     data = resp.json()
#     print(f"\n=== {endpoint.upper()} ===")
#     print(data)



# # ─── Helper to GET & save JSON ────────────────────────────────────────────────
# def fetch_and_save(endpoint, filename):
#     """
#     GET /v2/{endpoint}, raise on error, and save the JSON result to `filename`.
#     """
#     url = f"{BASE_URL}/v2/{endpoint}"
#     resp = requests.get(url, headers=HEADERS)
#     resp.raise_for_status()
#     data = resp.json()
#     with open(get_resource(filename,isDebug=True), "w") as f: json.dump(resp.json(), f, indent=2)
#     print(f"✔ Saved {endpoint} to {filename}")
    
#     rows = []
#     # Format with date and time
#     current_datetime = datetime.now()
#     formatted_date = current_datetime.strftime("%Y-%m-%d")
#     formatted_time = current_datetime.strftime("%H:%M:%S")
    
        
#     # Process data based on endpoint type
#     if endpoint == "positions":
#         for position in data:
#             # pre-process data ############################ past-data based
#             pct_amp = MIN_PCT_AMP
#             frq = 2
#             ############################################## current data
#             asset = position['symbol']
#             quantity = float(position['qty'])
#             market_price = float(position['current_price'])
#             qty_unit = int(PURCHASING_POWER / market_price + 0.50)
#             purchase_price = float(position['avg_entry_price'])
#             total_profit_and_lose = round((market_price/purchase_price - 1) * 100, 2) # in (%)
#             is_profitable = bool(total_profit_and_lose >= (TRIG_DISTROS[3] * pct_amp))
#             is_losable = bool(total_profit_and_lose < (TRIG_DISTROS[7] * pct_amp))
#             is_at_mid = not (is_profitable or is_losable)
#             is_stocked = (int(quantity) > 0)
#             ############################################### normalization
#             market_price = round(market_price, 2)
#             purchase_price = round(purchase_price, 2)
#             if (qty_unit < 1): 
#                 log_path = "alpaca_data2/log.txt"
#                 with open(log_path, "a") as log_file:
#                     log_file.write(f"[{datetime.now()}] Too expensive asset, manually trade it: {asset}\n")
#                 continue
#             # For each asset, write or append its position to a CSV file named by symbol.
#             csv_path = f"alpaca_data2/position-{asset}.csv"
#             headers = [
#                 "asset",
#                 "qty_unit",
#                 "quantity",
#                 "time",
#                 "market_price",
#                 "purchase_price",
#                 "total_profit_and_lose",
#                 "is_profitable",
#                 "is_at_mid",
#                 "is_losable",
#                 "is_stocked",
#                 "pct_amp",
#                 "frq",
#             ]
#             file_exists = os.path.isfile(csv_path)
#             row = {
#                 "asset": asset,
#                 "qty_unit": qty_unit,
#                 "quantity": quantity,
#                 "time": formatted_date + " " + formatted_time,
#                 "market_price": market_price,
#                 "purchase_price": purchase_price,
#                 "total_profit_and_lose":total_profit_and_lose,
#                 "is_profitable": is_profitable,
#                 "is_at_mid": is_at_mid,
#                 "is_losable": is_losable,
#                 "is_stocked": is_stocked,
#                 "pct_amp": pct_amp,
#                 "frq": frq,
#             }
#             rows.append(row)
#             with open(csv_path, mode="a", newline="") as csvfile:
#                 writer = csv.DictWriter(csvfile, fieldnames=headers)
#                 if not file_exists:
#                     writer.writeheader()
#                 writer.writerow(row)
#             print(f"✔ Data for {asset} written/appended to {csv_path}")
#     elif endpoint == "assets":
#         # For assets, we just save the JSON data without processing
#         pass
#     else:
#         print(f"WARNING: Unknown endpoint type: {endpoint}")

#     return rows






# # ─── main ─────────────────────────────────────────────────────────────────────
# if __name__ == "__main__":
#     # 1) Account overview (buying power, portfolio value, cash, status…)
#     get_and_print("account")

#     # 2) Open positions (symbol, qty, avg_entry_price, unrealized_pl…)
#     get_and_print("positions")

#     # 3) All assets you could trade (status, tradable, marginable…)
#     #    (filter by asset class or status in Python if you like)
#     get_and_print("assets")

#     # 4) Recent account activities (trades, dividends, etc.)
#     get_and_print("activities")




#     os.makedirs("alpaca_data", exist_ok=True)

#     # 1) Account overview
#     fetch_and_save("account",       "alpaca_data2/account.json")

#     # 2) Open positions
#     fetch_and_save("positions",     "alpaca_data2/positions.json")

#     # 3) All assets
#     fetch_and_save("assets",        "alpaca_data2/assets.json")

    
#     # 4) Recent account activities (trades, dividends, etc.)
#     fetch_and_save("activities",        "alpaca_data2/activities.json")
