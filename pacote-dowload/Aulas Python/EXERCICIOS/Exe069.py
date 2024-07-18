maior = 0
mulhermenor = 0
homem = 0
pessoa = 0

while True:
    nome = str(input('NOME: '))
    sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
    idade = int(input('IDADE: '))
    pessoa += 1
    
    if idade > 18:
        maior += 1
    
    if sexo in 'M':
        homem += 1
    
    if sexo in 'F' and idade < 20:
        mulhermenor += 1
    
    op = ' '
    while op not in 'SN':
       op = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if op in 'N':
        break
print(f'Foram cadastradas {pessoa} pessoas, dentre elas {maior} são maiores de idade.')
print(f'Tivemos {homem} homens cadastrados e {mulhermenor} mulheres tem menos de 20 anos')
print('FIM DO PROGRAMA')