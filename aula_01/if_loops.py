
if 4 < 5:
    print('você sabe de matemática')
else:
    print('você não sabe de matemática')


idade = int(input('Informe a sua idade: '))
hab = input('Possui Habilitação? Sim/Não: ')

if idade >=18 and hab.lower() == 'sim':
    print('você pode dirigir')
else:
    print('você não possui os requisitos necessários para dirigir')


cont = 0

while cont < 10:
    print(cont)
    cont = cont + 1 # cont +=1


dic = {'nome': 'Guido van Rossum',
       'linguagem': 'Python'

        }

lista = [0,1,2,3,4]

for chave in dic.keys():
    print(f'key:{chave}', dic[chave])

for num in lista:
    print(num)

for indice in range(len(lista)):
    print(lista[indice])



