print('====== Desafio 4 ======')

dados = input('Digite alguma coisa: ')

print('Tipo de dado digitado: {}'.format(type(dados)))

print('Pode ser um  inteiro? {}'.format(dados.isnumeric()))
print('Pode ser um  alfabetico? {}'.format(dados.isalpha()))
print('Pode ser um  alfanumerio? {}'.format(dados.isalnum()))

