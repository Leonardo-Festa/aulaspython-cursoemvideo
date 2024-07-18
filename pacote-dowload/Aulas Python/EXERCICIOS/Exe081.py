lista = []
totnum = 0
cinco = False
while True:
    lista.append(int(input('Digite um valor: ')))
    totnum += 1
    if 5 in lista:
        cinco = True

    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(f'Você digitou {totnum} números.')
print(f'A lista digitada decrescente foi {sorted(lista,reverse=True)}.')
if cinco == True:
    print('O número 5 está nessa lista.')
else:
    print('O número 5 não foi digitado.')
