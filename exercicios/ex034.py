# * Exercício 034
#         Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#         para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

# Eu..
"""
print('\n{:=^40}'.format(' Desafio 034 '))


# Criei uma funcao para ver se é possivel converter para float
def is_float(v):
    try:                    # tente
        float(v)            # converter para float
        return True         # se não der erro, retornar true
    except ValueError:      # Deu erro, pois não conseguiu converter
        return False        # retorne False

sSal = str(input('Qual o valor do salário (use (.) para separar) R$: ')).strip()

if is_float(sSal) and not sSal.isspace():       # Nâo preciso verificar espaço, pois usei o .strip() na leitura da variável, certp?
    sal = float(sSal)
    if sal > 1.250:
        sal = sal + (sal * 0.10)
    else:
        sal = sal + (sal * 0.15)
    print('Salário corrigindo R${}'.format(sal))
else:
    print('[ERRO] Dados inválidos.')
"""

# Professor
from colorama import Fore                       # colorama eu quem coloquei!

salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print(f'Quem ganhava ' + Fore.RED + f'R${salario:.2f}, ' + Fore.RESET + ' passa a ganhar' + Fore.GREEN + f' R${novo:.2f} ' + Fore.RESET + ' agora')



