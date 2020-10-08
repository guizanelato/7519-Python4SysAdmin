
import functools

from flask import Blueprint, redirect, jsonify, render_template, request, session

import ldap3


blueprint = Blueprint('auth', __name__)


LDAP_SERVER = '200.100.50.80:389'

OBJECT_CLASS = [
    'top',
    'person',
    'organizationalPerson',
    'inetOrgPerson',
    'posixAccount'
]

USERNAME = 'admin'
PASSWORD = '4linux'

LDAP_STRING = f'cn={USERNAME},dc=example, dc=com, dc=br'



def login_required(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if not session.get('auth'):
            return redirect('/sign-in')
        return function(*args, **kwargs)
    return wrapper


def create_ldap_connection():
	try:
            conn = ldap3.Connection(ldap3.Server(LDAP_SERVER),
                                    LDAP_STRING, 
                                    PASSWORD)

	except Exception as err:
		return jsonify({'mesagem': 'Não foi possível estabelecer conexão com o LDAP',
					   'erro': f'{err}'})
	else:
            conn.bind()
            return conn


def ldap_search(ldap_connection, email):
	ldap_connection.search(
		"uid={}, dc=example, dc=com, dc=br".format(email),
		'(objectClass=person)',
		attributes = [
			'sn',
			'userPassword'
		]
	)
	
	return ldap_connection.entries


def ldap_insert(ldap_connection, user_form):

	user = {
                    'cn': user_form.get('nome'),
                    'sn': user_form.get('sobrenome'),
                    'mail': user_form.get('email'),
                    'uidNumber': id(USERNAME),
                    'gidNumber': 1,
                    'uid': user_form.get('email'),
                    'homeDirectory': '/home/{}.{}'.format(
                            user_form.get('nome'),
                            user_form.get('sobrenome'),
                    ),
                    'userPassword': user_form.get('senha'),
                }


	res = ldap_connection.add(
			'uid={},dc=example,dc=com,dc=br'.format(
					user['mail']
				),
				OBJECT_CLASS,
				user
	)

	if res:
		return True
	
	return False


@blueprint.route('/' , methods = ['GET', 'POST'])
def sign_in():

	if request.method == 'POST':
		#validacao de login
            ldap_conn = create_ldap_connection()
            result = ldap_search(ldap_conn, request.form.get('email'))
            
            if len(result) > 0:
                ldap_user_passwd = result[0]['userPassword']
                if request.form.get('senha') == ldap_user_passwd.value.decode():
                    session['auth'] = True
                    return redirect('http://example.com/service/gitea')
                else:
                    return jsonify({'message': request.form, 'senha': ldap_user_passwd.value.decode()})
		

	return render_template('sign-in.html', context = None)


@blueprint.route('/sign-up', methods = ['GET', 'POST']) 
def sign_up():
	
    if request.method == 'POST':
            ldap_conn = create_ldap_connection()
            if ldap_insert(ldap_conn, request.form):
                return  redirect('/')
            else:
                return jsonify({'message': request.form})
            
    return render_template('sign-up.html', context = None)


