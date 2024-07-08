#  * Exercício 025
#                 Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome

print('\n{:=^40}'.format(' Desafio 025 '))

nome = str(input('Nome: '))
nome = nome.lower()
nome = nome.strip()
posNome = nome.find('silva')

if posNome == -1:
    print('Não tem o sobrenome "Silva"')
else:
    print('Sobrenome "Silva" Encontrado na posição {}.'.format(posNome + 1))
