while True:
    print(f'-'*35)
    n = int(input('A tabuada de qual número deseja? '))
    print(f'-'*35)
    c = 1
    if n < 0:
        break
    for c in range (1,11):
        mult = n * c
        print(f'{n} X {c} = {mult}')
        c += 1
print('PROGRAMA TABUADA ENCERRADO')
