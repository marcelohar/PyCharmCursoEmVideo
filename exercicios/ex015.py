#     * Exercício 015
#         Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#         pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('{:=^40} \n'.format(' Desafio 015 '))

dias = int(input('Informe a quantidade de dias: '))
km = float(input('Informe a quantidade de Km percorrido: '))

total = (60 * dias) + (0.15 * km)

print('\nValor das diárias: R$ {:.2f} \n'
      '     Valor dos Km: R$ {:.2f} \n'
      '            Total: R$ {:.2f}'
      .format(60 * dias, 0.15 * km, total ))

