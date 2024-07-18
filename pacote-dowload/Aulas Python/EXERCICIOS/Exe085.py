lista = [[] , []]
núm = 0

for v in range(1,8):
    núm = int(input(f'Digite o {v}° valor: '))
    if núm % 2 == 0:
        lista[0].append(núm)
    else:
        lista[1].append(núm)
    

lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
