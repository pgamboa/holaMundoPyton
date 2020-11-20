lista_1=list(range(0,20))
list_2=list(range(5,50,5))
list_3=[]

for i in lista_1:
    if i in list_2 and i not in list_3:
        list_3.append(i)

print(list_3)
print(list_3)
