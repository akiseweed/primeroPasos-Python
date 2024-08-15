'''
Calcular el área de un rectángulo
'''
def AreaRectangulo():
    base=int(input("ingrese la base del rectángulo: "))
    altura=int(input("ingrese la altura del rectángulo: "))
    area= base*altura
    print(f"El área del rectángulo es: {area}")
AreaRectangulo()