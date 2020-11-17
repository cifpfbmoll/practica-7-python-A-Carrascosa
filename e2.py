# Escribe un programa que pida un texto por pantalla, este texto lo pase como 
# parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas 
# y luego todo en mayúsculas.

def arrejuntador(nm, fn, ln):
    cm = nm + ' ' + fn + ' ' + ln 
    return cm

nombre = str(input('>>> Escribe un nombre:\n >  '))
apellido1 = str(input('>>> Escribe el primer apellido de %s:\n >  ' % (nombre)))
apellido2 = str(input('>>> Escribe el segundo apellido de %s:\n >  ' % (nombre)))

print('\n>>> El nombre completo de %s es:\n >  %s' % (nombre, arrejuntador(nombre, apellido1, apellido2)))