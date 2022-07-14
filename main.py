
from arbitrage_opportunity import *


def choose_arbitrage():
    print("Вибери дві біржи із доступних для відображення можливостей")
    print('1 -- Gate Binance')
    print('2 -- Binance Kucoin')
    print('3 -- Kucoin Gate')
    print('4 -- Mexc Kucoin')
    print('5 -- Mexc Binance')
    choose = int(input("...  "))
    if choose==1:
        check_arbitrage_biance_gate()
    if choose == 2:
        check_arbitrage_kucoin_binance()
    if choose == 3:
        check_arbitrage_kucoin_gate()
    if choose == 4:
        check_arbitrage_kucoin_mexc()
    if choose == 5:
        check_arbitrage_binance_mexc()



if __name__ == "__main__":
   choose_arbitrage()
