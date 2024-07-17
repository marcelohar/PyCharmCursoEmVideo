
print('\033[:33:40m Olá, mundo! \033[m')

a = 3
b = 5
print(f'Os valores são: \033[1;31;43m{a}\033[m e \033[1;34;43m{b}\033[m !!!')

# ------------------

nome = 'marcelo'

print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;34m', nome, '\033[m'))

# ------------------

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretobranco':'\033[7;30m'}

print('Outra forma de fazer {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))


# ------------------


# Aula 11 – Cores no Terminal
#
#     OBS: AS CORES NÃO SÃO DO PYTHON, SÃO DO PADRÃO ANSI
#     padrão ANSI - COMEÇA COM '\' + CODIGO EX: \033[M
#
#     \ -inicia
#     033 - CODIGO PARA CORES
#     [   - abre
#     cor - colocar código das cores para (style : text : background - SÃO OPCIONAIS
#     m   - fecha
#
#     ex: \033[0:33:44m
#     style =
#         0, = NENHUM (NONE)
#         1, = NEGRITO (BOLD)
#         4, = SUBLINHADO (UNDERLINE)
#         7, = INVERTER (NEGATIVE)
#     text =
#         30 = BRANCO
#         31 = VERMELHO
#         32 = VERDE
#         33 = AMARELO
#         34 = AZUL
#         35 = MAGENTA (ROXO)
#         36 = CIANO
#         37 = CINZA
#
#     background = 44
#         40 = BRANCO
#         41 = VERMELHO
#         42 = VERDE
#         43 = AMARELO
#         44 = AZUL
#         45 = MAGENTA
#         46 = CIANO
#         47 = CINZA



