#  * Exercício 028
#         Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#         O programa deverá escrever na tela se o usuário venceu ou perdeu
import random

print('\n{:=^40}'.format(' Desafio 028 '))

n = [0, 1, 2, 3, 4, 5]
r = random.choice(n)

print(r)
us = str(input('De "0" a "5", tente adivinhar qual número eu escolhi: '))

if us.isnumeric() and not us.isspace():
    us = int(us)
    if us == r:
        print('Parabéns! Realmente pense no número {}'.format(r))
    else:
        print('Errouuuu! Tente novamente!')

else:
    print('[ERRO] DADOS INVÁLIDOS!')
