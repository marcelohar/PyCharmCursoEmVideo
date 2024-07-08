#  * Exercício 024
#                 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

print('\n{:=^40}'.format(' Desafio 024 '))

cid = str(input('Informe o nome da cidade: '))
nome = cid.lower()
nome = nome.strip()                                # Removi os espaços iniciais e finais.
nome = nome.find('santo')

if nome == 0:
    print('A cidade começa com "Santo"!')

else:
    print('A cidade Não começa com "Santo"!')
