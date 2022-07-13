import ast

import requests


def find_pancakae():
    url1 = "https://api.pancakeswap.info/api/v2/tokens/"
    urlv1 = 'https://api.pancakeswap.info/api/tokens/'

    data = requests.get(url1)
    data = data.json()

    dictv2 = {}
    for n in data['data']:
        result = requests.get(url1 + n)
        result = result.json()
        dictv2[n] = result['data']['symbol']
    print(dictv2)
    with open('pancakev2.txt', 'a+') as f:
        f.write(str(dictv2))

    datav1 = requests.get(urlv1)
    datav1 = datav1.json()
    dict1 = {}
    for n in datav1['data']:
        result = requests.get(urlv1 + n)
        result = result.json()
        dict1[n] = result['data']['symbol']
    print(dict1)
    with open('pancakev1.txt', 'a+') as f:
        f.write(str(dict1))

    return dict1, dictv2


def binance():
    url = "https://api3.binance.com/api/v3/ticker/price"
    data = requests.get(url)
    data = data.json()
    # print(data)
    list = []
    for n in data:
        if "USDT" in n['symbol']:
            list.append(n['symbol'])
    with open("binance.txt", 'a+') as f:
        f.write(str(list))


def find_gateio():
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    url = '/spot/tickers'
    # query_param = 'currency_pair=BTC_USDT'
    # r = requests.request('GET', host + prefix + url  + "?" + query_param, headers=headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    r = r.json()

    list = []
    for n in r:
        # print(n['currency_pair'])
        if "_USDT" in n['currency_pair']:
            list.append(n['currency_pair'])
    with open('gateio.txt', 'a+') as f:
        f.write(str(list))

    return list


def check_similar():
    # pancv1, pancv2 = find_pancakae()

    # gateio = find_gateio()

    with open("binance.txt") as f:
        list = f.read()
    binance_list = ast.literal_eval(list)

    with open("gateio.txt") as f:
        list = f.read()
    gate_list = ast.literal_eval(list)

    result_list = []

    for n in binance_list:
        n_gate = n.replace("USDT", "_USDT")
        if n_gate in gate_list:
            result_list.append(n)
    with open("similar.txt", 'a+') as f:
        f.write(str(result_list))


def pancake_price_v1(contract):
    urlv1 = 'https://api.pancakeswap.info/api/tokens/'

    result = requests.get(urlv1 + contract)
    result = result.json()
    return float(result['data']['price'])


def pancake_price_v2(contract):
    urlv2 = "https://api.pancakeswap.info/api/v2/tokens/"
