# * Exercício 029
#         Escreva um programa que leia  a velocidade de um carro. Se ele utrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#         A multa vai custar R$ 7,00 por cada km acima do limite.


# Eu...
"""
print('\n{:=^40}'.format(' Desafio 029 '))

dado = str(input('Qual a velocidade do carro em km/h: ')).strip()
lim = 80

if dado.isnumeric() and not dado.isspace():
    km = int(dado)
    if km > lim:
        d = km - lim
        multa = float(d * 7)
        print('Você foi multado em R${:.2f}, por estar a cima de 80km/h'.format(multa))
else:
    print('[ERRO] Dados inválidos!')

"""

# Professor...

from colorama import Fore                              # precisa baixar a biblioteca 'pip install colorama


velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(Fore.RED + 'Voce foi multado em R${:.2f}'.format(multa) + Fore.RESET)      #fore = frete?

print( 'Tenha um bom dia! Dirija com segurança!')

