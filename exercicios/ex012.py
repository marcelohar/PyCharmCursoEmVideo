#  * Exercício 012
#         Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('{:=^40}'.format(' Desafio 012 '))

val = float(input('Informe o valor do produto: '))
newVal = val - (val * 0.05)

print('Preço do produto com 5% de desconto: {}'.format(newVal))

