#  * Exercício 018
#             Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#              cosseno e tangente desse ângulo.
import math

print('\n {:=^40} \n'.format(' Desafio 018 '))

ang = int(input('Informe o angulo: '))

angR = math.radians(ang)                # Por algum motivo tenho que converter o angulo em radianos

s = math.sin(angR)
c = math.cos(angR)
t = math.tan(angR)

print('Sen: {:.3f}. \n'
      'Cos: {:.3f}. \n'
      'tag: {:.3f}.'
      .format(s, c, t))
