#!/usr/bin/env python3

import requests
from urllib.request import urlretrieve
import pandas as pd
import re
import subprocess
from bs4 import BeautifulSoup as bs4, SoupStrainer
from os import path

btc_src = 'http://api.bitcoincharts.com/v1/csv/'

res = requests.get(btc_src)
soup = bs4(res.text, parse_only=SoupStrainer('a'))

#Get list of files
file_list = re.findall(r'href=\"([\w\.]*)\"', str(soup))

colnames=['timestamp','price','volume']
df = pd.DataFrame(columns=colnames)

#Download and add all files to a dataframe
for f in file_list:
    print("Extracting " + f)
    #Check if csv file exists (avoid unnecessary re-downloads)
    if not path.isfile(f[:-3]):
        urlretrieve(btc_src + f, f)
    if path.getsize(f) > 0:
        for chunk in pd.read_csv(f[:-3], chunksize = 10 ** 6, names=colnames):
            df = pd.concat([df, chunk])
            print('Shape: ')
            print(df.shape)

df.to_pickle('bitcoin_prices')
