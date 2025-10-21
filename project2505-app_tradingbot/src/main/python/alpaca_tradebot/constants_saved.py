




# ─── 1) CONFIG LISTS ──────────────────────────────────────────────────────────
ETF_LIST        = ["DIA", "SPY", "QQQ", "IWM", "NYF"]






EXCLUDED_ASSETS = []
VIRAL_ASSETS = []
PENNY_ASSETS = ["AMPG", "PLX"]



#####################################################################################
##################################################################################### Scalability (% yield)
#####################################################################################
#####################################################################################
#####################################################################################

####### Foundation Constants
EXTRE_SLOW_RATE = 1.100
SLOW_REACT_RATE = 1.085 # slow-reaction (considering versatility and no div.)
NORM_REACT_RATE = 0.785 # normal-reaction (considering dividend profit)
FAST_REACT_RATE = 0.575 # fast-reaction (when market is going up too fast)

#### increasing price
DEPTH_OF_TRANSACTION = 3
STD_DIV_OF_TRANSACTION = 0
PROFIT_RATE=1.0275          # (> 2.75%)
SELLING_RATE=1.0063 # upon the profit rate, so target profit rate = PROFIT_RATE * SELLING_RATE (pf% +0.63%)

SHRINK_RATE=0.9325          # (< -6.75%)
BUYING_RATE=0.9755          # (-0.25%)


# < STD_DIV_OF_TRANSACTION >
# 0: 2.00 ~ 2.77%
# 1: 2.78 ~ 3.85%
# 2: 3.80 ~ 5.25%
# 3: 5.06 ~ 7.00%
# 4: 6.56 ~ 9.07%
# 5: 8.20 ~ 11.34%
# 6: 9.77 ~ 13.50%




# ─── 2) ASSET LISTS ──────────────────────────────────────────────────────────

STAT_ASSETS = [
    "AMZN",                                     # logistics (cloud service, software*)
    "F","GM",                                   # auto (Not recommended)
    "HPQ","DELL",                               # hardware (computer)

    # https://companiesmarketcap.com/semiconductors/largest-semiconductor-companies-by-market-cap/
    "NVDA", #1; price: $141.72; div: 1.24%; D/E: 12.27%
    "AVGO", #2; price: $246.93; div: 5.00%; D/E: 166.03%        *************** dyna
    "AMD",  #6; price: $116.19; div: 0.43%; D/E: 8.17%
    "TXN",  #7; price: $192.42; div: 1.01%; D/E: 78.31%
    "QCOM", #8; price: $149.24; div: 1.14%; D/E: 52.74% 
    "AMAT", #10; price: $166.74; div: 1.55%; D/E: 35.18%
    "MU",   #11; price: $108.56; div: 2.14%; D/E: 30.89%        *************** dyna
    "LRCX", #13; price: $86.35;  div: 1.70%; D/E: 47.15%
    "ADI",  #14; price: $222.26; div: 1.94%; D/E: 20.62%
    "INTC", #16; price: $20.06;  div: 0.35%; D/E: 47.13%
    "SNPS", #17; price: $486.00; div: 0.79%; D/E: 7.15%
    "MRVL", #20; price: $68.35;  div: 4.90%; D/E: 33.89%        *************** dyna
    "MCHP", #26; price: $65.25;  div: 1.37%; D/E: 81.68%
    "MPWR", #27; price: $687.08; div: 0.88%; D/E: 0.50%
    "ON",   #34; price: $50.17;  div: 0.00%; D/E: 45.38%




    # Healthcare (Insurances) 
    "UNH",                     # UnitedHealth Group (#1)          2025-03-10   2.10
    "CI",                      # Cigna Group (#14)                2025-06-03   1.51
    # Healthcare (Pharmaceuticals)
    "NVO",                     # Novo Nordisk (#4)                2025-03-31   1.537 *****
    "BMY",                     # Bristol-Myers Squibb (#14)       2025-04-04   1.284
    "CVS",                     # CVS Health (#17)                 2025-04-22   1.038
    "PFE",                     # Pfizer (#11)                     2025-05-09   1.830 *****
    "JNJ",                     # Johnson & Johnson (#2)           2025-05-27   0.846
    "OSCR",

    # food / beverage
    "SBUX",                    # Starbucks Corporation (#5)       2025-05-16
    "PZZA",                    # Papa John's (#25)                2025-05-19
    "WEN",                     # The Wendy's Company (#21)        2025-06-02
    "PEP",                     # PepsiCo, Inc. (#3)               2025-06-06
    "KO",                      # The Coca-Cola Company (#1)       2025-06-13
    "CAVA",                    # CAVA Group, Inc. (#11)           ----------
    "DNUT",                    # Krispy Kreme, Inc. (---Joker---) ----------

    

    "TGT","WMT","COST","HD","BBY",              # glossary
    "ETH","BTC",                                      # crypto-coin

    'assets "non-versatile" with "dividend" in the order of forcast'] 








