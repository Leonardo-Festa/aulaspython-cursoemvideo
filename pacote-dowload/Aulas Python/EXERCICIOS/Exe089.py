lista = []
média = []

while True:
    nome = str(input('NOME: '))
    nota1 = float(input('PRIMEIRA NOTA:'))
    nota2 = float(input('SEGUNDA NOTA:'))
    lista.append(nome[:], nota1[:], nota2[:])

    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

for c in len(lista):
    aux = lista[1] + lista[2] / 2
    média.append(aux[:])
    
print('-='*20)
print('BOLETIM ESCOLAR')


while True:
    resp2 = str(input('Digite 999 para encerrar.'))
    if resp2 == 999:
        break
