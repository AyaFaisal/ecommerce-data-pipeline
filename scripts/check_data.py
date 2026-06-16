import pandas as pd
import os

def load_and_check():
    path = 'data/'
    orders = pd.read_csv(os.path.join(path, 'olist_orders_dataset.csv'))
    
    print("--- Orders Info ---")
    print(orders.info())
    print("\n--- First 5 Rows ---")
    print(orders.head())

if __name__ == "__main__":
    load_and_check()