SHORT_ASSETS = [
    "SOXL",
    "SOXS",
    "TSLL",
    "TSLQ",
]



DYNA_ASSETS_EXTREME = [
    "SOXL",
    "SOXS",
    "TSLL",
    "TSLQ",
    # "OSCR",
    "OKLO","SMR",
    "PZZA",
    "ORCL",
    "MU", "MRVL","AXP",
    

    'assets I can rip off'] ############ RIPPING OFF!!!! 


DYNA_ASSETS = [
    "SOXL",
    "SOXS",
    "TSLL",
    "TSLQ",


    "ORCL","META","ADBE",                           # software
    "CSCO","IBM","MSFT","GOOG","GOOGL","AAPL",      # harware+software
    "NFLX",                                         # entertainmant
    

    "AXP",                                      # bank processor
    "TGT",


    "AVGO", #2; price: $246.93; div: 5.00%; D/E: 166.03%        *************** dyna
    "MU",   #11; price: $108.56; div: 2.14%; D/E: 30.89%        *************** dyna
    "MRVL", #20; price: $68.35;  div: 4.90%; D/E: 33.89%        *************** dyna








    "BWXT","NNE","OKLO","SMR",                  # energy sector
    # "BWXT",  # BWX Technologies Inc.
    #          # - Supplies nuclear components and fuel internationally
    #          # - Sole manufacturer of naval nuclear reactors for U.S. Navy
    #          # - Engages in commercial nuclear services and government operations
    # "NNE",   # Nano Nuclear Energy Inc.
    #          # - Develops portable microreactors: ZEUS (solid core) and ODIN (salt-cooled)
    #          # - Focuses on nuclear fuel fabrication, transportation, and consulting
    #          # - Aims for vertically integrated nuclear energy solutions
    # "OKLO",  # Oklo Inc.
    #          # - Designs compact fast reactors for clean, reliable energy
    #          # - Targets deployment of first plant by 2027
    #          # - Serves data centers, industrial sites, and defense facilities
    # "SMR",   # NuScale Power Corporation
    #          # - Develops small modular reactors (SMRs) with 77 MWe capacity
    #          # - Received NRC approval for updated reactor design in May 2025
    #          # - Engages with data center operators for future deployments


    # fashion
    "NKE",   # Nike, Inc. (#8)
             # - Air Force 1, Air Max, Dunk (iconic sneakers)
             # - Dri-FIT apparel, Pro Training gear
             # - Jordan Brand, Nike SB (skateboarding), Nike Sportswear
    "RL",    # Ralph Lauren Corporation (#17)
             # - Polo Ralph Lauren Shirts (classic polos)
             # - Purple Label Suits (high-end tailoring)
             # - RRL Denim (vintage-inspired jeans)
             # - Lauren handbags and shoes (accessible luxury)
    "BURL",  # Burlington Stores, Inc. (#19)
             # - Off-price retailer: designer brands at reduced prices
             # - Categories: apparel, footwear, baby gear, home goods
             # - Similar to TJX and Ross; limited e-commerce presence
    "LEVI",  # Levi Strauss & Co. (#25)
             # - Levi's 501 Original Jeans, Trucker Jackets
             # - Denim innovations: Water<Less®, Sustainable cotton
             # - Lifestyle collections: Levi's Made & Crafted, Levi's Vintage Clothing
    "PVH",   # Phillips-Van Heusen (#35)
             # - Calvin Klein: underwear, denim, fragrances
             # - Tommy Hilfiger: logo polos, watches, outerwear
             # - Heritage Brands (previously): Van Heusen, IZOD
    "ANF",   # Abercrombie & Fitch Co. (#36)
             # - Abercrombie: modern casualwear, rebranded for inclusivity
             # - Hollister: Southern California-inspired lifestyle brand
             # - Strong social media presence, youth-oriented collections
    "ZGN",   # Ermenegildo Zegna Group (#47)
             # - Zegna: luxury menswear, triple stitch sneakers, #UseTheExisting™ sustainability platform
             # - Thom Browne: cropped suits, 4-bar stripe sweaters, avant-garde tailoring
             # - Focus on made-to-measure suits, sustainable wool, and high-end Italian craftsmanship
    "CPRI",  # Capri Holdings Ltd (#48)
             # - Michael Kors: Jet Set Travel Tote, Runway Smartwatch, perfumes
             # - Jimmy Choo: Romy Pumps, Diamond Sneakers, bridal collection
    "AEO",   # American Eagle Outfitters (#50) 
             # - American Eagle: denim jeans, graphic tees, outerwear
             # - Aerie: body-positive lingerie, activewear, and swimwear
             # - Focus on Gen Z trends, inclusivity, and casual lifestyle

    "TSLA", "RIVN", "LCID", "MULN",           # EV sector (added Mullen Automotive)
    # "TSLA",  # Tesla Inc. (#1)
    #          # - Leading electric vehicle (EV) manufacturer globally
    #          # - Operates Gigafactories and develops battery/storage technologies
    #          # - Diversifies into autonomous driving and energy products
    # "RIVN",  # Rivian Automotive Inc. (#6)
    #          # - EV maker specializing in trucks and SUVs (R1T, R1S)
    #          # - Focuses on adventure/lifestyle segment and fleet vehicles (e.g. Amazon vans)
    #          # - Invests in proprietary charging network and service infrastructure
    # "LCID",  # Lucid Motors (Lucid Group Inc.) (#11)
    #          # - Produces luxury EVs with high-performance specs (e.g. Lucid Air)
    #          # - Targets premium market segment with focus on efficiency and range
    #          # - Expanding internationally with focus on Middle East and Asia
    # "MULN",  # Mullen Automotive (#34)
    #          # - Develops and manufactures electric vehicles and EV components
    #          # - Focuses on affordable EVs and commercial vehicles
    #          # - Expanding partnerships and production capabilities


    'assets "versatile" without "dividend" in the order of forcast'] 




