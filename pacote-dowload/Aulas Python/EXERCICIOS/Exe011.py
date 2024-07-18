c = float(input('Qual é o comprimento da sua parede em metros: '))
a = float(input('Qual é a altura de sua parede em metros: '))
area = c * a
print('A área da sua parede é de {:.3f}² Para pintar sua parede, serão necessários {:.2f}L de tinta'.format(area,area/2))
