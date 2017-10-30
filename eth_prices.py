#!/usr/bin/env python3

import requests
import json
import pandas as pd

def get():
    res = requests.get('https://etherchain.org/api/statistics/price')
    eth_dict = json.loads(res.text)
    return pd.DataFrame(eth_dict['data'])
