t = int(input('Qual é o valor do primeiro termo?: '))
r = int(input('Qual é a razão?: '))
s = t + r
c = 1
print('{} -> '.format(t), end='')
while c < 10:
    print('{} -> '.format(s), end='')
    s = s + r  
    c = c + 1
print('FIM')