a = int(input('Digite o coeficiente A'))
b = int(input('Digite o coeficiente	B'))
c = int(input('Digite o coeficiente C'))

delta = (b*b) - (4*a*c)
xpositivo = ((b*(-1)) + (delta ** (1/2)))/(2*a)
xnegativo = ((b*(-1)) - (delta ** (1/2)))/(2*a)
print(delta)
if delta < 0 :
	print('Delta = ', b , '² * 4 * ' , a ,' * ' ,c)
	print(delta)
	print("Não há raizes reais")
else :
	print('Delta = ', b , '² * 4 * ' , a ,' * ' ,c)
	print('X´ = -', b , '+ √', delta , '/2*' ,a )
	print('X´´ = -', b , '- √', delta , '/2*' ,a )
	print(xpositivo)
	print(xnegativo)