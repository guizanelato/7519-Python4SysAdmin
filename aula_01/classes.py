
class Bicicleta:
    def __init__(self): # self <> this
        self.aro = 26   # atributos <> variáveis
        self.marchas= 11
        self.velocidade = 0
        self.tipo = 'speeed'


    def acelerar(self):
        self.velocidade += 10

    def brecar(self): # funcoes <> métodos
        if self.velocidade == 0:
            return "bicicleta está em repouso"
        self.velocidade -= 10

caloi = Bicicleta()


