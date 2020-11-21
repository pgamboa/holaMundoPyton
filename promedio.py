n1 = 25
n2 = 2.6
n3 = 56

p = n1+n2+n3/3
t1 = str(type(p)) #cambio a string el tipo de dato de la respuesta

print(t1)
redondeo=round(p,2) #round permite redondear los decimales

print("El promedio de tres números sin redondeo es: \n"+str(p)+ "y es de tipo \t" + t1)
print("El promedio de tres números con dos decimales es: \n"+str(redondeo) + "y es de tipo \t" + t1)