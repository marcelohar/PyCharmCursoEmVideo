# Como publicar como um modulo no site do python.org?

# Calculando lados de um triangulo retangulo
import math

print('\n {:=^40} \n'. format(' Achando os lados '))

print('Informe os dados disponíveis.')

h = input("Hipotenusa: ")

if h == "" or h == "0" :
    ca = int(input('Cateto adjacente: '))
    co = int(input('Cateto oposto: '))
    soma = (ca**2) + (co**2)
    h = int(math.isqrt(soma))

    print('Valor da hipotenusa: {:.0f}'.format(h))

elif h.isnumeric() and h != 0:
    c = int(input('Informe o cateto: '))
    h = int(h)

    # tenho que tratar o erro se a hipotenusa for maior que um dos catetos

    sub = (h**2) - (c**2)
    cr = math.sqrt(sub)

    print('Valor do cateto que falta: {:.0f}'.format(cr))

else:
    print('[ERRO] Somente números!')