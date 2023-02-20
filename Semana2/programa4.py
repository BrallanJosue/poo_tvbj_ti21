"""
    programa 4
    Nombre: Brallan Josue Tolentino Velasco 
    Fecha: 26/01/2023
    Descripcion: suma de dos numeros utilizando .format
"""

numero1 = 10 #primera variable
numero2 = 5 #segunda variable
print ("{} + {} = {}" .format (numero1, numero2, numero1+numero2)) #sentencia que imprime 10+5=15
print ("{n1} + {n2} = {suma}" .format (n1=numero1, n2=numero2, suma=numero1+numero2)) #Actualizacion por nombre 
print ("{n1} + {n2} = {suma}" .format (n1=numero1, n2=numero2, suma=numero1+numero2)) #Imprime la suma de dos numerosa con .format 
print ("{numero1} + {numero2}" .format (numero1, numero2, numero1+numero2)) #error porque no asigna variable 
