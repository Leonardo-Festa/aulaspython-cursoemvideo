from time import sleep
n1 = int(input('Digite o PRIMEIRO  valor: '))
n2 = int(input('Digite o SEGUNDO valor: '))
op = 0
maior = n1

while op != 5:
    print('----------MENU DE OPÇÕES----------')
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR 
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    op = int(input('Digite sua opção: '))
    if op == 1:
        sleep(1)
        print('Somando {} + {} = {}'.format(n1,n2,n1+n2))
    elif op == 2:
        sleep(1)
        print('Multiplicando {} X {} = {}'.format(n1,n2,n1*n2))
    elif op == 3:
        sleep(1)
        if n2 > n1:
         maior = n2
        print('O maior valor digitado foi {}'.format(maior))
    elif op == 4:
       n1 = int(input('Digite o PRIMEIRO valor: '))
       n2 = int(input('Digite o SEGUNDO valor: '))
    elif op == 5:
       print('Finalizando')
    else:
       print('Opção inválida, tente novamente.')
sleep(2)
print('Encerrando programa...')