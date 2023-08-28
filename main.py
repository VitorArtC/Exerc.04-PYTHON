
n = int(input('Digite um Numero: '))

print('-=' * 15)
print('''[1] Para Binario
[2] Para Octal
[3] Para Hexadacimal''')
print('-=' * 15)

es = int(input('Escolha entre 1 ,2 ,3: '))
print('-=' * 15)

if es == 1:
    print('O valor binario: {}'.format(bin(n)[2:]))
elif es == 2:
    print('O valor Octal: {}'.format(oct(n)[2:]))
elif es == 3:
    print('O valor Hexadacimal: {}'.format(hex(n)[2:]))

else:
    print('ERRO!! Digite um numero entre 1 e 3')
