# Exercício 005
#   Faça um programa que leia um númeo inteiro e mostre na tela o seu sucessor e seu antecessor.


print('{:=^40}'.format(' Desafio 005 '))

num = int(input('Digite um número inteiro: '))

sucessor = num + 1

antecessor = num - 1

print('O antecessor de {} é {} e o sucessor de {} é {}. '.format(num, antecessor, num, sucessor))
