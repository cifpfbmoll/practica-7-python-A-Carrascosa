# Escribe un programa que pida una frase (entrada por teclado), y le pase como 
# parámetro a una función dicha frase. La función debe sustituir todos los 
# espacios en blanco de una frase por un asterisco, y devolver el resultado 
# para que el programa principal la imprima por pantalla.

def asterisqueador(txt):
    txt = txt.replace(" ", "*")
    return txt

frase = str(input('>>> Escribe una frase:\n >  '))
print('\n>>> La frase con asteríscos es:\n %s' % (asterisqueador(frase)))