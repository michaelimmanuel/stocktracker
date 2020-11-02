from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime


def real_time_stock_price(stock):
    url = "https://finance.yahoo.com/quote/"+stock+"?p="+stock
    r = requests.get(url)
    web_content = BeautifulSoup(r.text, "lxml")
    web_content = web_content.find("div", {"class": "D(ib) Mend(20px)"})
    web_content = web_content.find("span").text

    return web_content


HSI = ["TSLA", "FB", "GOOGL", "BBRI.JK"]

for step in range(1, 101):
    price = []
    col = []
    time_stamp = datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")

    for stock_code in HSI:
        price.append(real_time_stock_price(stock_code))

    col = [time_stamp]
    col.extend(price)

    df = pd.DataFrame(col)
    df = df.T
    df.to_csv("real time stock data.csv", mode="a", header=False)
    print(col)
