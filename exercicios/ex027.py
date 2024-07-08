# * Exercício 027
#                 faça uma programa para ler o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('\n{:=^40}'.format(' Desafio 027 '))

nome = str(input('Digite o nome completo: '))
divNome = nome.split()
tamList = len(divNome) - 1

print('Primeiro nome: {}'.format(divNome[0]))
print('Último nome: {}.'.format(divNome[tamList]))


