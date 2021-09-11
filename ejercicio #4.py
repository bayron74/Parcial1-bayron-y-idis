#Hacer un programa en Python para determinar el aumento de un  trabajador,
#se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del  5%,
#si generaba menos de $2000 su aumento será de un 10%.

salario = float(input("Ingresa su salario actual"))

if salario >= 2000:
    aumento = salario * 0.05
    incre = salario + aumento
    print("Su aumento del 5% es de:", aumento)
    print("SU total con aumento es:", incre)
    
elif salario <= 1999:
    aumento = salario * 0.10
    incre = salario + aumento
    print("Su aumento del 10% es de:", aumento)
    print("Su nuevo salario es de:", incre)
    
