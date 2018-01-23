import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

time_flag = True

while True:
    if datetime.now().minute != 59:
        time.sleep(58) # 58秒待機
        continue

    f = open('nikkei_heikin.csv', 'a')
    writer = csv.writer(f, lineterminator='\n')
    while datetime.now().second != 59:
        time.sleep(1)
    time.sleep(1)
    csv_list = []
    time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    csv_list.append(time_)

    url = "http://www.nikkei.com/markets/kabu/"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    prices = soup.select("span.mkc-stock_prices")
    price = prices.pop(0)
    nikkei_heikin = price.string
    print(time_, nikkei_heikin)
    csv_list.append(nikkei_heikin)
    writer.writerow(csv_list)
    f.close()
    time.sleep(58)