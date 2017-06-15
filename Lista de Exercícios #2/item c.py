#Acima de R$ 400,00 30% do saldo médio
#Entre R$ 400,00 – R$ 300,00 25% do saldo médio
#Entre R$ 300,00 – R$ 200,00 20% do saldo médio
#Até R$ 200,00 10% do saldo médio#

saldo = int(input('Digite seu saldo médio para atualização de crédito'))

if saldo <= 200:
	credito = saldo + saldo * 0.1
	print('Seu novo crédito é:', credito)
elif (saldo > 200) and (saldo < 300):
	credito = saldo + saldo * 0.2
	print('Seu novo crédito é ', credito)
elif (saldo > 300) and (saldo < 400):
	credito = saldo + saldo * 0.25
	print('Seu novo crédito é ', credito)
else:
	credito = saldo + saldo * 0.3
	print('Seu novo crédito é ', credito)
