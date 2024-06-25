# * Exercício 011
#         Faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá,
#         sabendo que cada litro de tinta pinta uma área de 2m^2

print('{:=^40}'.format(' Desafio 011 '))

lar = float(input('Didite a largura: '))
alt = float(input('Digite a altura: '))

area = alt * lar
litros = area / 2

print('É necessário {:.2f}L para pintar uma área de {:.2f}m²  quadrados!'.format(litros, area))


