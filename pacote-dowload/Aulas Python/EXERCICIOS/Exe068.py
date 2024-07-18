from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR?')
v = 0
while True:
    compnum = randint(0,10)
    jognum = int(input('Escolha um número: '))
    jogarim = str(input('Par ou Impar? ')).strip().upper()[0]
    soma = compnum + jognum
    print(f'O computador jogou {compnum}')
    print(f'A soma deu {soma} ')
    print(f'Deu PAR' if soma % 2 == 0 else 'DEU IMPAR')
    
    if jogarim == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu.')
            break

    elif jogarim == 'I':
        if soma % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu.')
            break
print(f'O jogo acabou, você venceu {v} vezes.')
