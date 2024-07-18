pessoas = []
dados = []

while True:
    dados.append(str(input('NOME: ')))
    dados.append(int(input('PESO: ')))
    pessoas.append(dados[:])
    dados.clear()

    escolha = str(input('Quer continuar? [S/N]? '))
    if escolha in 'Nn':
        break

print(f'Foram cadastradas um total de {len(pessoas)} pessoas.')
print('Dentre essas, as que possuem um peso maior que 100kg são ', end=' ')
for p in pessoas:
        if p[1] > 99:
             print(f'[{p[0]}] ', end=' ')
print()
print('E as que estão abaixo dos 75kg são ', end=' ')
for p in pessoas:
     if p[1] < 75:
          print(f'[{p[0]}]', end =' ')
