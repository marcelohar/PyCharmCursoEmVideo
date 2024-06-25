# Exercício 005
#   Faça um programa que leia um númeo inteiro e mostre na tela o seu sucessor e seu antecessor.


print('{:=^40}'.format(' Desafio 005 '))

num = int(input('Digite um número inteiro: '))

print('O antecessor de {} é {}. \no sucessor de {} é {}. '.format(num, (num-1), num, (num+1)))

# Lembrando que de primeira usei 3 variáveis, mas quanto mais variável mais memória consome.

