# * Exercício 029
#         Escreva um programa que leia  a velocidade de um carro. Se ele utrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#         A multa vai custar R$ 7,00 por cada km acima do limite.

print('\n{:=^40}'.format(' Desafio 029 '))

dado = str(input('Qual a velocidade do carro em km/h: ')).strip()
lim = 80

if dado.isnumeric() and not dado.isspace():
    km = int(dado)
    if km > lim:
        d = km - lim
        multa = float(d * 7)
        print('Você foi multado em R${:.2f} por estar a cima de 80km/h'.format(multa))
else:
    print('[ERRO] Dados inválidos!')
