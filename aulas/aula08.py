import math
import emoji


num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))   // com arredondamento para cima

## USANDO EMOJI

print(emoji.emojize('Olá, Munddo :sunglasses:'))
