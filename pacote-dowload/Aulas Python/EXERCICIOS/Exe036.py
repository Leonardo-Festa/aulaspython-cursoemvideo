print('-='*20)
print(' '*7,'ANALISADOR DE EMPRÉSTIMO')
print('-='*20)
vc = float(input('Valor do imóvel: R$'))
sc = float(input('Salário do comprador: R$'))
a = int(input('Em quantos anos vai ser feito o pagamento: '))
par = vc / (a * 12)

if par <= sc * (30/100):
    print('\033[1;32m*EMPRÉSTIMO APROVADO!*\033[m\n Valor da parcela mensal: R${:.2f}'.format(par))
else:
    print('\033[1;31m*EMPRÉSTIMO NEGADO*\033[m')