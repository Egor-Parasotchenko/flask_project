import requests
from time import ctime

def get_dogecoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    dogecoin_price = data['dogecoin']['usd']
    return dogecoin_price


def get_current_time():
    return ctime()