#  * Exercício 017
#             Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo, calcule e mostre o comprimento da hipotenusa
#             obs: tem modulo. tentar achar?
import math

print(('\n {:=^40} \n'.format(' Desafio 017 ')))

print('Infome...')
cO = int(input('Cateto Oposto: '))
cA = int(input('Cateto Adjacente: '))
h = math.hypot(cA, cO)

print("Hipotenusa: {:.0f}".format(h))




