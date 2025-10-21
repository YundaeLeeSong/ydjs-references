from typing import Optional, Tuple, List, Dict, Any


#################################################################
################################################### ETF Libra (Resonance)
#################################################################

MK_INDEX_ASSETS = [
    "SPXL", # S&P 500
    "HIBL", # S&P 500 (High Beta)
    "TQQQ", # NASDAQ 100
    "WEBL", # Dow Jones
    "TNA",  # Russell 2000 (Small Cap)

    #### 3x leveraged ETFs (extra for Libra behavior)
    # "SOXL",
    "SOXS",
    # "NAIL",
    # "PILL",
    
    #### 2x leveraged ETFs (extra for Libra behavior)
    "TSLL", 
    "TSLZ", 
    "MSTU",
    "MSTZ",
    # "CONL",
    # "CONI",
    "MRAL",
    # "IONX",
    "IONZ",
    # "SMCX",
    "SMCZ",

    "BITQ", # general crypto 1
    "LMBO", # general crypto 2
    # "REKT", # general crypto (short)

    #### inverse dividend ETFs (extra for Libra behavior)
    'WNTR', # MSTR
    'FIAT', # COIN
    # 'DIPS', # NVDA
    'CRSH', # TSLA
    'ETHD', # ETH
]

# Global mapping of (ticker, leverage) to underlying asset
TICKER_LEVERAGE_TO_ASSET: Dict[Tuple[str, int], str] = {
    # ###################################################### Leveraged ETFs (by Index)
    # ("SPXL", 3)     : "NULL",   # S&P 500
    # ("HIBL", 3)     : "NULL",   # S&P 500 (High Beta)
    # ("TNA",  3)     : "NULL",   # Russell 2000 (Small Cap) 
    # ("WEBL", 3)     : "NULL",   # Dow Jones  
    # ("TQQQ", 3)     : "NULL",   # NASDAQ 100
    ###################################################### Leveraged ETFs (by Sectors)
    ("SOXL", 3)     : "NULL",   # Semi-condoctor
    ("SOXS",-3)     : "NULL",
    ("TECL", 3)     : "NULL",   # Technology 
    ("TECS",-3)     : "NULL",
    ("FAS",  3)     : "NULL",   # Financial 
    ("FAZ", -3)     : "NULL",
    ("DRN",  3)     : "NULL",   # Real Estate  
    ("DRV", -3)     : "NULL",
    
    ("NAIL", 3)     : "NULL",   # Homebuilders
    ("CURE", 3)     : "NULL",   # Healthcare
    ("RETL", 3)     : "NULL",   # Retail
    ("DUSL", 3)     : "NULL",   # Industrials
    ("UTSL", 3)     : "NULL",   # Utilities
    ("WANT", 3)     : "NULL",   # Consumer Discretionary
    ("TPOR", 3)     : "NULL",   # Transportation
    ("PILL", 3)     : "NULL",   # Pharmaceutical & Medical


    ("BITQ", 2)     : "NULL",   # Bitwise Crypto Industry Innovators ETF
    ("REKT", -1)    : "NULL",   # Direxion Daily Crypto Industry Bear 1X Shares
    ("LMBO", 2)     : "NULL",   # Direxion Daily Crypto Industry Bull 2X Shares





    #### Crypto Trader (Brokearge)
    ("MSTU", 2)     : "MSTR",
    ("MSTZ", -2)    : "MSTR",
    ("WNTR", -1)    : "MSTR",
    

    #### Bitcoin (BTC)
    # fixed supply of 21 million coins and a proof‑of‑work consensus 
    # that ensures network security through computational effort. 
    ("BITX", 2)     : "BTC",
    ("BTCZ", -2)    : "BTC",

    ("BITU", 2)     : "BTC",
    ("SBIT", -2)    : "BTC",

    ("MRAL", 2)     : "MARA",
    
    #### Ethereum (ETH)
    # smart contracts and decentralized applications (dApps). 
    # Uses a proof‑of‑stake, transaction (“gas”) fees in staking, 
    # mechanism to validate transactions, 
    # reducing energy consumption compared to proof‑of‑work chains. 
    ("ETHU", 2)     : "ETH",
    ("ETHD", -2)    : "ETH",







    #### Crypto Trader (Altcoin)
    ("CONL", 2)     : "COIN",
    ("CONI", -2)    : "COIN",
    ("FIAT", -1)    : "COIN",

    ("CRCA", 2)     : "CRCL",
    ## XRP (Ripple) (XRP)
    # native token of the open‑source XRP Ledger, 
    # created to enable fast, low‑cost cross‑border payments. 
    # pre‑issued at inception with transactions confirmed via 
    # a unique consensus protocol (NOT proof‑of‑work)
    # [IMPORTANT] XRP offers the cheapest fee for transactions
    ("XRPT", 2)    : "CRCL",







    #### Pharma / Bio-Tech
    ("LLYX", 2)     : "LLY",
    ("ELIS", -1)    : "LLY",

    ("HIMZ", 2)     : "HIMS",

    ("UNHG", 2)     : "UNH",

    ("NVOX", 2)     : "NVO",



    #### Semi-condoctor
    ("AMUU", 2)     : "AMD",
    ("AMDD", -1)    : "AMD",


    ("NVDL", 2)     : "NVDA",
    ("NVDU", 2)     : "NVDA",
    ("NVD", -2)     : "NVDA",
    ("NVDS", -1.5)  : "NVDA",
    
    ("DIPS", -1)    : "NVDA",




    ("MUU", 2)      : "MU",
    ("MUD", -1)     : "MU",

    ("AVGX", 2)     : "AVGO",
    ("AVS", -1)     : "AVGO",

    ("INTW", 2)     : "INTC",
    
    ("ARMG", 2)     : "ARM",

    #### Semi-condoctor (material)

    ("ASMG", 2)     : "ASML",
    
    
    #### Hardware
    ("IONX", 2)     : "IONQ",
    ("IONZ", -2)    : "IONQ",

    ("SMCX", 2)     : "SMCI",
    ("SMCZ", -2)    : "SMCI",

    ("RGTX", 2)     : "RGTI",
    ("RGTZ", -2)    : "RGTI",

    ("QBTX", 2)     : "QBTS",
    ("QBTZ", -2)    : "QBTS",



    


    
    #### Software (Buisness)
    ("PLTU", 2)     : "PLTR",
    ("PTIR", 2)     : "PLTR",
    ("PLTD", -1)    : "PLTR",
    ("PLTZ", -2)    : "PLTR",

    ("ORCX", 2)     : "ORCL",

    ("CRMG", 2)     : "CRM",

    #### Software (Consumer Services)
    ("GGLL", 2)     : "GOOGL",
    ("GGLS", -1)    : "GOOGL",

    ("AMZU", 2)     : "AMZN",
    ("AMZD", -1)    : "AMZN",
    
    ("MSFU", 2)     : "MSFT",
    ("MSFD", -1)    : "MSFT",

    ("ADBG", 2)     : "ADBE",
    


    #### Tesla
    ("TSLL", 2)     : "TSLA",
    ("TSLZ", -2)    : "TSLA",
    
    ("CRSH", -1)    : "TSLA",


    #### Aerospace
    ("JOBX", 2)     : "JOBY",

    #### Nuk Energy
    ("OKLL", 2)     : "OKLO",
    ("SMU", 2)      : "SMR",



    # Extend this mapping with additional ETF entries as needed
}





