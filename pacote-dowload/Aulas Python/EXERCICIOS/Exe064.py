c = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    soma = soma + n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} vezes e a soma entre eles foi {}.'.format(c - 1,soma - 999))
