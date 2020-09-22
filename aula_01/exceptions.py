

try:
    # código potencialmente travável
    num1 = 10
    num2 = 0
    print(num1/num3)
except ZeroDivisionError as err:
    print('Não divirás por zero', err)
except NameError: 
    print('Voce nao definiu a variavel')
except Exception as err:
    print(f"erro inesperado - {err}")
else:    
    # caso o código for bem sucedido
    print('divisão executada com sucesso') 
finally:
    print('passei pelo finally')
    # executa independente se o foi bem sucedido

