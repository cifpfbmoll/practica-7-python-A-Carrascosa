# Escribe un programa que lea el nombre de una persona y un carácter (entrada por teclado), 
# le pase estos datos a una función que comprobará si dicho carácter está en su nombre. 
# El resultado de dicha función lo imprimirá el programa principal por pantalla.

def buscador(nm, letter):
    nm = nm.upper()
    letter = letter.upper()
    resultado = nm.find(letter)
    if resultado != -1:
        resultado = 'SI'
    else:
        resultado = 'NO'
    return resultado

nombre = str(input('>>> Escribe un nombre:\n >  '))
vocal = str(input('>>> Escribe una vocal:\n >  '))

print('\n>>> La letra %s %s está en el nombre \'%s\'\n' % (vocal, buscador(nombre, vocal), nombre))