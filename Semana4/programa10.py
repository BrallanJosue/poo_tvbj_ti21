"""
    Programa 10
    Nombre: Brallan Josue Tolentino Velasco
    Fecha: 09/02/2023
    Descripcion: Compara dos numeros e imprime el mayor de ellos
"""

def mayor (numero1:int, numero2:int)-> int: #define la funcion mayor con dos variables
    result = None # Creacion de la variable resulta con el valor None 
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1:
        result = numero2
    return result

print (mayor(2, 1)) #2
print (mayor(1, 2)) #2
print (mayor(2, 2)) #None
print (mayor(2, -1)) #2
print (mayor(-1, 2)) #2
print (mayor(-1, -1)) #None
print (mayor(-2, -1)) #-1
print (mayor(-1, -2)) #-1
   