def is_etf(ticker: str) -> bool:
    return any(key[0] == ticker for key in TICKER_LEVERAGE_TO_ASSET)

def is_bear_etf(ticker: str) -> bool:
    """
    Check if a ticker is a bear ETF (has negative leverage).

    Args:
        ticker: The ticker symbol to check
    Returns:
        bool: True if the ticker is a bear ETF (negative leverage), False otherwise
    """
    for (etf_ticker, leverage), _ in TICKER_LEVERAGE_TO_ASSET.items():
        if etf_ticker == ticker and leverage < 0: return True
    return False

def get_equiv_asset_etf(
    asset_symbol: Optional[str] = None,
    tick_n_lev: Optional[Tuple[str, int]] = None
) -> Optional[Any]:
    """
    Lookup leveraged ETFs by underlying asset or reverse lookup asset by ticker-leverage.

    If `asset` is provided, returns a list of dicts each with keys:
      - 'ticker': ETF ticker string
      - 'leverage': leverage integer (e.g., 2, -2)
    Returns None if no matching entries.

    If `tick_n_lev` is provided, returns a dict with keys:
      - 'ticker': ETF ticker string
      - 'leverage': leverage integer
      - 'asset': underlying asset string
    Returns None if not found.

    Only one of `asset` or `tick_n_lev` should be non-None.
    Raises ValueError if both are provided simultaneously.
    """
    if asset_symbol is not None:
        if tick_n_lev is not None: 
            raise ValueError("Provide only one of `asset` or `tick_n_lev`.")

    # Lookup by asset: gather all matching ticker-leverage entries
    if asset_symbol is not None:
        results: List[Dict[str, Any]] = []
        for (ticker, leverage), asset_val in TICKER_LEVERAGE_TO_ASSET.items():
            if asset_val == asset_symbol:
                results.append({
                    "ticker": ticker,
                    "leverage": leverage,
                })
        return results if results else None

    # Reverse lookup by ticker+leverage pair
    if tick_n_lev is not None:
        asset_val = TICKER_LEVERAGE_TO_ASSET.get(tick_n_lev)
        if asset_val is None:
            return None
        ticker, leverage = tick_n_lev
        return {
            "ticker": ticker,
            "leverage": leverage,
            "asset": asset_val,
        }
    # Neither argument provided
    return None

