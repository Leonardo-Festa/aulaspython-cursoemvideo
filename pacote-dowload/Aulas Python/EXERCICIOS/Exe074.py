from random import randint
tupla = (randint(1,9), randint(1,9), randint(1,9),
         randint(1,9),randint(1,9))
print(f'Os números sorteados foram: ',end=' ')
for n in tupla:
    print(f'{n} ', end=' ')

print(f'\nO maior número sorteado foi {max(tupla)}')
print(f'O menor número sorteado foi {min(tupla)}')
