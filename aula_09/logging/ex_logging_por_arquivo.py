import logging , logging.config, yaml
import requests

with open('logging.yaml') as f:
    logging.config.dictConfig(yaml.safe_load(f))

logfile = logging.getLogger('file')
logconsole = logging.getLogger('console') 

url = 'http://python521.herokuapp.com/validar/desafio'

dic ={'timestamp': 'teste', 'mensagem':'resposta' }


try:
    #response = requests.get(url)
    response = requests.post(url, json=dic)
    response.raise_for_status()

except requests.exceptions.HTTPError as err:
    logconsole.error(f' HTTP ERROR: {err}')
    logfile.warning(f'HTTP ERROR: {err}')
except requests.exceptions.Timeout as err:
    logconsole.error(f'TIMEOUT - tempo limite excedido : {err}')
except requests.exceptions.ConnectionError as err:
    logconsole.error(f'CONNECTION ERROR: {err}')
except Exception as err:
    logconsole.critical(f'Erro desconhecido - {err}')

else:
    logconsole.info(f' Ação concluída com sucesso: {dic}')
