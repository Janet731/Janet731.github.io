"""
Use alpha vantage api to get stock data and plot it
"""

# disable pylint


import requests
import pandas as pd
from matplotlib import pyplot as plt

API_KEY = "ZF4OHV9WDOXNQ5B6"
STOCK_SYMBOL = "MSFT"

def get_daily_stock_data(symbol: str):
    """Get daily stock data from alpha vantage api"""
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}" 
    response = requests.get(url)
    data = response.json()
    print(data)
    return data
 
def main():
    data = get_daily_stock_data(STOCK_SYMBOL)
    
    # Turn the data into a pandas dataframe
    df = pd.DataFrame(data["Time Series (Daily)"]).T
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)

    # Print the DataFrame
    print(df)
    
    # export the data to a csv file
    df.to_csv("stockData.csv")
    
    # plot the data
    plt.plot(df["4. close"])
    plt.show()

if __name__ == "__main__":
    main()