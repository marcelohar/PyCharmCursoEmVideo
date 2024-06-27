# * Exercício 016
#             Crie um programa que leia um núemro real qualquer pelo teclado e mostre na tela a sua porção inteira
#             ex: digite um núemro 6.127
#                 O número tem a parte interia 6

from math import trunc                                                  # importei somente o objeto trunc da classe math

print('\n{:=^40}\n'.format(' Desafio 016 '))

n = float(input('Digite um número: '))

print('A parte inteira do número ({}) é {}.'.format(n, trunc(n)))     # não preciso usar especificar a classe para puchar o metodo (math.trunc() )
