nome = str(input('Digite seu nome completo: ')).upper().strip()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'. format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n) - 1]))

