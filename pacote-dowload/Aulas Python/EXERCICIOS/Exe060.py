n = int(input('Digite um número para calcular se fatorial: '))
v = n
f = 1
print('Calculando {}! = '.format(n), end='')
while v > 0:
    print('{}'.format(v), end='')
    print(' X ' if v > 1 else ' = ',end='')
    f = f * v
    v = v - 1   
print(f)   

