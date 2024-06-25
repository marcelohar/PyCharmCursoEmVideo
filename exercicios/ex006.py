#   Exercício 006
#       Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('{:=^40}'.format(' Desafio 006 '))

num = int(input('Digite um número: '))

print('O dobro de {} é {}. \n'
      'O triplo de {} é {}. \n'
      'A Raiz quadrada de {} é {:.2f}.'. format(num, (num*2), num, (num*3), num, (num**0.5)))    # Lembrando que se elevarmos qualquer número a
                                                                                                      # '0,5' ou a '1/2', teremos a raiz quadrada desse número
