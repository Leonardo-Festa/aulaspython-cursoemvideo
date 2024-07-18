from random import randint
from time import sleep

print('O computador irá pensar num número de 1 a 10 ...')
sleep(1)
computador = randint(1,10)
v = 0
acertou = False

while not acertou:
    jogador = int(input('Tente adivinhar o número que o computador escolheu: '))
    v += 1
    if jogador == computador:
        acertou = True
    else: 
        if jogador < computador:
            print('Mais... tente de novo.')
        elif jogador > computador:
            print('Menos... tente de novo.')
print('Parabéns, você acertou!!! Você precisou de {} tentativas para acertar.'.format(v))
