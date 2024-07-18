v = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
     int(input('Digite outro valor: ')),int(input('Digite outro valor: ')))
        
print(f'O número 9 apareceu {v.count(9)} vezes.')
if 3 in v:
     print(f'O número 3 foi digitado na {v.index(3)+ 1 }ª posição.')
else:
    print('O número 3 não foi digitado.')
print(f'Os números pares digitados foram ', end=' ')
for c in v:
    if c % 2 == 0:
        print(c, end=' ')