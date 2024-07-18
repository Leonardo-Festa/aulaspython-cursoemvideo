num = []
maior = 0
menor = 0
for v in range(0,5):
    num.append(int(input('Digite um número: ')))
    if v == 0:
        maior = num[v]
        menor = num[v]
    else:
        if num[v] > maior:
            maior = num[v]
        if num[v] < menor:
            menor = num[v]
print(f'O maior número dessa lista é o {maior} e ele está na posições...',end=' ')
for i,v in enumerate(num):
    if v == maior:
        print(f'{i} ...',end=' ')
print()
print(f'O menor número dessa lista é o {menor} e ele está nas posições...',end=' ')
for i,v in enumerate(num):
    if v == menor:
        print(f'{i} ...',end=' ')
print()
print(num)
