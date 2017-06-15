#TIPO DESCRIÇÃO RENDIMENTO MENSAL
#1 Poupança 10%
#2 Fundo de renda fixa 15
%
tipo = int(input("""Digite o tipo de operação
1. Poupança.
2. Fundo de renda fixa."""))


if(tipo == 1):
	valor = float(input('Agora digite o valor a ser depositado'))
	valor = valor + (valor * 0.1)
	print('O valor corrigido será: ', valor)
elif(tipo == 2):
	valor = float(input('Agora digite o valor a ser depositado'))
	valor = valor + (valor * 0.15)
	print('O valor corrigido será: ', valor)
else:
	print('Operação inválida, fim do programa')

