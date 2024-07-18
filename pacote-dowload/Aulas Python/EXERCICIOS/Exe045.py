from random import choice
from time import sleep
print('Vamos jogar Jokenpô')
p = str('Pedra')
pp = str('Papel')
t = str('Tesoura')
lista = [p,pp,t]
comput = choice(lista)
jogador = str(input('Sua escolha: '))
print('JO')
sleep (1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O computador jogou {}'.format(comput))

if comput == 'Pedra' and jogador == 'Pedra':
    print('Xiii, deu empate!')
elif comput == 'Pedra' and jogador == 'Papel':
    print('Parabéns, você me derrotou!')
elif comput == 'Pedra' and jogador == 'Tesoura':
    print('HAHAHA EU GANHEI!!!')
elif comput == 'Papel' and jogador == 'Pedra':
    print('HAHAHA EU GANHEI!!!')
elif comput == 'Papel' and jogador == 'Papel':
     print('Xiii, deu empate!')
elif comput == 'Papel' and jogador == 'Tesoura':
    print('Parabéns, você me derrotou!')
elif comput == 'Tesoura' and jogador == 'Pedra':
   print('Parabéns, você me derrotou!')
elif comput == 'Tesoura' and jogador == 'Papel':
     print('HAHAHA EU GANHEI!!!')
elif comput == 'Tesoura' and jogador == 'Tesoura':
    print('Xiii, deu empate!') 
else:
    print('Opção inválida, tente novamente.')


