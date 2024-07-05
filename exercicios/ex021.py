#  Exercício 021
#             Faça um programa em python que abra e reproduza o áudio de um arquivo mp3

import pygame
import time

pygame.init()

pygame.mixer.music.load('somEx021.mp3')
pygame.mixer.music.play()
# pygame.event.wait()                   # só funcionou com o 'while'

while pygame.mixer.music.get_busy():
    time.sleep(1)
    '''
    time.sleep(1): Dentro do loop, estamos pausando a execução por 1 segundo a cada iteração. Isso evita que o programa consuma muitos recursos enquanto espera.
    '''
print("executado!")


"""
# Marcelo
from playsound import playsound

import os


print('\n {:=^40} \n'.format(' Desafio 021 '))

print('Executando som!')

playsound(r'C:\\Users\\marcelo.rangel\\Documents\\Projetos\\PyCharmCursoEmVideo\\som\\msc1.mp3')

print('Som executado com sucesso!')


"""
''' tive que instalar o módulo para executar o som .mp3
    - cliquei no 'python console' e coloquei o seguinte comando: pip install playsound==1.2.2 (versão que funcionou)
    - Após instalar, tive que importar: from playsound import playsound
    - chamei a função e passei o caminho de onde está o arquivo + o nome do arquivo .mp3
        obs: para funcionar temos que usar \\ ou r (caracteres de escape) no endereço da caminho:
        r - antes do caminho. ex: r'.....'
        \\ - se não usar o 'r'
        
    - Podemo usar como alternativa a bibliotecas 'pygame'.
    
'''

