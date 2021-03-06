
from os import environ

import requests 
import functools

from flask import Blueprint, render_template, jsonify, redirect,  request, session


def login_required(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if not session.get('auth'):
            return redirect('http://example.com/session')
        return function(*args, **kwargs)
    return wrapper

blueprint = Blueprint('gitea', __name__) 

GITEA_TOKEN = environ['GITEA_TOKEN']
GITEA_URL = 'http://200.100.50.30:3000/api/v1'

endpoints = {
        'users': f'{GITEA_URL}/admin/users',
        'repos': f'{GITEA_URL}/repos/search',
        
}

headers = {
        'Authorization': f'token {GITEA_TOKEN}'
}



@blueprint.route('/', methods = ['GET'])
@login_required
def gitea_page():
    #1: pegar usuários
    
    try:
        response = requests.get(endpoints['users'], headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        #log
        return jsonify({'mensagem': f'Não foi possível estabelecer conexão com o Gitea {err}'})
    else:
        users =[{
            'login': user['login'],
            'email': user['email'],
            'admin': user['is_admin']
                
        } for user in response.json()
    ]
    #2: pegar projetos
        try:
            response = requests.get(endpoints['repos'], headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return jsonify({'mensagem': 'Não foi possível estabelecer conexão com o gitea'})
        else:
            projects= [
                {
                    'id': project['id'],
                    'owner': project['owner']['login'],
                    'nome': project['name'],
                    'ssh_url': project['ssh_url']
                    
                } for project in response.json()['data'] 
            ]

    #3: criar um payload com as informações
            context = {
                'users': users,
                'projects': projects
            }
            
    #4: renderizar a página com o contexto
    return render_template('gitea.html', context=context) 


@blueprint.route('/add/users', methods = ['POST'])
def add_user():

    #0: resgatar informações do formulário
    #1: formatar o payload para add user no gitea
    context = {

        'email': request.form.get('email'),
        'full_name': '',
        'must_change_password': True,
        'password': '!23Mudar',
        'send_notify': False,
        'source_id': 0,
        'is_admin': request.form.get('is_admin'),
        'username': request.form.get('username')
        
    }

    #3: realizar um post no gitea
    try:

        response = requests.post(
                    endpoints['users'], headers=headers, json=context)
    
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        return jsonify({'mensagem':'Erro ao processar a requisição no Gitea'})
    else:
    
        #4: renderizar a página padrão
        return redirect('/')


@blueprint.route('/sign-in')
def sign_in():
    return jsonify({'message': 'você não está logado', 'session': session.get('auth')})
