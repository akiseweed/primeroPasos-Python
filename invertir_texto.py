'''
invertir una cadena de texto 
'''
def Invertir():
    cadena = str(input(f"Ingrese una palabra a invertir: "))
    invertir = cadena[::-1]
    print(invertir)
Invertir()