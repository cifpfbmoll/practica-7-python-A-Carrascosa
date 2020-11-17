# Escribe un programa que lea una frase (entrada por teclado), y la pase como parámetro 
# a un procedimiento. El procedimiento contará el número de vocales (de cada una) que 
# aparecen, y lo imprimirá por pantalla.

def contador(txt):
    for i in ["a", "e", "i", "o", "u"]:
        vocales = list(txt).count(i)
        print(' >  Hay %s %s' % (vocales, i))

frase = str(input('>>> Escribe una frase:\n >  '))
contador(frase)