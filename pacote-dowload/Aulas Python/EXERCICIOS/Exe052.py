r = 0
n = int(input('Digite um número: '))
for c in range(1,n+1):
    if n % c == 0:
        r = r + 1
if r == 2:
    print('ESSE É UM NÚMERO PRIMO')
else:
    print('ESSE NÃO É UM NÚMERO PRIMO')
