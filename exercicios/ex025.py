#  * Exercício 025
#                 Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome

# Eu...

"""
print('\n{:=^40}'.format(' Desafio 025 '))

nome = str(input('Nome: '))
nome = nome.lower()
nome = nome.strip()
posNome = nome.find('silva')

if posNome == -1:
    print('Não tem o sobrenome "Silva"')
else:
    print('Sobrenome "Silva" Encontrado na posição {}.'.format(posNome + 1))
"""

# Professor...
nome = str(input('Qual é seu nome completo? ')).strip()             #.strip() remove os espaços iniciais e finais
print('Seu nome tem silva? {}'.format('silva' in nome.lower()))     # 'silva' está em: nome '.lower' = em minúsculo? se sim é true



