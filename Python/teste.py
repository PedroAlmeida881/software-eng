print('Ola, aluno da escfolqa estadual, aqui voce podera fazer a media de suas notas de suas 5 provas. Mas antes, faca o que se pede logo abixo')
nome=input('Digite seu nome:')
idade=int(input('Digite sua idade:'))
print('Bem vindo(a)',nome,',voce tem',idade,'anos e vai ver suas notas, espero que se der bem em!')

Nota_1 = float(input('Digite sua primeira nota: '))
Nota_2 = float(input('Digite sua segunda nota: '))
Nota_3 = float(input('Digite sua terceira nota: '))
Nota_4 = float(input('Digite sua quarta nota: '))
Nota_5= float(input('Digite sua quinta nota: '))

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4 + Nota_5) / 5    
print('A média das notas é: ', media)

Resultado = 'Aprovado' if media >= 6 else 'Reprovado'
print('O aluno', nome, 'foi', Resultado)