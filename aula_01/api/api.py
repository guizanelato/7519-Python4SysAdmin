
import requests

#1: qual o endereço que iremos requisitar
url = 'https://viacep.com.br/ws/{}/json/'

#2: informar um cep
cep = '06223040' # input

#3: fazer a requisição

try:
    response = requests.get(url.format(cep))
    response.raise_for_status() 

#if response.status_code != 200:
#    print(response.text)
#else:
#    print(response.json())

except requests.exceptions.HTTPError as err:
    print(f'HTTP ERROR - {err}')
except requests.ConnectionError as err:
    print(f'Erro de conexão - {err}')
except requests.TimeoutError as err:
    print('Tempo limite excedido')
except Exception as err:
    print(f"Erro Inesperado - {err}")
else:
    payload = response.json()
    for chave, valor in payload.items():
        print(chave, valor) 




