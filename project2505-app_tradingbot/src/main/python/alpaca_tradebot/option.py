from datetime import datetime, timedelta
import math




# High dividend assets grouped by week
HIGH_DIVS_1 = [
    'TSLY',
    'TSMY',
    'GOOY',
    'FEAT',
    'OARK',
    'SNOY',
    'FIVY',
    'TSLP',
    'XOMO',
    'QQQT',
    'SPYT',
    'ULTY',
    'IVVW',
    "LFGY",   # YieldMax Crypto Industry & Tech Portfolio Option Income ETF
]
HIGH_DIVS_2 = [
    'HOOW',
    'TSLW',
    'MARO',
    'MRNY',
    'TQQY',
    'YSPY',
    'PLTY',
    'NVDY',
    'GDXY',
    'FBY',
    'XPAY',
    'JPMO',
]
HIGH_DIVS_3 = [
    'COIW',
    'TSYY',
    'NVYY',
    'CONY',
    'HOOY',
    'CVNY',
    'JOF',
    'AMDY',
    'ABNY',
    'NFLY',
    'PYPY',
    'MSFO',
]
HIGH_DIVS_4 = [
    'MSTY',
    'SMCY',
    'AIYY',
    'CEPI',
    'AMZY',
    'XYZY',
    'AIPI',
    'APLY',
    'FEPI',
    'DISO',
]




EXPIRED_DIVIDEND_ASSETS = [
    'ICOI',
    'IMST',
    'IMRA',
]





# Combine all high dividend asset lists into a single list
HIGH_DIVIDEND_ASSETS = HIGH_DIVS_1 + HIGH_DIVS_2 + HIGH_DIVS_3 + HIGH_DIVS_4 + EXPIRED_DIVIDEND_ASSETS

# ─── Helpers for dividend asset selection ─────────────────────────────
def get_current_week_of_month():
    """
    Compute a 0-3 week index where:
    - Week 0 begins on the month's first Friday (and includes any days before it).
    - Each subsequent week starts 7 days later.
    - Index wraps every 4 weeks (mod 4).
    """
    today = datetime.now().date()
    first_of_month = today.replace(day=1)
    # Monday=0, ..., Sunday=6
    first_weekday = first_of_month.weekday()
    # How many days until the first Friday (weekday 4)
    days_to_first_friday = (4 - first_weekday) % 7
    first_friday = first_of_month + timedelta(days=days_to_first_friday)
    # print("==============================================")
    # print("==============================================")
    # print(f"first_friday={first_friday}")
    # print("==============================================")
    # print("==============================================")
    if (today - first_friday).days < 0: week_index = 0
    else: week_index = math.ceil(((today - first_friday).days + 1) / 7.0)

    return week_index % 4











def get_div_asset_list(current_week: int):
    """
    Returns the high dividend asset lists for the next 
    two upcoming weeks.
    If the week index is 4 or more, wraps to 0.
    """
    high_divs = [HIGH_DIVS_1, HIGH_DIVS_2, HIGH_DIVS_3, HIGH_DIVS_4]
    # Calculate indices for the next two weeks (wrap around with modulo)
    this_week = ((current_week + 0) % 4)
    next1week = ((current_week + 1) % 4)
    next2week = ((current_week + 2) % 4)
    
    today = datetime.now().weekday()
    # Saturday(5), Sunday(6), Monday (0), Tuesday (1) 
    # -> include this week (still have few days to buy)
    if today in (0,1,      5,6): 
        return high_divs[this_week] + high_divs[next1week] + high_divs[next2week] 
    else: 
        return high_divs[next1week] + high_divs[next2week]




def is_last_div(asset):
    """
    Determine whether an asset was a high-dividend asset in the previous week.

    Args:
        asset (str): The asset symbol to check.

    Returns:
        bool: True if the asset is in the high-dividend list for the previous week,
              False otherwise.
    """
    current_week = get_current_week_of_month()
    high_divs = [HIGH_DIVS_1, HIGH_DIVS_2, HIGH_DIVS_3, HIGH_DIVS_4]
    last_week = ((current_week - 1) % 4)
    this_week = ((current_week + 0) % 4)

    today = datetime.now().weekday()
    if asset in high_divs[last_week]:                               return True
    if asset in high_divs[this_week] and today in (        4,5,6):  return True ## next week prep
    return False


def is_not_div_sell(asset):
    """
    Determine whether an asset should not be held for 
    dividend purposes (i.e., signal a potential sell avoid)

    Args:
        asset (str): The asset symbol to check.

    Returns:
        bool: True if the asset for next week OR
              (1) the asset matches high-dividend AND
              (2) today is not a sell-relevant day (Mon [0] or Tue [1] or Wen [2] or Thr [3]** are NOT great),
              False otherwise.
    """
    current_week = get_current_week_of_month()
    high_divs = [HIGH_DIVS_1, HIGH_DIVS_2, HIGH_DIVS_3, HIGH_DIVS_4]
    this_week = ((current_week + 0) % 4)
    next_week = ((current_week + 1) % 4)

    today = datetime.now().weekday()
    if asset in high_divs[this_week] and today in (0,1,2,3,  5,6):  return True
    if asset in high_divs[next_week] and today in (    2,3,4,5,6):  return True ## next week prep
    return False




if __name__ == "__main__":
    test_assets = ["XYZY", "SNOY", "MARO", "HOOY", "UNKNOWN"]
    for asset in test_assets:
        if is_last_div(asset):
            print(f"{asset}: is a dividend asset to not BUY")
        elif is_not_div_sell(asset):
            print(f"{asset}: is a dividend asset to not SELL")
        else:
            print(f"{asset}: is a asset for normal operation")