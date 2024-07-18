t = int(input('Qual é o valor do primeiro termo?: '))
r = int(input('Qual é a razão?: '))
s = t + r
c = 1
op = 10
e = 'S'
print('{} -> '.format(t), end='')
while e == 'S':
    while c < op:
       c = c + 1
       print('{} -> '.format(s), end='')
       s = s + r
    print('PAUSA')
    e = str(input('\nQuer continuar a contagem? [S/N] ')).strip().upper()
    if e == 'S':
        op = int(input('Quantos termos mais quer ver?: '))
        c = 0
print('FIM')
