import requests

def preco_btc():
    try:
        api_precobtc = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        preco = api_precobtc.json()
        return preco['bitcoin']['usd']
    
    except:
        return "Indisponivel"


def preco_ult_200():
    try:
        api_ult200 = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=200')
        preco_200d = api_ult200.json()
        precos = [preco[1] for preco in preco_200d['prices']]
        return precos
    
    except:
        return "Indisponivel"


def calcular_multiplo_de_mayer():
    try:
        preco_atual = preco_btc()
        precos_ultimos_200_dias = preco_ult_200()
        media_ult_200 = sum(precos_ultimos_200_dias) / len(precos_ultimos_200_dias)
        multiplo_de_mayer = preco_atual / media_ult_200
        return str(multiplo_de_mayer)[:4]
    
    except:
        return "Indisponivel"


def taxas_onchain():
    try:
        api_mempool = requests.get('https://mempool.space/api/v1/fees/recommended')
        if api_mempool.status_code == 200:
            taxas = api_mempool.json()
            return taxas
        else:
            return "Indisponivel"
    except:
        return "Indisponivel"
    

def preco_btc_formatado():
    try:
        preco_formatado = '${:,.2f}'.format(preco_btc())
        return preco_formatado
    
    except:
        return 'Indisponivel'
    

def taxas_onchain_formatado():
    try:
        prioridade_alta = str(taxas_onchain()['fastestFee']) + ' sat/vB'
        prioridade_media = str(taxas_onchain()['halfHourFee']) + ' sat/vB'
        prioridade_baixa = str(taxas_onchain()['hourFee']) + ' sat/vB'

        taxas_formatado = {
            'fastestFee': prioridade_alta,
            'halfHourFee': prioridade_media,
            'hourFee': prioridade_baixa
        }
        return taxas_formatado

    except:
        falha = {
        'fastestFee': 'Indisponivel',
        'halfHourFee': 'Indisponivel',
        'hourFee': 'Indisponivel'
    }
        return falha