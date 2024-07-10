# * Exercício 031
#         Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km pra viagens de até 200km e R$0,45 para viagens mais longas

print('\n{:=^40}'.format(' Desafio 031 '))

sDis = str(input('Qual a distância em km/h: '))

if sDis.isnumeric() and not sDis.isspace():
    dis = int(sDis)
    if dis <= 200:
        pas = dis * 0.5
        print('Valor da passagem R${:.2f}'.format(pas))
    else:
        pas = dis * 0.45
        print('Valor da passagem R${:.2f}'.format(pas))
else:
    print('[ERRO]Dados inválidos')