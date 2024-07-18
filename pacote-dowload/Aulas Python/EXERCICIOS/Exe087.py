matriz = [[0, 0, 0] , [0, 0, 0] , [0, 0, 0]]
par = somacol = maior = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite o valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            somacol += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        if l == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]


for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print(f'A soma dos valores pares digitados é: {par}')
print(f'A soma dos valores da terceira coluna é: {somacol}')
print(f'O maior valor digitado na segunda coluna foi: {maior}')
