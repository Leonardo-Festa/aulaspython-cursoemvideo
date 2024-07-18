lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)


    resp = str(input('Quer continurar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Esses são os valores digitados {lista}')
print()
print(listapar)
print()
print(listaimpar)