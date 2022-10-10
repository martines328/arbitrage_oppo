import ast


def binance_kucoin_similar():
    with open("coins/kucoin.txt") as f:
        list = f.read()
    kucoin_list = ast.literal_eval(list)

    with open("coins/binance.txt") as f:
        list = f.read()
    binance_list = ast.literal_eval(list)

    result_list = []

    for n in kucoin_list:
        n_gate = n.replace("-USDT", "USDT")
        if n_gate in binance_list:
            result_list.append(n)
    with open("similar_list/binance_kucoin_similar.txt", 'a+') as f:
        f.write(str(result_list))

def binance_poloneix_similar():
    with open("coins/poloneix.txt") as f:
        list = f.read()
    poloneix_list = ast.literal_eval(list)

    with open("coins/binance.txt") as f:
        list = f.read()
    binance_list = ast.literal_eval(list)

    result_list = []

    for n in binance_list:
        n_poloniex = n.replace("USDT", "_USDT")
        if n_poloniex in poloneix_list:
            result_list.append(n)

    with open("similar_list/binance_poloneix_similar.txt", 'a+') as f:
        f.write(str(result_list))





def gate_kucoin_similar():
    with open("coins/kucoin.txt") as f:
        list = f.read()
    kucoin_list = ast.literal_eval(list)

    with open("coins/gateio.txt") as f:
        list = f.read()
    gate_list = ast.literal_eval(list)

    result_list = []

    for n in kucoin_list:
        n_gate = n.replace("-USDT", "_USDT")
        if n_gate in gate_list:
            result_list.append(n)
    with open("similar_list/gate_kucoin_similar.txt", 'a+') as f:
        f.write(str(result_list))


def binance_gate_similar():
    # pancv1, pancv2 = find_pancakae()

    # gateio = find_gateio()

    with open("coins/binance.txt") as f:
        list = f.read()
    binance_list = ast.literal_eval(list)

    with open("coins/gateio.txt") as f:
        list = f.read()
    gate_list = ast.literal_eval(list)

    result_list = []

    for n in binance_list:
        n_gate = n.replace("USDT", "_USDT")
        if n_gate in gate_list:
            result_list.append(n)
    with open("similar_list/binance_gate_similar.txt", 'a+') as f:
        f.write(str(result_list))



def gate_mexc_similar():
    with open("coins/mexc.txt") as f:
        list = f.read()
    mexc_list = ast.literal_eval(list)

    with open("coins/gateio.txt") as f:
        list = f.read()
    gate_list = ast.literal_eval(list)

    result_list = []

    for n in mexc_list:
        if n in gate_list:
            result_list.append(n)
    with open("similar_list/gate_mexc_similar.txt", 'a+') as f:
        f.write(str(result_list))


def mexc_kucoin_binace_similar():
    with open("coins/kucoin.txt") as f:
        list = f.read()
    kucoin_list = ast.literal_eval(list)

    with open("coins/binance.txt") as f:
        list = f.read()
    binance_list = ast.literal_eval(list)

    with open("coins/mexc.txt") as f:
        list = f.read()
    mexc_list = ast.literal_eval(list)
    # kucoin mexc
    mexc_kucoin_list = []

    for n in kucoin_list:
        n_mexc = n.replace("-USDT", "_USDT")
        if n_mexc in mexc_list:
            mexc_kucoin_list.append(n)
    with open("similar_list/mexc_kucoin_similar.txt", 'a+') as f:
        f.write(str(mexc_kucoin_list))

    mexc_binance_list = []
    # binance mexc
    for n in binance_list:
        n_mexc = n.replace("USDT", "_USDT")
        if n_mexc in mexc_list:
            mexc_binance_list.append(n)
    with open("similar_list/mexc_binance_similar.txt", 'a+') as f:
        f.write(str(mexc_binance_list))
