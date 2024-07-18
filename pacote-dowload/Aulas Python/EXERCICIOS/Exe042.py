print('=-=' * 20)
print(' ' * 16 , 'ANÁLISADOR DE TRIANGULOS 2.0')
print('=-=' * 20)

s1 = float(input('Digite o 1° segmento: '))
s2 = float(input('Digite o 2° segmento: '))
s3 = float(input('Digite o 3° segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima \033[1;32mPODEM\033[m formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES') 
else:
    print('Os segmentos acima \033[1;31mNÂO PODEM\033[m formar um triângulo')
    