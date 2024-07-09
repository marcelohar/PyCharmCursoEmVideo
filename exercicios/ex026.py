# * Exercício 026
#                 Faça um programa que leia uma frase pelo teclado e mostre:
#                  - qtd de vezes que aparece a letra "A"
#                  - Qual a posição que ela aparede a primeira vez
#                  - Qual a posição ela aparece a última vez.

# Eu...
"""
print('\n{:=^40}'.format(' Desafio 026 '))

frase = str(input('Digite uma frase: '))
frase = frase.strip()
frase = frase.lower()
tamFrase = len(frase)
posi=[]

for i in range(tamFrase):                       # Para cada posição de i no intervalo de 'tamanho da frase'
    if frase[i] == 'a':
        posi.append(i)

tamPosi = int(len(posi))

print('Qtd de letra "A": {}'.format(frase.count('a')))                      # poderia aproveitar  tamposi
print('Posição da primeira letra: {}.'.format(frase.find('a') + 1))         # poderia aproveitar  tamposi

print('Ultima posição da letra: {} '.format(posi[tamPosi - 1] + 1))         # -1 pq a o vetor tem 3 posições e começa no 0, então é a posição 2 ou seja:0, 1, 2!
                                                                            # +1 apenas para aparecer visualmente o lugar da letra
"""

# Professor...

frase = str(input('Digite uma frase: ')).upper().strip()            # .upper() = tudo maiúsculo e .strip = remova os espaços iniciais e finais.
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))