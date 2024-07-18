maior = 0
menor = 0
for c in range(1,3):
    peso = float(input('Digite o {}° peso: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso digitado foi {:.1f}Kg, e o menor peso digitado foi {:.1f}Kg'.format(maior,menor))
