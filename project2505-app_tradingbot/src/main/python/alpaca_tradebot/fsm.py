#!/usr/bin/env python3
import time
import threading
import json


from .balances import get_and_print, fetch_and_save
from .orders import cancel_order, fetch_orders,save_orders_to_csv, cancel_all_orders_in



import sys
import platform

def beep(frequency, duration):
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(frequency, duration)  # frequency, duration in ms
    else:
        # ASCII BEL character; most terminals will make a beep
        sys.stdout.write('\a')
        sys.stdout.flush()

def schedule(name: str, interval: float):
    """
    Runs in its own thread, beeping and printing `name` every `interval` seconds.
    """
    next_time = time.time() + interval
    while True:
        sleep_time = next_time - time.time()
        if sleep_time > 0: time.sleep(sleep_time)
        # trigger
        print(f"[{time.strftime('%H:%M:%S')}] 🔔 {name}")
        beep(1000,200)

        

        next_time += interval










def fsm(name: str, interval: float):
    """
    Runs in its own thread, beeping and printing `name` every `interval` seconds.
    """
    state = 0
    prev = None
    curr = None
    # 0: waiting
    next_time = time.time() + interval
    while True:
        sleep_time = next_time - time.time()
        if sleep_time > 0: time.sleep(sleep_time)
        # # trigger
        # print(f"[{time.strftime('%H:%M:%S')}] 🔔 {name}")
        # beep(800,100)


        # FSM Logic (Design)
        if (prev is None and curr is None): 
            with open("alpaca_data/orders.json", 'r', encoding='utf-8') as f: curr = f.read()
            ### prompt and alert
            print("\tFinite State Machine (FSM) for trading just started... Waiting for orders change...")
            beep(800,100)
            state = 0
        elif (prev is None or state == 0): 
            print("\tFetched Orders are being processed...")
            prev = curr
            with open("alpaca_data/orders.json", 'r', encoding='utf-8') as f: curr = f.read()
            if (prev == curr): 
                ### prompt and alert
                print("\tchanges in orders have been NOT caught...")
                beep(600,100)
                state = 0
            else: 
                ### prompt and alert
                print("\tchanges in orders have been ✔ caught...")
                beep(2000,100)
                state = 1
        elif (state == 1): 
            print("\t\tCalculation is being processed...")


            ### prompt and alert
            beep(2400,100)
            state = 0

        # elif state == 2: print("Orders are being cancelled...")




        next_time += interval








def fetch(name: str, interval: float):
    """
    Runs in its own thread, beeping and printing `name` every `interval` seconds.
    """
    next_time = time.time() + interval
    while True:
        sleep_time = next_time - time.time()
        if sleep_time > 0: time.sleep(sleep_time)
        # trigger
        print(f"[{time.strftime('%H:%M:%S')}] 🔔 {name}")
        beep(1600,100)




        ### [GET] Fetch orders by assets
        path = "alpaca_data/orders.json"
        orders = fetch_orders()             # your existing function
        with open(path, "w") as f: json.dump(orders, f, indent=2)
        print(f"✔ Saved {len(orders)} open orders to {path}")
        # if you need to inspect them in code:
        for o in orders:
            print(f"- {o['id']} | {o['symbol']} | {o['side']} {o.get('qty') or o.get('notional')}@{o['limit_price']}")
        save_orders_to_csv(orders)               # writes alpaca_data/orders.csv



        next_time += interval










def run():
    # Launch one thread per repeating sound
    threads = [
        threading.Thread(target=fsm,      args=("Finite State Machine (9.20s)",   9.20), daemon=True),
        threading.Thread(target=fetch,    args=("GET... fetching data (4.53s)",   7.53), daemon=True),
        # threading.Thread(target=schedule, args=("Warning              (23s)",   23.0),  daemon=True),
    ]
    for t in threads:
        t.start()

    print("Press Ctrl+C to stop.")
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped by user")

if __name__ == "__main__":
    run()
