# * Exercício 023
#                 Faca um programa que leia um número de 0  9999 e mostre na tela cada um dos gigitos separados
#                 ex: 1834
#                     unidade: 4
#                     dezena: 3
#                     centena: 8
#                     milhar: 1

print('\n {:=^40}'.format(' Desafio 023 '))

n = str(input('Informe um número de até 4 digitos: '))


print('Unidade: {} \n'
      ' Dezena: {} \n'
      'Centena: {} \n'
      ' milhar: {}'.format(n[3], n[2], n[1], n[0]))

