
from os import environ
import requests


GITEA_TOKEN = environ['GITEA_TOKEN']
GITEA_URL = 'http://200.100.50.10:3000/api/v1'

endpoints = {
        'users': f'{GITEA_URL}/admin/users',
        'repos': f'{GITEA_URL}/repos/search',
        
        }

headers = {
        'Authorization': f'token {GITEA_TOKEN}'
        
        }

response = requests.get(endpoints['repos'], headers=headers, json={'q': ''})




exit()
# lembrar do tratamento de exceptions

# listar usuários 
response = requests.get(
            endpoints['users'], headers=headers)


print(response.json())


# criar um usuário

payload = {
    'email': 'guilherme.zanelato@4linux.com.br',
    'full_name': 'Guilherme Zanelato Corrêa',
    'must_change_password': True,
    'password': '!23Mudar',
    'send_notify': False,
    'source_id': 0,
    'username': 'guizanelato'
        
}

response = requests.post(
            endpoints['users'], headers=headers, json=payload)




