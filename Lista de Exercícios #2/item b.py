salario = float(input('Digite o seu salário'))

if salario < 900:
	salario = salario + salario * 0.3
	print('Seu salário será:', salario)
else: 
	print('Seu salário é maior ou igual a 900. Não haverá reajuste.')
