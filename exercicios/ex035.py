# * Exercício 035
#         Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo retangulo.

print('\n{:=^40}'.format(' Desafio 035 '))

print('Informe 3 retas')
sR1 = str(input('1º Reta: ')).strip()       # .strip, além de remover os espços, facilita na hora de verificar se está vazio
sR2 = str(input('2º Reta: ')).strip()
sR3 = str(input('3º Reta: ')).strip()

if sR1.isnumeric() and sR2.isnumeric() and sR3.isnumeric():
    r1 = int(sR1)
    r2 = int(sR2)
    r3 = int(sR3)

    maior = r1
    if r2 > maior:
        maior = r2

    if r3 > maior:
        maior = r3

#    if maior**2 ==  como vou saber quais dos r é os outros dois menores. Se por acaso o r2 for maior como vou saber que r3 e r1 sao os menosres/


    # maior = hip, qual é maior?


    # h^2 = c1^2 + c2^2

else:
    print('[ERRO] Dados inválidos.')