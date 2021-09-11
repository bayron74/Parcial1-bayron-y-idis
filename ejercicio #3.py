#Realizar un programa que simule un inicio de sesión solicitando el nombre
#de usuario=”tunombre” y contraseña=”123”, y mostrar un mensaje en pantalla,
#inicio de  sesión correcto/ nombre de usuario incorrecto.

contra = 1234

print("Crearas una cuenta")
nombre = input("Ingrese su nombre")
contra = int(input("Ingrese una contraseña"))


if contra == 1234:
    print("Inicio de sesion correcto")

else:
    print("inicio de sesion incorrecto")
