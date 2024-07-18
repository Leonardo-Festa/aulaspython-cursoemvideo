from math import hypot
catOP = float(input('Comprimento do cateto oposto:'))
catAD = float(input('Comprimento do cateto adjacente:'))
print('A hipotenusa vai medir {:.2f}'.format(hypot(catOP,catAD)))
