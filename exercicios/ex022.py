# * Exercício 022
#                 crie um programa que leia o nome completo com todas as letras:
#                 - maiusculas
#                 - minusculas
#                 - qtd letras sem espaço
#                 - qtd letras o primeiro nome


# Eu
"""
print('\n{:=^40}\n'.format(' Desafio 022 '))

nome = str(input('Qual seu nome: '))
print('Maiúsculas: ', nome.upper())
print('Minúscula: ', nome.lower())
lNome = nome.split()                                    # Separei as palavras
jNome = ''.join(lNome)                                  # Juntei sem espços
print('Qtd sem espaço: ', len(jNome))
print('Qtd letras do primeiro nome:',len(lNome[0]))
"""

# Professor...

nome = str(input('Qual seu nome: ')).strip()            # para remover os caracater iniciais e finais
print('Maiúsculas: ', nome.upper())
print('Minúscula: ', nome.lower())
print('Seu nome tem ao todos {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))                 # O primeiro 'espaço' estára na posição: 0,1,2,'3'. Isso significa que a qtd anterior é letras, que é igual a 3


