# * Exercício 033
#         Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('\n{:=^40}'.format(' Desafio 033 '))

print('Informe 3 número')
sN1 = str(input('1º Nº: '))
sN2 = str(input('2º Nº: '))
sN3 = str(input('3º Nº: '))

if sN1.isnumeric() and sN2.isnumeric() and sN3 and not sN1.isspace() and not sN2.isspace() and not sN3.isspace():
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