# * Exercício 035
#         Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo retangulo.

# Consegui com número inteiro, mas ao mudar para float deu erro. então não consegui

"""
def isFloat(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


print('\n{:=^40}'.format(' Desafio 035 '))

print('Informe 3 retas')
sR1 = str(input('1º Reta: ')).strip()       # .strip, além de remover os espços, facilita na hora de verificar se está vazio
sR2 = str(input('2º Reta: ')).strip()
sR3 = str(input('3º Reta: ')).strip()

if isFloat(sR1) and isFloat(sR2) and isFloat(sR3):
    r1 = float(sR1)
    r2 = float(sR2)
    r3 = float(sR3)

    maior = r1


    if r3 > maior:                                              # Lembrando que a sequência 3,2,1 faz diferença
        maior = r3
        if r3**2 == r2**2 + r1**2:
            print('3 As Retas formam um triângulo retângulo!')
        else:
            print('3 As retas NÃO formam um triângulo!')

    if r2 > maior:
        maior = r2

        if r2 ** 2 == r1 ** 2 + r3 ** 2:
            print('2 As Retas formam um triângulo retângulo!')
        else:
            print('2 As retas NÃO formam um triângulo!')

    if r1 == maior:
        if r1**2 == r2**2 + r3**2:
            print('1 As Retas formam um triângulo retângulo!')
        else:
            print('1 As retas NÃO formam um triângulo!')

else:
    print('[ERRO] Dados inválidos.')

"""

# Professor

print('-='*20)
print('Analisador de triângulo')
print('-='*20)

r1 = float(input('Primeiro segimento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('O segimentos acima NÃO PODE FORMAR triângulo!')





