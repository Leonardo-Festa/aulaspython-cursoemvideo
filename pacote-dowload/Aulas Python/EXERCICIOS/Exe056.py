velho = 0
nova = 0
idadetotal = 0
media = 0
for c in range(1,5):
    print('-'*11,'{}ª PESSOA'.format(c),'-'*11)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    idadetotal = idadetotal + idade
    if sexo in 'Mm':
        if c == 1:
            velho = idade
            maisve = nome
        else:
            if idade > velho:
                velho = idade
                maisve = nome
                idadevelho = idade
    else:
        if idade < 20:
            nova = nova + 1

media = idadetotal / 4
print('A média de idade desse grupo é de {} anos'.format(media))
print('O homem mais velho desse grupo é o {} que tem {} anos'.format(maisve,idadevelho))
print('Nesse grupo tem {} mulheres que possuem menos de 20 anos.'.format(nova))
