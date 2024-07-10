# * Exercício 032
#         Faça um programa que leia um ano qualquer e mostre se ele é bissexto - *** estudar o que é ano bissexto.

print('\n{:=^40}'.format(' Desafio 32 '))

sAno = str(input('Informe o ano "XXXX": '))

if sAno.isnumeric() and not sAno.isspace():

    ano = int(sAno)
    if ano % 4 == 0:
        if ano % 100 == 0:
            print('O Ano {} não é bissexto.'.format(ano))

          #  continuar

            if ano % 400 == 0:
                print('O ano {} é bixesto!'.format(ano))

else:
    print('[ERRO] Dados inválidos!')
