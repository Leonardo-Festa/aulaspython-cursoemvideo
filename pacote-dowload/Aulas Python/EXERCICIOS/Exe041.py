from datetime import date
ano = int(input('Em que ano você nasceu? 19'))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade == 25:
    print('GATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')
    
