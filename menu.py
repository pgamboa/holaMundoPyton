print("Bien venido al mundo virtual, el menu:\n")

while (True):
    print("""Acciones del menu principal
1.- Saludar
2.- Sumar dos numeros
3.- Salir""")
    respuesta = int(input("Por favor ingrese una opcio: "))
    if respuesta == 1:
        print("Hola amigos desde Debian-Python")
    elif respuesta == 2:
        num_1 = float(input("Ingresa el primer numero: \n"))
        num_2 = float(input("Ingresa el segundo numero: \n"))
        print("El resultado de la suma es: {suma}".format(suma=num_1+num_2))
    elif respuesta == 3:
        print("Hasta la proxima")
        break
    else:
        print("La opción ingresada no existe")
