#Hacer un Python para ayudar a un trabajador a saber cuál será su sueldo
#semanal,  se sabe que, si trabaja 40 horas o menos, se le pagará $20 por hora,
#pero si  trabaja más de 40 horas entonces se le pagarán a $25 por hora.  
trabajo=int(input("ingrese sus horas trabajadas "))

if trabajo <=40:
	horas=trabajo *20
	print("supago es de: $",horas)
elif trabajo >=41:
	horas=trabajo *25
	print("su pago es de: $",horas)
