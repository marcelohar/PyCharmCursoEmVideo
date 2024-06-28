#  * Exercício 019
#             Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
#              Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random

print('\n {:=^40} \n'.format(' Desafio 019 '))


nomes = []
for i in range(4):
    nome = input('{}º Aluno: '.format(i+1))
    nomes.append(nome)

r = random.choice(nomes)
print('Selecionado {}!'.format(r))


