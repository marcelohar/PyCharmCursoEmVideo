# Converter graus Celsius para Fahrenheit
# 1 Multiplique a temperatura em graus Celsius por 9/5.
# 2 Adicione 32 ao resultado.


print('{:=^40} \n'.format(' Desafio 014 '))

temp = float(input('Informe a temperatura em ºC: '))
conv = (temp * 1.8) + 32                                                    # 9/5 = 1.8
print('A temperatura de {}ºC equivale a {}ºF.'.format(temp, conv))

