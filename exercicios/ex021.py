# * Exercício 021
#             Faça um programa em python que abra e reproduza o áudio de um arquivo mp3
from playsound import playsound


print('\n {:=^40} \n'.format(' Desafio 021 '))

print('Executando som!')

playsound(r'C:\Users\marcelo.rangel\Downloads\excluir\door-43633.mp3')

print('Som executado com sucesso!')


''' tive que instalar o módulo para executar o som .mp3
    - cliquei no 'python console' e coloquei o seguinte comando: pip install playsound==1.2.2 (versão que funcionou)
    - Após instalar, tive que importar: from playsound import playsound
    - chamei a função e passei o caminho de onde está o arquivo + o nome do arquivo .mp3
        obs: para funcionar temos que usar \\ ou r (caracteres de escape) no endereço da caminho:
        r - andes do caminho. ex: r'.....'
        \\ - se não usar o 'r'
        
    - Podemo usar como alternativa a bibliotecas 'pygame'.
    
'''

