v = float(input('Qual a velocidade marcada: '))
if v > 80:
    print('Você ultrapassou o limite da velocidade na via!')
    tm = (v - 80) * 7
    print('O valor da multa a pagar é de R${:.2f}'.format(tm))
else:
    print('Você está andando na velocidade permitida, continue assim.')
