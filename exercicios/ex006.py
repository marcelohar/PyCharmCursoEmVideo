#   Exercício 006
#       Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('{:=^40}'.format(' Desafio 006 '))

num = int(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
rQuadrada = num ** 0.5

print('O dobro de {} é {}. \n'
      'O triplo de {} é {}. \n'
      'A Raiz quadrada de {} é {}.'. format(num, dobro, num, triplo, num, rQuadrada))
