n = int(input('Digite um número para ver sua tabuada: '))
for c in range(0,11):
    r = n * c
    print('{} X {} = {} '.format(n,c,r))
    