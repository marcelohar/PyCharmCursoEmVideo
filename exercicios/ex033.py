# * Exercício 033
#         Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Eu... esqueci de de fazer qual era o maior e qual era o menor
"""
print('\n{:=^40}'.format(' Desafio 033 '))

print('Informe 3 número')
sN1 = str(input('1º Nº: ')).strip()
sN2 = str(input('2º Nº: ')).strip()
sN3 = str(input('3º Nº: ')).strip()

if sN1.isnumeric() and sN2.isnumeric() and sN3:
    n1 = int(sN1)
    n2 = int(sN2)
    n3 = int(sN3)

    if n3 > n2 or n3 > n1:
        print('O 3número {} é maior que {} e o {}!'.format(n3, n2, n1))
    elif n2 > n1:
        print('O 2número {} é maior que {} e o {}'.format(n2, n1, n3))
    else:
        print('O 1número {} é maior que {} e o {}'.format(n1, n2, n3))

else:
    print('[ERRO] Dados inválidos.')

"""

# Professor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'Maior valor {maior}')
print(f'Menor valor {menor}')















