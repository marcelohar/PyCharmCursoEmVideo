#  * Exercício 018
#             Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#              cosseno e tangente desse ângulo.


from math import sin, cos, tan, radians               # IMPORTEI SOMENTE OS NECESSÁRIO

print('\n {:=^40} \n'.format(' Desafio 018 '))

ang = int(input('Informe o angulo: '))

angR = radians(ang)                # Por algum motivo tenho que converter o angulo em radianos

s = sin(angR)                      # NÃO USEI 'math.sin() pq importei somente o que preciso.
c = cos(angR)
t = tan(angR)

print('Sen: {:.2f}. \n'       
      'Cos: {:.2f}. \n'
      'tag: {:.2f}.'
      .format(s, c, t))
