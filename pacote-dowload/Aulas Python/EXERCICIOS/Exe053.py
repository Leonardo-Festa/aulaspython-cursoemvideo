f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
juntos = ''.join(palavras)
inverso = ''
for c in range(len(juntos) - 1, -1, -1):
    inverso =+ inverso + juntos[c]
if inverso == juntos:
    print('Temos um Palíndromo')
else:
    print('Não é Palíndromo')
    