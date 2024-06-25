# * Exercício 013
#         faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

print('{:=^40}'.format(' Desafio 013 '))

sal = float(input('Informe o salário: R$ '))
newSal = sal + (sal * 0.15)

print('Salário atualizado com 15% de aumento: R$ {:.2f}'.format(newSal))
