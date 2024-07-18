n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
m = (n1 + n2) / 2

if m < 5:
    print('Sua média foi {} - \033[1;31mREPROVADO\033[m'.format(m))
elif m >= 5 and m < 7:
    print('Sua média foi {} - \033[1;33mRECUPERAÇÃO\033[m'.format(m))
elif m > 7:
    print('Sua média foi {} - \033[1;32mAPROVADO\033[m'.format(m))
