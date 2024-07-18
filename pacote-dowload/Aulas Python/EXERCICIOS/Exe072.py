valor = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO',
         'SEIS','SETE','OITO','NOVE','DEZ','ONZE',
         'DOZE','TREZE','CATORZE','QUINZE',
        'DEZESSEIS','DEZESETE', 'DEZOITO','DEZENOVE','VINTE')
while True:
    while True:
        tecla = int(input('Digite um número entre 0 e 20: '))
        if 0 <= tecla <= 20:
            break
    print(f'Você digitou o número {valor[tecla]}')
    op = str(input('Quer continuar? ')).strip().upper()[0]
    if op not in 'S':
        break
print(f'Fim do programa.')

