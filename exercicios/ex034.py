# * Exercício 034
#         Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#         para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

print('\n{:=^40}'.format(' Desafio 034 '))


# Criei uma funcao para ver se é possivel converter para float
def is_float(v):
    try:                    # tente
        float(v)            # converter para float
        return True         # se não der erro, retornar true
    except ValueError:      # Deu erro, pois não conseguiu converter
        return False        # retorne False

sSal = str(input('Qual o valor do salário (use (.) para separar) R$: ')).strip()

if is_float(sSal) and not sSal.isspace():
    sal = float(sSal)
    if sal > 1.250:
        sal = sal + (sal * 0.10)
    else:
        sal = sal + (sal * 0.15)
    print('Salário corrigindo R${}'.format(sal))
else:
    print('[ERRO] Dados inválidos.')