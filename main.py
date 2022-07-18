import create_similar
import proc
from arbitrage_opportunity import *



def get_all_list():
    proc.binance()
    proc.gate_io()
    proc.mexc()
    proc.kucoin()

    create_similar.binance_gate_similar()
    create_similar.gate_mexc_similar()
    create_similar.gate_kucoin_similar()
    create_similar.binance_kucoin_similar()
    create_similar.mexc_kucoin_binace_similar()


def choose_arbitrage():
    print("Вибери дві біржи із доступних для відображення можливостей")
    print('1 -- Gate Binance')
    print('2 -- Binance Kucoin')
    print('3 -- Kucoin Gate')
    print('4 -- Mexc Kucoin')
    print('5 -- Mexc Binance')
    print('6 -- Mexc Gate')

    choose = int(input("...  "))
    if choose == 1:
        check_arbitrage_biance_gate()
    if choose == 2:
        check_arbitrage_kucoin_binance()
    if choose == 3:
        check_arbitrage_kucoin_gate()
    if choose == 4:
        check_arbitrage_kucoin_mexc()
    if choose == 5:
        check_arbitrage_binance_mexc()
    if choose == 6:
        check_arbitrage_gate_mexc()



if __name__ == "__main__":
    choose_arbitrage()
    # get_all_list()