import ast
import concurrent.futures

from get_ticket_price import *


def check_arbitrage_biance_gate():
    print("||| BINANCE GATE ARBITRAGE |||")
    # list = ['MLNUSDT', 'GTCUSDT']
    list = []
    with open("similar_list/binance_gate_similar.txt") as f:
        list = f.read()
    biance_gate_similar_list = ast.literal_eval(list)
    for n in biance_gate_similar_list:
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_binance_price, str(n))
                binance_price = future.result()

            gate_symbol = n.replace("USDT", "_USDT")

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(gate_io_price, str(gate_symbol))
                gate_price = future.result()

            temp = gate_price / binance_price
            temp *= 100
            temp -= 100
            if temp > 1:
                print("binance -> gate - " + n + "  ||  " + str(temp))
            if temp < -1:
                # if temp > 1:
                print("gate -> binance - " + n + "  ||  " + str(temp))
        except Exception as e:
            continue


def check_arbitrage_kucoin_gate():
    print("||| KUCOIN GATE ARBITRAGE |||")
    # list = ['MLNUSDT', 'GTCUSDT']
    list = []
    with open("similar_list/gate_kucoin_similar.txt") as f:
        list = f.read()
    kucoin_gate_similar_list = ast.literal_eval(list)
    for n in kucoin_gate_similar_list:
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_kucoin_price, str(n))
                kucoin_price = future.result()

            gate_symbol = n.replace("-USDT", "_USDT")

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(gate_io_price, str(gate_symbol))
                gate_price = future.result()

            temp = gate_price / kucoin_price
            temp *= 100
            temp -= 100
            if temp > 1 and temp < 20:
                print("kucoin -> gate - " + n + "  ||  " + str(temp))
            if temp < -1 and temp > -20:
                # if temp > 1:
                print("gate -> kucoin - " + n + "  ||  " + str(temp))
        except Exception as e:
            continue


def check_arbitrage_kucoin_binance():
    print("||| KUCOIN Binance ARBITRAGE |||")
    # list = ['MLNUSDT', 'GTCUSDT']
    list = []
    with open("similar_list/binance_kucoin_similar.txt") as f:
        list = f.read()
    kucoin_binance_similar_list = ast.literal_eval(list)
    for n in kucoin_binance_similar_list:
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_kucoin_price, str(n))
                kucoin_price = future.result()

            binance_symbol = n.replace("-USDT", "USDT")

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_binance_price, str(binance_symbol))
                binance_price = future.result()

            temp = binance_price / kucoin_price
            temp *= 100
            temp -= 100
            if temp > 0.5 and temp < 20:
                print("kucoin -> binance - " + n + "  ||  " + str(temp))
            if temp < -0.5 and temp > -20:
                # if temp > 1:
                print("binance -> kucoin - " + n + "  ||  " + str(temp))
        except Exception as e:
            continue


def check_arbitrage_kucoin_mexc():
    print("||| KUCOIN MEXC ARBITRAGE |||")
    # list = ['MLNUSDT', 'GTCUSDT']
    list = []
    with open("similar_list/mexc_kucoin_similar.txt") as f:
        list = f.read()
    kucoin_mexc_similar_list = ast.literal_eval(list)
    for n in kucoin_mexc_similar_list:
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_kucoin_price, str(n))
                kucoin_price = future.result()

            mexc_symbol = n.replace("-USDT", "_USDT")

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_mexc_price, str(mexc_symbol))
                mexc_price = future.result()

            temp = kucoin_price / mexc_price
            temp *= 100
            temp -= 100
            if temp > 1 and temp < 20:
                print("mexc -> kucoin - " + n + "  ||  " + str(temp))
            if temp < -1 and temp > -20:
                # if temp > 1:
                print("kucoin -> mexc - " + n + "  ||  " + str(temp))
        except Exception as e:
            continue


def check_arbitrage_binance_mexc():
    print("||| BINANCE MEXC ARBITRAGE |||")
    # list = ['MLNUSDT', 'GTCUSDT']
    list = []
    with open("similar_list/mexc_binance_similar.txt") as f:
        list = f.read()
    binance_mexc_similar_list = ast.literal_eval(list)
    for n in binance_mexc_similar_list:
        try:

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_binance_price, str(n))
                binance_price = future.result()

            mexc_symbol = n.replace("USDT", "_USDT")

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_mexc_price, str(mexc_symbol))
                mexc_price = future.result()

            temp = binance_price / mexc_price
            temp *= 100
            temp -= 100
            if temp > 0.5 and temp < 20:
                print("mexc -> binance - " + n + "  ||  " + str(temp))
            if temp < -0.5 and temp > -20:
                # if temp > 1:
                print("binance -> mexc - " + n + "  ||  " + str(temp))

        except Exception as e:
            continue


def check_arbitrage_gate_mexc():
    print("||| GATE MEXC ARBITRAGE |||")

    list = []
    with open("similar_list/gate_mexc_similar.txt") as f:
        list = f.read()
    gate_mexc_similar_list = ast.literal_eval(list)
    for n in gate_mexc_similar_list:
        try:

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(gate_io_price, str(n))
                gate_price = future.result()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_mexc_price, str(n))
                mexc_price = future.result()

            temp = gate_price / mexc_price
            temp *= 100
            temp -= 100
            if temp > 1 and temp < 20:
                print("mexc -> gate - " + n + "  ||  " + str(temp))
            if temp < -1 and temp > -20:
                # if temp > 1:
                print("gate -> mexc - " + n + "  ||  " + str(temp))

        except Exception as e:
            continue
