# * Exercício 030
#         Cria um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

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
