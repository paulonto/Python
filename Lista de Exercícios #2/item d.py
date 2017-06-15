#Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com
#as tabelas a seguir, o novo preço e a classificação.
#TABELA 1 – PERCENTUAL DE AUMENTO
#PREÇO %
#Até R$ 50,00 5
#Entre R$ 50,00 e R$ 100,00 (Inclusive) 10
#Acima de R$ 100,00 15
#TABELA 2 - CLASSIFICAÇÕES
#NOVO PREÇO CLASSIFICAÇÃO
#Até 80,00 D
#Entre R$ 80,00 e R$ 120,00 (Inclusive) C
#Entre R$ 120,00 e R$ 200,00 (Inclusive) B
#Maior que R$ 200,00 A


preco = float(input('Digite o preço'))
if preco <= 50:
	preco = preco + (preco * 0.05)
elif (preco > 50) and (preco <= 100):
	preco = preco + (preco *0.1)
else:
	preco = preco + (preco *0.15)
if preco <= 80:
	clas = 'D'
elif (preco > 80) and (preco <= 120):
	clas = 'C'
elif (preco > 120) and (preco <=200):
	clas = 'B'
else:
	clas = 'A'


print('Produto custa: ', preco, '. E sua classificação é: ', clas)