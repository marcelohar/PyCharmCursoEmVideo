# * Exercício 010
#         Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (considere US$ 1,00 = 3,27)

print('{:=^40}'.format(' Desafio 010 '))

val = float(input('Digite a quantidade de dinheiro disponível: '))
dol = val / 3.27

print('Com R${:.4}, pode comprar ${:.4}'.format(val, dol)) # Com a formatão ':.4' acontece erro se o núemoro for grande.
