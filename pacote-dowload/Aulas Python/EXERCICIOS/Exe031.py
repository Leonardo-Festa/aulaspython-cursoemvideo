d = float(input('Digite a distância da viagem em Km: '))
if d <= 200:
    v = d * 0.5
else:
    v = d * 0.45
print('A taxa dessa viagem é de R${:.2f}'.format(v))
