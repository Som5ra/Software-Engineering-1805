import requests
from bs4 import BeautifulSoup
import datetime
import re
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
}

url = "https://www.maigoo.com/goomai/167245.html"


if __name__ == '__main__':
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    names = soup.find_all('td', class_='sch_name')
    file = open('exhibitions.txt', 'w+')
    for name in names:
        file.write(str(name.text) + '\n')
    file.close()