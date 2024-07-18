d = int(input('Dias alugados:'))
km = float(input('Km rodados:'))
p = d * 60 + km * 0.15
print('Total a pagar:R${:.2f}'.format(p))
