"""
    Programa 8
    Nombre: Brallan Josue Tolentino Velasco
    Fecha: 07/02/2023
    Descripcion: 
"""
n1= int(input("numero1: "))
n2= int(input("numero2: "))
#Solucion 1
if n1 > n2:
    print (n1)
if n2 > n1:
    print (n2)
if n1==n2:
    print (None)

#Solucion 2
if n2 > n1:
    print(n2)
if n1 > n2:
    print (n1)
else:
    print (None)

#Solucion 3
if n1 > n2:
    print(n1)
elif n2 > n1:
    print (n2)
else:
    print (None)

#Solucion 4
if n1==n2:
    print (None)
elif n1