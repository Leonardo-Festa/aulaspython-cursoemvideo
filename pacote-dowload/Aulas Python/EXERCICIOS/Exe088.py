from random import sample
palpite = []
aux = []
jogos = int(input('Olá! Quantos jogos você deseja fazer?: '))

for c in range(jogos):
    aux = sample(range(1,60), 6)
    palpite.append(aux[:])
    aux.clear()
for c in range(jogos):
    print(f'Palpite para o {c+1}º jogo: {sorted(palpite[c])}')
