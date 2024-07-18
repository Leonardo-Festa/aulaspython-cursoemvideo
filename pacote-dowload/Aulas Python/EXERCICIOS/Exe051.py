t = int(input('Qual o valor do primeiro termo: '))
r = int(input('Qual a razão: '))
dec = t + (10-1) * r
for c in range(t,dec + r,r):
    print('{} -> '.format(c),end='')
print('ACABOU')
