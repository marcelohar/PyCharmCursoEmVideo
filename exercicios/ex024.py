#  * Exercício 024
#                 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

# Eu...
"""
print('\n{:=^40}'.format(' Desafio 024 '))

cid = str(input('Informe o nome da cidade: '))
nome = cid.lower()
nome = nome.strip()                                # Removi os espaços iniciais e finais.
nome = nome.find('santo')

if nome == 0:
    print('A cidade começa com "Santo"!')

else:
    print('A cidade Não começa com "Santo"!')
"""
# Professor

cid = str(input("Em que cidade você nasceu? ")).strip()         # .strip() para remover os espaços iniciais e finais
print(cid[:5].upper() == 'SANTO')                               # 'santo' e = 5 letras, mas lembrar que começa em '0', porém está até ':5' pq sempre pega uma posição a menos.
                                                                # '.upper() deixar tudo em maiúsculo e com parar se é = a 'SANTO' SE FOR, TERÁ O O RETORO DE "TRUE"
