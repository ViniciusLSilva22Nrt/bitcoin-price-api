import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df():
    #url para obter o preço do bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    #Requisição GET para a API
    response = requests.get(url)
    data = response.json()

    #extraindo dados e armazenando em variáveis
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_coleta = datetime.now()

    #criando o dataframe com os dados coletados
    df = pd.DataFrame ([{
        'ativo': ativo,
        'preco': preco,
        'moeda': moeda,
        'horario_coleta': horario_coleta
    }])

    return df

df = get_bitcoin_df()