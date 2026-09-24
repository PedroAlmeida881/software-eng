idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você é menor de idade.')
elif  idade >= 18 and idade < 65:
    print('Você é adulto.')
else: 
    print('Você é idoso.')
    idade = int(input('Digite sua idade: '))
if idade < 12:
    print('Você pode vber apenas filme infantil')
elif idade >= 12 and idade < 18:
    print('Você pode ver filme infantil e filme adolescente')
elif idade >= 18 and idade < 65:
    print('Você pode ver filme infantil, filme adolescente e filme adulto')


