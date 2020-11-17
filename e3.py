# Escribe un programa que pida un texto por pantalla, este texto lo pase como 
# parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas 
# y luego todo en mayúsculas.

def separador(txt):
    print('\n>>> La frase separada es:\n ')
    for i in range(len(txt)):
        print(' >  %s' % (txt[i]))

frase = str(input('>>> Escribe una frase:\n >  '))
separador(frase)