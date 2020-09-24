
import json
from datetime import datetime

import requests

"""
O rot 13 é uma forma clássica de cifrar uma mensagem - consiste em coletar cada caractere
de uma mensagem e substituí-lo pelo caractere 13 posições à frente. por exemplo:

a letra 'a' seria convertida em 'n' 
a letra 'b' seria convertida em 'o'

e assim por diante...

Considerando o alfabeto que conhecemos e incluindo os algarismos de 0 até 9:

- faça uma requisição que colete a mensagem cifrada no seguinte endereço: 
-> https://python521.herokuapp.com/desafio

A partir da mensagem recebida, é pedido para decifrar a mensagem e encaminhar a resposta para o endereço através do método POST:
 - https://python521.heroku.com/validar/desafio

a resposta deverá ter o seguinte formato: 
    {
        'timestamp': data e horário do momento
        'data': mensagem cifrada
    }

ex:

{
    "timestamp": "Mon, 21 Sep 2020 14:53:30 GMT",
    "data": "Socorro, subi em um onibus no marrocos"

}

dica: para obter o formado do timestamp , utilize o pacote datetime e seu método now()

"""


#1: url alvo
url = 'https://python521.herokuapp.com/validar/desafio'

#2: json 

payload = {
        'timestamp' : str(datetime.now()),
        'data' : 'eu não sei a resposta!!!@@#$%'

        }

#3: enviar as informações para o endpoint
## trecho passível de erro
response = requests.post(url, json=payload)
print(response.json())
