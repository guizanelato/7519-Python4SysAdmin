
import ldap3

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

LDAP_STRING= f'cn={USERNAME}, dc=example, dc=com, dc=br'


conexao = ldap3.Connection(
			ldap3.Server(LDAP_SERVER),
			LDAP_STRING, PASSWORD)

conexao.bind()

# consulta 

conexao.search("uid=developer@example.com, dc=example, dc=com, dc=br", '(objectClass=person)', attributes= ['sn', 'userPassword'])

resultado = conexao.entries

senha = resultado[0]['userPassword']

# ver senha no formado de string

senha =  senha.value.decode()


exit()
# inserir usuário 

new_user = {
    'cn': 'developer',
    'sn': '4linux',
    'mail': 'developer@example.com',
    'uidNumber': id(USERNAME),
    'gidNumber': 1,
    'uid': 'developer@example.com',
    'homeDirectory': '/home/{}.{}'.format(
        'developer',
        '4linux'),
    'userPassword': '123456'
             
}


result = conexao.add(
            'uid={}, dc=example, dc=com, dc=br'.format(
                new_user['mail']),
            OBJECT_CLASS,
            new_user
)






