# Escribe un programa que pida una frase (entrada por teclado), y pase la frase 
# como parámetro a una función que debe eliminar los espacios en blanco 
# (compactar la frase). El programa principal imprimirá por pantalla el resultado final.

def condensador(txt):
    txt = txt.replace(" ", "")
    return txt

frase = str(input('>>> Escribe una frase:\n >  '))
print('\n>>> La frase condensada es:\n %s' % (condensador(frase)))