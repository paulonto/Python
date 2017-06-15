altura = float(input('Digite  a sua altura'))
sexo = str(input('Digite o seu sexo'))
sexo = sexo[:1]

if(sexo == "m") or (sexo == "M"):
	peso_ideal = ((72.7 * altura) - 58)
elif(sexo == "f") or (sexo == "F"):
	peso_ideal = ((62.1 * altura) - (44.7))
elif (sexo != "m") and (sexo != "M") and (sexo != "m") and (sexo != "m"):
	print('Sexo Inválido')
print('O seu peso ideal é:' ,peso_ideal)