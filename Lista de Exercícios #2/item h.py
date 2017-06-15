#Faça um programa que receba a idade e o peso de uma pessoa. De acordo com a tabela
#a seguir, verifique e mostre em qual grupo de risco essa pessoa se encaixa.
#IDADE              PESO
#                   Até 60  60 <> 90  > 90
#Menores que 20        9       8       7
#De 20 a 50            6       5       4
#Maiores q 50          3       2       1

idade = int(input('Digite sua idade:'))
peso = float(input('Digite seu peso:'))


if (idade < 20) and (peso <=60):
	risco = 9
elif(idade < 20) and (peso > 60) and (peso <= 90):
	risco = 8
elif(idade < 20) and (peso > 90):
	risco = 7
elif(idade >= 20) and (idade <= 50) and (peso <= 60):
	risco = 6
elif(idade >= 20) and (idade <= 50) and (peso >= 60) and (peso <=90):
	risco = 5
elif(idade >= 20) and (idade <= 50) and (peso > 90):
	risco = 4
elif(idade > 50) and (peso <= 60):
	risco = 3
elif(idade > 50) and (peso >= 60) and (peso <= 90):
	risco = 2
elif(idade > 50) and (peso > 90):
	risco = 1
print('Seu nível de risco é:',risco)
