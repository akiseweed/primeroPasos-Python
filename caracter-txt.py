""""
replace=reemplazo 
reemplazar un caracter en una cadena
"""
def remplazar():
    cadena="amarillo"
    cadenaAlterada= cadena.replace("o","asd")#reemplaza el primer item, en este caso la "o" por el segundo parámetro 
                                                #en este caso asd, pero puede ser cualquier palabra
    print(f"nueva = {cadenaAlterada}")
remplazar()