# * Exercício 022
#                 crie um programa que leia o nome completo com todas as letras:
#                 - maiusculas
#                 - minusculas
#                 - qtd letras sem espaço
#                 - qtd letras o primeiro nome

print('\n{:=^40}\n'.format(' Desafio 022 '))

nome = str(input('Qual seu nome: '))
print('Maiúsculas: ', nome.upper())
print('Minúscula: ', nome.lower())
lNome = nome.split()                                    # Separei as palavras
jNome = ''.join(lNome)                                  # Juntei sem espços
print('Qtd sem espaço: ', len(jNome))
print('Qtd letras do primeiro nome:',len(lNome[0]))




