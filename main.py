import ast
import asyncio
import json

import requests as requests


async def get_binance_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price?symbol="
    data = requests.get(url + symbol)
    data = data.json()
    return float(data['price'])


async def gate_io_price(symbol):
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


async def check_arbitrage():
    list = []
    with open("similar.txt") as f:
        list = f.read()
    similar_list = ast.literal_eval(list)
    for n in similar_list:
        binance_price = await get_binance_price(str(n))
        gate_symbol = n.replace("USDT", "_USDT")
        gate_price = await gate_io_price(gate_symbol)

        temp = gate_price / binance_price
        temp *= 100
        temp -= 100
        if temp > 1:
            print("binance -> gate - " + n + "  ||  " + str(temp))
        if temp < -1:
            # temp += 100
            if temp > 1:
                print("gate -> binance - " + n + "  ||  " + str(temp))


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(check_arbitrage())
