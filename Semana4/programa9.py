""" Programa 9
    Nombre: Brallan Josue Tolentino Velasco
    Fecha: 09/02/2023
    Descripcion:
"""
def mayor(numero1, numero2): #Variables

    result = None
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