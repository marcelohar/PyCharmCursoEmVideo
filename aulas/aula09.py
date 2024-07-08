frase = ' Curso em video Python '

print(frase)

print('pulando 2 em 2: ', frase[::2])

print('Qtd de "O": ', frase.upper().count('O'))
    # como no python tudo é objeito, combineis a chamadas de alguns: passei a frase para maiúsculo e mandei procurar em maiusculo.

print('Tamanho: ',len(frase))

print('removendo espaços: ', len(frase.strip()))

print('trocando palavra: ', frase.replace('Python','Android'))

# uma string é imutável. Não posso trocar uma letra dentro da strig: frase[0]= 'j' - dará erro.

# o 'replace' não muda a string, mas gera uma nova!!

print('Curso' in frase) # retorno = true

print(frase.find('Curso')) # retorna a posição onde começa

print(frase.lower().find('video')) # colocque a frase em minúsculo e procure 'vídeo'.

print(frase.split()) # cria uma lista com as palavras da frase

fDividida = frase.split()

print(fDividida[0]) # posição das palavas da lista gerada

print(fDividida[2][3]) # pega a plavras 2 e retire a letra da posição 3








# Dando print em varias linhas ao mesmo tempo, basta usar """ no print

print("""\n\nNessa aula, vamos aprender operações com String no 
Python. As principais operações que vamos aprender são o 
Fatiamento de String, Análise com len(), count(), find(), 
transformações com replace(), upper(), lower(), capitalize(), 
title(), strip(), junção com join().""")