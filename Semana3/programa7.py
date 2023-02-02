"""
    Programa 7
    Nombre: Brallan Josue Tolentino Velasco
    Fecha: 31/01/2023
    Descripcion: Calcular e imprimir el area y perimetro de un cuadrado y circulo
"""
print ("programa que calcule el area y perimetro de un circulo") #imprime un mensaje de consola 
pi = 3.1416
radio = float(input("El radio es: ")) # pide el valor de la variable radio 
perimetro = 2*pi*radio # Formula para calcular el perimetro 
area =  pi*radio**2 #Formula para calcular el area
print("El area de un circulo", radio, "De radio es",area, "cm²") #Imprime el resultado
print("El perimetro de un circulo", radio, "radio es", perimetro) #Imprime el resultado
print("Programa que calcula el area y perimetro de un cuadrado") #Imprime un mensaje de consola
lado = float(input("Lado de cuadrado: ")) #El valor de Lado
perimetro = lado * 4 #Formula para sacar el perimetro de un cuadrado
area =  lado * lado #Formula que imprime el area de un cuadrado
print("El area de un cuadraddo es", lado, "lado es", area, "cm²") #Imprime el area
print("El perimetro de un cuadrado es", lado, "lado es", perimetro, "cm²" ) #Imprime el perimetro

