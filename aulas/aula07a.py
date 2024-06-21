n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
ex = n1 ** n2

print('A soma é {}, o produto é {}, a divisão é {:.2} '.format(s, m, d), end='')
print('Adivisão interira é {} e a potência é {}'.format(di, ex))


