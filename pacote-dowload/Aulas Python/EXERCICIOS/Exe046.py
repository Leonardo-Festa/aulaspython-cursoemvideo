import emoji
from time import sleep
print('Vamos começar a contagem regressiva!!!')
for c in range(10,0,-1):
    sleep(1)
    print(c)
sleep(1)
print(emoji.emojize(':sparkler:'*10))