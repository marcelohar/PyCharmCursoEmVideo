# * Exercício 011
#         Faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá,
#         sabendo que cada litro de tinta pinta uma área de 2m^2

print('{:=^40}'.format(' Desafio 011 '))

alt = float(input('Digite a altura: '))
lar = float(input('Didite a largura: '))
area = alt * lar
litros = area / 2

print('É necessário {}L para pintar uma área de {}m quadrados!'.format(litros, area))
