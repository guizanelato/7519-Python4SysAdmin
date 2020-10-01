
import docker as dc
from flask import Blueprint, render_template, jsonify, flash, redirect

blueprint = Blueprint('docker', __name__) 

@blueprint.route('/docker', methods = ['GET'])
def docker_page():
    
    try:
        docker  = dc.DockerClient(base_url='unix://var/run/docker.sock')
    except Exception as err:
        return jsonify({'timestamp': str(datetime.now()), 
                        'mensagem': 'Não foi possível conectar ao docker'
                    })

        #flash('Não foi possível conectar ao serviço do Docker', err)
        # possível entrada de log
    else:
        context = [        
            {
                'id': container.short_id,
                'imagem': container.image.tags[0],
                'status': container.status
                
            } for container in docker.containers.list(all=True)
                
        ]

        return render_template('docker.html', context=context) 

@blueprint.route('/docker/<container_id>/start', methods = ['GET'])
def docker_start(container_id): 
    try:
        docker  = dc.DockerClient(base_url='unix://var/run/docker.sock')
    except Exception as err:
        return jsonify({'timestamp': str(datetime.now()), 
                        'mensagem': 'Não foi possível conectar ao docker'
                    })

        #flash('Não foi possível conectar ao serviço do Docker', err)
        # possível entrada de log
    else:
        
        container = docker.containers.get(container_id)

        if container:
            container.start()
            # Log INFO ->  container iniciado
        return redirect('/docker')


@blueprint.route('/docker/<container_id>/stop', methods = ['GET'])
def docker_stop(container_id): 
    try:
        docker  = dc.DockerClient(base_url='unix://var/run/docker.sock')
    except Exception as err:
        return jsonify({'timestamp': str(datetime.now()), 
                        'mensagem': 'Não foi possível conectar ao docker'
                    })

        #flash('Não foi possível conectar ao serviço do Docker', err)
        # possível entrada de log
    else:
        
        container = docker.containers.get(container_id)

        if container:
            container.stop()
            # Log INFO ->  container iniciado
        return redirect('/docker')



