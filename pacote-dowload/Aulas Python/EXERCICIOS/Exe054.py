from datetime import date
maior = 0
menor = 0
anoat = date.today().year
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento da {}° pessoa : '.format(c)))
    if anoat - ano >= 21:
        maior = maior + 1
    elif anoat - ano < 21:
        menor = menor +1
print('Dentre esses, {} já atingiram a maioridade e {} ainda são menores.'.format(maior,menor))