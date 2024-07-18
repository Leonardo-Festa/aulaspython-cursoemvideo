cont = 0
s = 0
for c in range(1,7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print('A soma dos {} números pares digitados é de {}'.format(cont,s))