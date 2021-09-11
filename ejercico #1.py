#Tiendas Don Pepe desea un programa para ingresar por teclado el monto de  compra
#y el día de la semana; si el día es martes o jueves, se realizará un descuento
#del  15% por la compra. Visualizar el descuento y el total a pagar por la compra.  



monto = int(input("Ingrese el monto"))
dias = input("Ingrese el dia de hoy")

if dias ==("martes") or ("jueves"):
    descuento = monto * 0.15
    total = monto - descuento
    print("Su descuento es:", descuento)
    print("El total a pagar es:",total)
    
else:
    print("Su total a pagar es:", monto)
    
