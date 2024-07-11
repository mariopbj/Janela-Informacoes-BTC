import requests

def preco_btc():
    try:
        api_precobtc = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        preco = api_precobtc.json()
        return preco['bitcoin']['usd']
    
    except:
        return "error"


def preco_ult_200():
    try:
        api_ult200 = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=200')
        preco_200d = api_ult200.json()
        precos = [preco[1] for preco in preco_200d['prices']]
        return precos
    
    except:
        return "error"


def calcular_multiplo_de_mayer():
    try:
        preco_atual = preco_btc()
        precos_ultimos_200_dias = preco_ult_200()
        media_ult_200 = sum(precos_ultimos_200_dias) / len(precos_ultimos_200_dias)
        multiplo_de_mayer = preco_atual / media_ult_200
        return multiplo_de_mayer
    
    except:
        return "error"