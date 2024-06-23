# Exercício 008
#         Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

print('\n{:=^40}'.format(' Desafio 008 '))

metro = int(input('Digite a QTD em metro: '))

cm = metro * 100
mm = cm * 10

print('Em {}m temos {}cm '
      '\nEm {}cm temos {}mm'.format(metro, cm, cm, mm))
