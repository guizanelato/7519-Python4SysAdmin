
from flask import Blueprint, render_template, jsonify, redirect,  request
import jenkins


blueprint = Blueprint('jenkins', __name__) 

# verificar uso de variáveis de ambiente
JENKINS_OPTS = {
        
    'url': 'http://200.100.50.40:8080',
    'username': 'developer',
    'password': '4Linux@'
        
}

def jenkins_client(opts):
    try:
        client = jenkins.Jenkins(**opts)
    except Exception as err:
        #log
        print('Não foi possível estabeler conexão com o jenkins')
    else:
        return client


def get_jobs():
    client = jenkins_client(JENKINS_OPTS)
    return [
        {
            'job': job.get('name'),
            'url': job.get('url'),
            'status': job.get('color')
        }  for job in client.get_all_jobs()      
    ]

def get_nodes():
    client = jenkins_client(JENKINS_OPTS)
    return [
        {
            'node': node.get('name'),
            'status': get_node_status(node.get('offline'))
        }  for node in client.get_nodes()       
    ]

    
def get_node_status(status):
    if not status:
        return 'Online'
    else:
        return 'Offline'

@blueprint.route('/', methods = ['GET'])
def jenkins_page():

    context = {
        'jobs': get_jobs(),
        'nodes': get_nodes()
    }
    
    return render_template('jenkins.html', context=context)

@blueprint.route('/<jobname>/run', methods = ['GET'])
def job_run(jobname):
    client = jenkins_client(JENKINS_OPTS)
    client.build_job(jobname)

    return redirect('/')
    


