v = float(input('Digite o preço do produto: R$'))
d = v * 15/100
print('O preço com desconto de 15%: R${:.2f}, você está economizando R${:.2f}'.format(v - d,d))

