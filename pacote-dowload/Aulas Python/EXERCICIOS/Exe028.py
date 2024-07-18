from random import randint
from time import sleep
n = randint(1,5)
print('O computador escolheu um número de 1 a 5')
r = int(input('Tente adivinhar qual número ele escolheu: '))
print('PROCESSANDO...')
sleep(2)
if r == n:
    print('Parabéns! Você acertou em cheio.')
else:
    print('Você errou, o número que ele escolheu foi {}'.format(n))
