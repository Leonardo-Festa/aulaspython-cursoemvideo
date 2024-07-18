tot = 0
mil = 0
produto = 0
while True:
    nome = str(input('PRODUTO: '))
    preço = float(input('PREÇO: R$'))
    tot += preço
    produto += 1

    if produto == 1:
        maisb = preço
        barato = nome

    if preço > 1000:
        mil += 1
    
    if preço < maisb:
        maisb = preço
        barato = nome

    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
print('-='*25)    
print(f'QUANTIDADE DE PRODUTOS: {produto}')
print(f'PRODUTOS COM VALOR MAIOR QUE R$1000,00: {mil}')
print(f'PRODUTO MAIS BARATO: {barato} ({maisb})')
print(f'VALOR TOTAL DA NOTA: {tot:.2f}')
