lista = ('Café', 18.90,
         'Bolacha', 2.80,
         'Leite', 7.50,
         'Pão', 1,
         'Coxinha', 6,
         'Suco',8.5,)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for c in range(0,len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end=' ')
    else:
        print(f'R$ {lista[c]:>5.2f}')
print('-' * 40)

    
 
