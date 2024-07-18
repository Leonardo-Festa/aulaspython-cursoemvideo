num = int(input('Digite um número: '))
bcon = int(input('-Digite 1 para conversão binária\n-Digite 2 para conversão octal\n-Digite 3 para conversão hexadecimal\n:'))
bina = bin(num)
octa = oct(num)
hexa = hex(num)

if bcon == 1:
    print('Binário: {}'.format(bina[2:]))
elif bcon == 2:
    print('Octal: {}'.format(octa[2:]))
elif bcon == 3:
    print('Hexadecimal: {}'.format(hexa[2:]))
else:
    print("Tecla inválida")