def get_asset_state(asset: str) -> int:
    if not is_etf(asset): 
        if get_equiv_asset_etf(asset_symbol=asset) is not None: return 2    # NORM -> ETF chain
        else: return 0    # NORM
    else: return 1        # ETF










def main() -> None:
    """
    Demonstrate lookup functionality with example cases.
    """
    # Example 1: lookup for ETH
    eth_etfs = get_equiv_asset_etf(asset_symbol="ETH")
    if eth_etfs is not None:
        print(eth_etfs)
        print("Leveraged ETFs for ETH:")
        for etf in eth_etfs:
            print(f"  • {etf['ticker']} ({etf['leverage']}×)")

    print()  # Blank line for readability



    # # Example 2: reverse lookup for a given ticker-leverage pair
    # info = get_equiv_asset_etf(tick_n_lev=("ETHU", 2))
    # if info:
    #     print(info)
    #     print(
    #         f"  Ticker: {info['ticker']}, "
    #         f"Leverage: {info['leverage']}×, "
    #         f"Asset: {info['asset']}"
    #     )

    # print()


    

    # Example 3: lookup for BTC
    btc_etfs = get_equiv_asset_etf(asset_symbol="BTC")
    if btc_etfs is not None:
        print("Leveraged ETFs for BTC:")
        for entry in btc_etfs:
            print(f"  • {entry['ticker']} ({entry['leverage']}×)")

    print()





    # Example 4: lookup for non-existing asset
    sol_etfs = get_equiv_asset_etf(asset_symbol="SOL")
    if sol_etfs:
        print("Leveraged ETFs for SOL:")
        for entry in sol_etfs:
            print(f"  • {entry['ticker']} ({entry['leverage']}×)")

    print()



    # Example usage
    if is_etf("ETHT"): print("ETHT is a etf (bull/bear) registered.")
    if is_etf("ETHU"): print("ETHU is a etf (bull/bear) registered.")
    if is_etf("ETHD"): print("ETHD is a etf (bull/bear) registered.")
    print('\n\n\n')



    asset = "ETH"
    if (get_asset_state(asset) == 0): print(f"\t[**0]{asset} is maybe a normal asset WITHOUT ETF.")
    if (get_asset_state(asset) == 1): print(f"\t[**1]{asset} is a etf (bull/bear) registered.")
    if (get_asset_state(asset) == 2):
        print(f"\t[**2]{asset} is a normal asset WITH ETF found.")
        etfs = get_equiv_asset_etf(asset_symbol=asset)
        for etf in etfs:
            if (etf['leverage'] > 0): 
                print(f"  • {etf['ticker']} ({etf['leverage']}×) is a bull")
            if (etf['leverage'] < 0): 
                print(f"  • {etf['ticker']} ({etf['leverage']}×) is a bear")






    # pairs = [("ETHU", 2), ("ETHD", -2), ("BTCZ", -2)]

    # print("Example 1: Unpacking in for loop")
    # for ticker, leverage in pairs:
    #     print(f"Ticker: {ticker}, Leverage: {leverage}")

    # print("\nExample 2: Using enumerate with unpacking")
    # for index, (ticker, leverage) in enumerate(pairs):
    #     print(f"{index}: {ticker} ({leverage}x)")

    # print("\nExample 3: Access tuple elements without unpacking")
    # for pair in pairs:
    #     print(f"Pair: {pair[0]} → {pair[1]}x")



if __name__ == "__main__":
    main()
