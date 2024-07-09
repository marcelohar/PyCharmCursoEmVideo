# * Exercício 023
#                 Faca um programa que leia um número de 0  9999 e mostre na tela cada um dos gigitos separados
#                 ex: 1834
#                     unidade: 4
#                     dezena: 3
#                     centena: 8
#                     milhar: 1

# Eu...
"""
print('\n {:=^40}'.format(' Desafio 023 '))

n = str(input('Informe um número de até 4 digitos: '))
n = '{:0>4}'.format(n)
print(n)
print('Unidade: {} \n'
      ' Dezena: {} \n'
      'Centena: {} \n'
      ' milhar: {}'.format(n[3], n[2], n[1], n[0]))
"""

# Professor...

num = int(input('Informe um número: '))
u = num // 1 % 10                           # num 'divisão inteira' por 1 e do resultado, faça o 'resto da divisão' entre o 'resultado' e '10'. trara o resto da divisão.
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(' Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))





