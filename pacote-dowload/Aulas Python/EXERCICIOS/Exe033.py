n1 = int(input('Digite o 1° número:'))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número digitado foi \033[1;31m{}\033[m'.format(menor))
print('O maior número digitado foi \033[1;34m{}'.format(maior))    

    