HOLD_ASSETS = [ ### you don't wanna handle it
    # "SOXL",
    # "SOXS",
    # "PEP",
    # "COST",
    # "SMR",
    # "SMR",

    # "TSLA", "RIVN", "LCID", "MULN",
    
    'assets I want to hold'] 










##################################################################################### Quantity
##################################################################################### (Dividend)
##################################################################################### (Current Balance)
#####################################################################################
TRIPLE_ASSETS = [ # for buying only                                 Ex-Dividend Date and %
    # "SOXL",
    # "SOXS",
    # "TSLL",
    # "TSLQ",


    # "TGT",                   # Target Corporation                 2025-05-14  1.180 *******
    # "PZZA",                  # Papa John's International Inc.     2025-05-19  1.050
    # "JNJ",                   # Johnson & Johnson                  2025-05-27  0.846

    # "WEN",                     # The Wendy's Company                2025-06-02  1.260 *******
    # "PEP",                     # PepsiCo Inc.                       2025-06-06  1.078
    # "HPQ",                     # HP Inc.                            2025-06-11  1.160 *******
    # "UNH",                   # UnitedHealth Group Inc.            2025-06-17  0.704
    # "BBY",                   # Best Buy Co., Inc.                 2025-06-18  1.430 *******

    # 'PVH',                     # PVH Corp.                          2025-06-04  N/A
    # 'BMY',	               # Bristol-Myers Squibb Company       04/04/2025	1.28	*******
    # 'AEO',	               # American Eagle Outfitters, Inc.    04/11/2025	1.14	*******
    # 'CVS',	               # CVS Health Corporation	            04/22/2025	1.04	


    # 'PFE',	                # Pfizer Inc.	                    5/9/2025	0.43	1.83	TRUE
    # 'TGT',	                # Target Corporation	            5/14/2025	1.12	1.19	TRUE
    # 'PZZA',	                # Papa John's International, Inc.   5/19/2025	0.46	1.02	FALSE


    # "AMZN",                  # Amazon.com Inc.: Does not currently pay dividends
    # "AMD",                   # Advanced Micro Devices Inc.: Does not pay dividends
    # "INTC",                  # Intel Corporation: Dividend suspended as of 2024
    # "ANF",                   # Abercrombie & Fitch Co.: Does not pay dividends
    # "BURL",                  # Burlington Stores Inc.: Does not pay dividends



    
    "ASSETS TO DOUBLE DOWN! based on https://stockanalysis.com/stocks/orcl/forecast/",
    "price reference: https://stockanalysis.com/stocks/orcl/forecast/"]





    # # Real Estate (REITs)
    # "ADC",                     # Agree Realty Corp.                2025-06-30   4.00
    # "VICI",                    # VICI Properties                   2025-06-25   5.45
    # "O",                       # Realty Income                     2025-06-16   5.69

    # # Tobacco
    # "PM",                      # Philip Morris International       2025-06-09   3.04
    # "MO",                      # Altria Group                      2025-06-10   6.73
    # "BTI",                     # British American Tobacco          2025-06-12   7.01

    # # Utilities
    # "DUK",                     # Duke Energy                       2025-06-16   3.55

    # # Telecom
    # "VZ",                      # Verizon                           2025-06-12   6.17


    # # Financial Services / Payments
    # "MA",                      # Mastercard                        2025-06-12   0.52
    # "V",                       # Visa                              2025-06-12   0.65
    # "INTU",                    # Intuit                            2025-06-10   0.55
    # "SPGI",                    # S&P Global                        2025-06-20   0.73

    # # Technology (Large Caps)
    # "NVDA",                    # Nvidia                            2025-06-12   0.03
    # "CRM",                     # Salesforce                        2025-06-06   0.63
    # "MSFT",                    # Microsoft                         2025-06-16   0.71
    # "ASML",                    # ASML Holding                      2025-06-04   0.97

    # Zero-dividend tickers (ranked at bottom, not eligible for TRIPLE strategy)
    # "GOOGL",                 # Alphabet                          -           0.00
    # "AMZN",                  # Amazon                            -           0.00
    # "PDD",                   # Pinduoduo                         -           0.00
    # "MELI",                  # MercadoLibre                      -           0.00

    # "PLTR",                  # Palantir                          -           0.00
    # "DUOL",                  # Duolingo                          -           0.00
    # "HIMS",                  # Hims & Hers                       -           0.00

    # "JOBY",                  # Joby Aviation                     -           0.00
    # "ASTS",                  # AST & Science                     -           0.00
    # "ACHR",                  # Archer Aviation                   -           0.00
    # "RGTI",                  # Rigetti Computing                 -           0.00
    # "IONQ",                  # IonQ                              -           0.00
    # "RKLB",                  # Rocket Lab USA                    -           0.00
    # "SYM",                   # Symbotic                          -           0.00
    # "LMND",                  # Lemonade                          -           0.00
    # "ALAB",                  # Aileron Therapeutics              -           0.00
    # "RDDT",                  # Reddit                            -           0.00
    # "NET",                   # Cloudflare                        -           0.00
    # "MU",                    # Micron Technology                 -           0.00
    # "RBRK",                  # Revolve Group                     -           0.00
    # "TEM",                   # Tempus AI                         -           0.00
    # "SNOW",                  # Snowflake                         -           0.00
    # "S",                     # SentinelOne                       -           0.00
    # "TMDX",                  # TransMedics                       -           0.00
    # "NBIS",                  # Nebius                            -           0.00
    # "SOFI",                  # SoFi Technologies                 -           0.00
    # "OSCR",                  # Oscar Health                      -           0.00
    # "CDLR",                  # Cadeler                           -           0.00
    # "AMD",                   # Advanced Micro Devices            -           0.00





