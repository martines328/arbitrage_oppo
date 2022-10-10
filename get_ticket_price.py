import requests


def get_kucoin_price(symbol):
    base_url = 'https://api.kucoin.com'
    url = f'/api/v1/market/orderbook/level1?symbol={symbol}'
    data = requests.get(base_url + url)
    data = data.json()
    return float(data['data']['price'])


def get_poloneix_price(symbol):
    url =f'https://api.poloniex.com/markets/{symbol}/price'
    data = requests.get(url)
    data = data.json()
    return float(data['price'])

def get_binance_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price?symbol="
    data = requests.get(url + symbol)
    data = data.json()

    return float(data['price'])


def gate_io_price(symbol):
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    url = '/spot/tickers'
    query_param = f'currency_pair={symbol}'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    # r = requests.request('GET', host + prefix + url, headers=headers)
    r = r.json()
    for item in r:
        return float(item['last'])


def get_mexc_price(symbol):
    base_url = 'https://www.mexc.com'
    url = '/open/api/v2/market/ticker'
    prefix = f"?symbol={symbol}"
    r = requests.request('GET', base_url + url + prefix)
    r = r.json()
    for n in r['data']:
        return float(n['last'])
