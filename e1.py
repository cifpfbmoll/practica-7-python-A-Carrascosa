# Escribe un programa que pida un texto por pantalla, este texto lo pase como 
# parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas 
# y luego todo en mayúsculas.

def mayusculas(texto_mayusculas):
    texto_mayusculas = texto_mayusculas.upper()
    return texto_mayusculas

def minusculas(texto_minusculas):
    texto_minusculas = texto_minusculas.lower()
    return texto_minusculas

texto = str(input('>>> Escribe un texto:\n >  '))

print('\n>>> Texto original:\n >  %s' % (texto))
print('>>> Texto en mayúsculas:\n >  %s' % (mayusculas(texto)))
print('>>> Texto en minusculas:\n >  %s' % (minusculas(texto)))