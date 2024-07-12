# * Exercício 032
#         Faça um programa que leia um ano qualquer e mostre se ele é bissexto - *** estudar o que é ano bissexto.


# Eu... não consegui fazer

'''
print('\n{:=^40}'.format(' Desafio 32 '))

sAno = str(input('Informe o ano "XXXX": '))

if sAno.isnumeric() and not sAno.isspace():

    ano = int(sAno)
    print(ano)
    if ano % 4 == 0:
        print(ano)
        if ano % 100 != 0:
            print(ano)
            if ano % 400 == 0:
                print('O ano {} é bixesto!'.format(ano))

else:
    print('[ERRO] Dados inválidos!')

'''


