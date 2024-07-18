clas = ('Atl Paranaense','Bahia','Botafogo','Atl MG','Bragantino',
        'Palmeiras','Flamengo','São Paulo','Internacional',
        'Cruzeiro','Grêmio','Fortaleza','Criciúma','Corinthians',
        'Juventude','Fluminense','Vasco','Vitória','Atl. GO','Cuiabá')
print('=-'*20)
print(f'Os 5 primeiros colocados no campeonato são {clas[0:5]}')
print('=-'*20)
print(f'Os 4 ultimos colocados na tabela são {clas[-5:]}')
print('=-'*20)
print(f'Os times em ordem alfabética {sorted(clas)}')
print('=-'*20)
print(f'O Tricolor Paulista está na {clas.index('São Paulo') + 1}ª posição na tabela')
print('=-'*20)
