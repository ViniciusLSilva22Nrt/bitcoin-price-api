import time
import pandas as pd
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df

valor_bitcoin = get_bitcoin_df()
valor_commodities = get_commodities_df()

while True:
    print(valor_bitcoin)
    print(valor_commodities)

    time.sleep(60)  # Aguarda 60 segundos antes da próxima iteração 
