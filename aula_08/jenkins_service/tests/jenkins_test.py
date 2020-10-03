
import jenkins

JENKINS_OPTS = {
    'url': 'http://200.100.50.20:8080',
    'username': 'developer',
    'password': '4Linux@'
}

try:
    client = jenkins.Jenkins(**JENKINS_OPTS)
except Exception as err:
    print('Não foi possível estabelecer conexão com o Jenkins')


