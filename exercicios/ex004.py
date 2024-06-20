print('====== Desafio 4 ======')

dados = input('Digite alguma coisa: ')

print('Tipo de dado digitado: {}'.format(type(dados)))

print('Só tem espaços: ', dados.isspace())
print('Pode ser um  numero? {}'.format(dados.isnumeric()))
print('Pode ser um  alfabetico?', dados.isalpha())
print('Pode ser um  alfanumerio? {}'.format(dados.isalnum()))
print('Está em maiúscula? ', dados.isupper())
print('Está em minúscula? {}'.format(dados.islower()))
print('Está com maiúscula e minúscula "capitalizada"', dados.istitle())
