
import logging , logging.config, yaml
import requests

with open('logging.yaml') as f:
    logging.config.dictConfig(yaml.safe_load(f))

logfile = logging.getLogger('file')
logconsole = logging.getLogger('console') 

url = 'http://uol.com.br/essapaginanaoexiste'


try:
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.HTTPError as err:
    logconsole.error(f' HTTP ERROR: {err}')
except requests.exceptions.Timeout as e:
    logconsole.error(f'TIMEOUT - tempo limite excedido : {e}')
except requests.exceptions.ConnectionError as e:
    logconsole.error(f'CONNECTION ERROR: {e}')
except Exception as err:
    logconsole.critical(f'Erro desconhecido - {e}')



exit()
logfile.debug('DEBUG FILE TESTE')
logfile.info('teste')
logconsole.info('teste')
logconsole.debug('DEBUG CONSOLE TESTE')
logconsole.error('TESTE')
logconsole.critical('TESTE CRITICAL')

exit()
# definições 

#1: logger

logger = logging.getLogger(__name__) 

#2: formato de saída
log_format = "%(asctime)s - %(levelname)s - %(message)s "

#3: handler

#4: setar o formato de saída
logger.setFormatter = logging.Formatter(log_format)

#5: definir nível 

logger.setLevel(logging.INFO)



