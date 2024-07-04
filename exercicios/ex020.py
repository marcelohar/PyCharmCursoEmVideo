# * Exercício 020
#             O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#              Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada. (uma sequencia na ordem)

from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

shuffle(lista)                                   # shuffle =  embaralhar

print('Orden de apresentção: {}'.format(lista))


'''
Versão Marcelo

import random

print('\n {:=^40} \n'.format(' Desafio 020 '))

print('Insira os nomes dos alunos.')
nomes = []
for i in range(4):
    nome = input('{}º Aluno: '.format(i+1))
    nomes.append(nome)                              # Anexando cada nome em uma posição do vetor

nomesAleatorios = random.sample(nomes, len(nomes))  # novo vetor que recebe os nomes da lista 'nomes'
                                                    # de acordo com o seu tambanho 'len(nomes)

print('\nOrdem dos escolhidos.')
c = 0
for i in nomesAleatorios:                        # Para cada 'nome' dentro da lista 'nomesAleatorios, imprima na tela o nome
    c = c + 1
    print('{}º {}.'.format(c, i))


'''