
inteiro = 1
double = 1.50
string = 'isto é uma string'
tuplas = (0,1,2,3, "Guilherme", 3.50)


print(tuplas[-1]) # 3.50

lista = [0,2,3,4,'Nome', [8,9,10]]

print(lista[1])

lista.append('novo elemento')

dic = {
    'nome': 'Guido Van Rossum',
    'linguagem': 'Python',
    'ano': 1990,
    'data': {
            'data-chave':'novo valor',
            'outra chave': 'outro valor'
        },
}

print(dic['nome']) #Guido
dic['nova_chave'] = 'Novo Valor'
