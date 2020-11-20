lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]



while True:
    num = int(input("Ingrese un numero entre 0-9: "))
    if num >= 0 and num <= 9:
        print("El numero {} esta dentro del rango ".format(num))
        break
if num in lista:
    print ("El numero ", num, "se encuentra en la lista ", lista)
else:
    print ("El numero ", num, "no encuentra en la lista ", lista)
