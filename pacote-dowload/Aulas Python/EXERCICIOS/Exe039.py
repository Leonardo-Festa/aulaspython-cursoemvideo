from datetime import date
nasc = int(input('Em que ano você nasceu? '))
sexo = str(input('Você é do sexo MASCULINO ou FEMININO '))
anoat = date.today().year
idade = anoat - nasc




if idade < 18 and sexo == 'M':
    saldo = 18 - idade
    print('Você deverá se alistar daqui {} anos'.format(saldo))
    ano = anoat + saldo
    print('O ano do seu alistamento será {}'.format(ano))
elif idade == 18 and sexo == 'M':
    print('Você deve se alistar ainda esse ano!')
elif idade > 18 and sexo == 'M':
    saldo = idade - 18
    print('Já se passou {} anos de seu alistamento'. format(saldo))
    ano = anoat - saldo
    print('O ano de seu alistamento foi {}'.format(ano))
else:
    print('Como você é mulher, não é necessário se alistar')

