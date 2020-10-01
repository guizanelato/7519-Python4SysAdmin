import docker as dc

try:
    docker  = dc.DockerClient(base_url='unix://var/run/docker.sock')
except Exception as err:
    print('Não foi possível conectar ao Docker', err)


container_list = [
        {
            'id': container.short_id,
            'imagem': container.image.tags[0],
            'status': container.status
            
        } for container in docker.containers.list(all=True)
        
]

