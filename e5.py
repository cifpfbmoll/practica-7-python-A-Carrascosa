# Escribe un programa que te pida una frase y una vocal (entrada por teclado), 
# y pase estos datos como parámetro a una función que se encargará de cambiar 
# todas las vocales de la frase por la vocal seleccionada. Devolverá la función 
# la frase modificada, y el programa principal la imprimirá:

def reemplazo(txt, letter):
    for i in ["a", "e", "i", "o", "u"]:
        txt = txt.replace(i, letter)
    return txt

frase = str(input('>>> Escribe una frase:\n >  '))
vocal = str(input('>>> Escribe una vocal:\n >  '))

print('\n>>> La frase reemplazada es:\n %s' % (reemplazo(frase, vocal)))