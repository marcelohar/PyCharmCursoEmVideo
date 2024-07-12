# * Exercício 030
#         Cria um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.


# Eu...

"""

print('\n{:=^40}'.format(' Desafio 030 '))

dNum = str(input('Digite um número inteiro: ')).strip()

if dNum.isnumeric() and not dNum.isspace():
    n = int(dNum)
    if n % 2 == 0:
        print('O número {} é PAR!'.format(n))
    else:
        print('O número {} é ÍMPAR!'.format(n))
else:
    print('[ERRO] Dados inválidos!')
"""
# Professor...

número = int(input('Me diga um número qualquer: '))
resultado = número % 2

if resultado == 0:
    print(f'O número {número} é PAR')
else:
    print('O número {} é ÍMPAR'.format(número))
