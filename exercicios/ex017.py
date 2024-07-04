#  * Exercício 017
#             Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo, calcule e mostre o comprimento da hipotenusa
#             obs: tem modulo. tentar achar?

from math import hypot



print(('\n {:=^40} \n'.format(' Desafio 017 ')))

print('Infome...')
cO = float(input('Cateto Oposto: '))
cA = float(input('Cateto Adjacente: '))
h = hypot(cA, cO)

print("Hipotenusa: {:.2f}".format(h))




2.5