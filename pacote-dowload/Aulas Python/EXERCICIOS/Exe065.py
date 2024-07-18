n = int(input('Digite um número: '))
resp = str(input('Quer continuar? [S/N] ')).strip().upper()
soma = n
maior = n
menor = n
cont = 1
while resp == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()  
média = soma / cont
print('Foram digitados {} números'.format(cont))
print('A média entre esses valores foi de {}'.format(média))
print('O MAIOR número digitado foi {} e o MENOR foi {}'.format(maior,menor))
