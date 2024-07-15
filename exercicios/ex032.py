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

# Professor
from datetime import date                                                   # Trabalhar somente com datas


ano = int(input("Que ano quer analisar? Coloque 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year                                         # pega a data do dia atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:           # se o resto da divisão do ano por 4 = 0 'e' o resto da divisão do ano por 100 for diferente ou o resto da divisão do ano por 400 == 0 . só se ocorrer tudo isso..

    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

































