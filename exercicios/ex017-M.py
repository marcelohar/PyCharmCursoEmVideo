# Como publicar como um modulo no site do python.org?

# Calculando lados de um triangulo retangulo
import math

print('\n {:=^40} \n'. format(' Achando os lados '))

print('Informe os dados disponíveis.')

h = input("Hipotenusa: ")

if h == "" or h == "0":
    ca = float(input('Cateto adjacente: '))
    co = float(input('Cateto oposto: '))
    h = math.hypot(ca, co)
    print('Valor da hipotenusa: {:.2f}'.format(h))

    ''' marcelo 
    soma = int((ca**2) + (co**2))
    h = float(math.isqrt(soma))
    '''


elif h.isnumeric() and h != 0:
    c = float(input('Informe o cateto: '))
    h = float(h)

    # tenho que tratar o erro se a hipotenusa for maior que um dos catetos

    sub = int((h**2) - (c**2))
    cr = float(math.sqrt(sub))

    print('Valor do cateto que falta: {:.2f}'.format(cr))

else:
    print('[ERRO] Somente números!')