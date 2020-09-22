
# funcoes nativas
print('isto é uma função nativa')

# funcoes a partir da bib. padrao
# import random
from random import randint
from calc import soma

print(randint(0,10))

print(soma(10,10))

# funcao anonima

jujuba = lambda x,y: x+y
print(jujuba(10,2)) # 12

