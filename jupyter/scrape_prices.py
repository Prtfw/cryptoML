#!/usr/bin/env python3

import requests
import urllib
import pandas as pd
import re
import subprocess
from bs4 import BeautifulSoup as bs4, SoupStrainer
import json

btc_src = 'http://api.bitcoincharts.com/v1/csv/'

res = requests.get(btc_src)
soup = bs4(res.text, parse_only=SoupStrainer('a'))

#Get list of files
file_list = re.findall(r'href=\"([\w\.]*)\"', str(soup))

df = pd.DataFrame(columns=['timestamp','price','volume'])
#Download and add all files to a dataframe
for f in file_list:
    urllib.urlretrieve(btc_src + f, f)
    subprocess.run(['gunzip', f[:-3]])
    df = df.append(pd.read_csv(f[:-3]))

df.to_pickle('bitcoin_prices')
