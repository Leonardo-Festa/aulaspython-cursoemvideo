peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso ideal'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f}, você está no peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f}, você está com sobrepeso'.format(imc))
elif imc >=30 and imc < 40:
    print('Seu IMC é de {:.1f}, você está com Obesidade'.format(imc))
else:
    print('Seu IMC é de {:.1f}, você está com Obesidade mórbida'. format(imc))
    