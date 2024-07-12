#  * Exercício 028
#         Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#         O programa deverá escrever na tela se o usuário venceu ou perdeu


# Eu
"""
import random

print('\n{:=^40}'.format(' Desafio 028 '))

n = [i for i in range(6)]                   # cria uma lista com 5 posições.
print(n)
r = random.choice(n)

us = str(input('De "0" a "5", tente adivinhar qual número eu escolhi: ')).strip()

if us.isnumeric() and not us.isspace():
    us = int(us)
    if us == r:
        print('Parabéns! Realmente pensei no número {}'.format(r))
    else:
        print('Errouuuu! Pensei no número {}. Tente novamente!'.format(r))

else:
    print('[ERRO] DADOS INVÁLIDOS!')
"""

# Professor...

from random import randint              # Para gerar um inteiro
from time import sleep                  # Para deixar o programa em um loop durante um tempo

computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)                                                                                    # em espera por 2 segundos.
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))


