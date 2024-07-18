palavra = ('CACHORRO','GATO','PAPAGAIO','COBRA','PEIXE')
for c in palavra:
    print(f'\nNa palavra {c} existem',end=' ')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')