"""
    Programa 6
    Nombre: Brallan Josue Tolentino Velasco
    Fecha: 30/01/2023
    Descripcion: Calculo de perimetro y area de cualquier triangulo
"""
print("Calcula el area y perimetro de un triangulo") #Imprime un mensaje de consola

lado1 = float(input("Primer lado del triangulo: ")) #Pide al usuario el primer valor
lado2 = float(input("Segundo lado del triangulo: ")) #Pide al usuario el segundo valor
lado3 = float(input("Tercer lado del triangulo: ")) #Pide al usuario el terver valor

perimetro = lado1 + lado2 + lado3 #Calcula el perimetro
semiperimetro = perimetro / 2 #Calcula el semiperimetro
area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5 #Formula para calcular el area

print("El perimetro es: ",perimetro) #Imprime el perimetro
print("El area es: ",area) #Imprime el area
