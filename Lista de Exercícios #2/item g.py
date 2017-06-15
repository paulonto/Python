#CATEGORIA IDADE
#Infantil 5 a 7
#Infanto-Juvenil 8 a 10
#Juvenil 11 a 15
#Adulto 16 a 30
#Master Acima de 30

idade = int(input('Digite sua idade'))

if (idade < 5 ):
	categoria = 0;
elif(idade >= 5) and (idade <= 7 ):
	categoria = 'Infantil'
elif(idade >= 8) and (idade <= 10 ):
	categoria = 'Infanto-Juvenil'
elif(idade >= 11) and (idade <= 15 ):
	categoria = 'Juvenil'
elif(idade >= 16) and (idade <= 30 ):
	categoria = 'Adulto'
else:
	categoria = 'Master'

if(categoria == 0):
	print('Disponível apenas para nadadores com idade superior a 4 anos.')
else:
	print('Sua categoria é:',categoria)
