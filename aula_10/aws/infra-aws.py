# script de teste

import uuid
from time import sleep

import boto3

class InfraAWS:
    def __init__(self):
        self.ec2 = boto3.resource('ec2')
        self.client = None
        self.vpc = None
        self.gateway = None
        self.route = None
        self.routetable = None
        self.subnet = None
        self.security_group = None
        self.key_pair = None
        self.instances = None

    def geradorDeNomes(prefixo):
        return ''.join([prefixo, '_', str(uuid.uuid4())])
    
    def boto3Client(self, servico):
        self.client = boto3.client(servico) 


    def criarVPC(self,
            CIDR = '172.16.0.0/16', 
            tag = geradorDeNomes('teste')):
        
        self.vpc = self.ec2.create_vpc(CidrBlock = CIDR)

        self.vpc.create_tags(Tags=[{"Key": "Name", "Value": tag}])

        # Mesmo exemplo de tags se utilizássemos o client
        #self.ec2.create_tags(Resources =[
        #    self.vpc['Vpc']['VpcId'] <- note que a forma de acesso é bem diferente
        #    ], 
        #    Tags=[
        #        { 'Key': 'Name', 
        #         'Value': tag 
        #        }
        #    ]
        #)
        
        self.vpc.wait_until_available()
        
        self.boto3Client('ec2')

        self.client.modify_vpc_attribute(
                VpcId = self.vpc.id, 
                EnableDnsSupport = { 'Value' : True }
        )

        self.client.modify_vpc_attribute( 
                VpcId = self.vpc.id, 
                EnableDnsHostnames = { 'Value' : True }
        )

    def deletarVPC(self):
        self.vpc.delete()


    def criarInternetGateway(self):
        self.gateway = self.ec2.create_internet_gateway()
        self.vpc.attach_internet_gateway(InternetGatewayId=self.gateway.id)

    def deletarInternetGateway(self):
        self.vpc.detach_internet_gateway(InternetGatewayId=self.gateway.id)
        self.gateway.delete()
        
    def criarRota(self):
        self.routetable =  self.vpc.create_route_table()
        self.route = self.routetable.create_route(
                DestinationCidrBlock='0.0.0.0/0', 
                GatewayId= self.gateway.id
        )


    def deletarRota(self):
        self.route.delete()

    def deletarTabelaDeRotas(self):
        self.routetable.delete()


    def criarSubRede(self, CIDR = '172.16.1.0/24'):
        self.subnet = self.ec2.create_subnet(CidrBlock=CIDR, VpcId= self.vpc.id)
        self.routetable.associate_with_subnet(SubnetId= self.subnet.id)

    def deletarSubRede(self):
        self.subnet.delete()


    def criarSecurityGroup(self, 
            nome = 'SSH-ONLY', 
            desc = 'Somente acesso via SSH'):

        self.security_group = self.ec2.create_security_group(
                GroupName=nome, 
                Description= desc, 
                VpcId= self.vpc.id
            )

        self.security_group.authorize_ingress(
                CidrIp='0.0.0.0/0', 
                IpProtocol='tcp', 
                FromPort=22, 
                ToPort=22
            )
    def deletarSecurityGroup(self):
        self.security_group.delete()

    def criarChaves(self, key_name):
        with open('ec2-keypair.pem', 'w') as chave:
            self.key_pair = self.ec2.create_key_pair(KeyName = key_name)
            conteudo_chave = str(self.key_pair.key_material)
            chave.write(conteudo_chave)

    def deletarChaves(self):
        self.key_pair.delete()


    def criarInstancia(self, tipoInstancia='t2.micro', imagem='ami-05c0d7f3fffb419c8'):
        self.instances = self.ec2.create_instances(
                ImageId= imagem, #https://wiki.debian.org/Cloud/AmazonEC2Image/Buster
                InstanceType= tipoInstancia,
                MaxCount=1,
                MinCount=1,
                NetworkInterfaces=[{
                    'SubnetId': self.subnet.id,
                    'DeviceIndex': 0,
                    'AssociatePublicIpAddress': True,
                    'Groups': [self.security_group.group_id]
                }],
                KeyName = self.key_pair.key_name)



    def terminateAll(self):
        print('Terminando todas as instancias...')
        self.ec2.instances.terminate()
        sleep(5)
        print('Removendo chaves...')
        sleep(1)
        self.deletarChaves()
        print('Removendo Security Groups')
        sleep(1)
        self.deletarSecurityGroup()
        print('Removendo rota ...')
        sleep(1)
        self.deletarRota()
        print('Removendo sub rede')
        sleep(1)
        self.deletarSubRede()
        print('Removendo Tabela de Rotas...')
        sleep(1)
        self.deletarTabelaDeRotas()
        print('Removendo Gateway...')
        sleep(1)
        self.deletarInternetGateway()
        print('Remover VPC...')
        sleep(1)
        self.deletarVPC()
        
if __name__ == '__main__':
    aws = InfraAWS()
    aws.criarVPC()
    aws.criarInternetGateway()
    aws.criarRota()
    aws.criarSubRede()
    aws.criarSecurityGroup()
    aws.criarChaves('ec2-teste')
    aws.criarInstancia()



## VPC

## Gateway

## Route Table and Subnet

## Security Group

## EC2 Instance
