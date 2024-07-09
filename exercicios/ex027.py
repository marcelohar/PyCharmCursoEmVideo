# * Exercício 027
#                 faça uma programa para ler o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Eu...
"""
print('\n{:=^40}'.format(' Desafio 027 '))

nome = str(input('Digite o nome completo: '))
divNome = nome.split()
tamList = len(divNome) - 1

print('Primeiro nome: {}'.format(divNome[0]))
print('Último nome: {}.'.format(divNome[tamList]))
"""

# Professor...
n = str(input('Digite seu nome completo: ')).strip()        # .strip() remove os  espaços iniciais e finais
nome = n.split()                                            # separa cada palavra da string e dá a ela novos índices
print('Muito prazer em te conhecher!')
print('Seu primeiro nome é {}'. format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))
