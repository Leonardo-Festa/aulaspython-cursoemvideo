s = float(input('Digite o sálario do funcionário R$'))
if s >= 1250.00:
    a = s + (s * 10/100)
  
else:
    a = s + (s *15/100)
    
    
print('Seu novo sálario é de \033[4;36mR${:.2f}\033[m'.format(a))