preço = float(input('Valor do produto: R$'))
opção = int(input('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é sua opção: '''))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    parcela = int(input('Quantas parcelas: '))
    valpar = total / parcela
    print('Sua compra será parcelada em {}x de {:.2f}'.format(parcela,valpar))
else:
    total = 0
    print('ERRO, OPÇÃO DE PAGAMENTO INVÁLIDA, TENTE NOVAMENTE')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))
    