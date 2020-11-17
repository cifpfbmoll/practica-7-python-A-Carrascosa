# Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento 
# y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman.
# Si coinciden solo las dos últimas tiene que decir que riman un poco y si no, que no riman.

def rimas(w1, w2):
    if w1[len(w1)-3: len(w1)] == w2[len(w2)-3: len(w2)]:
        print('\n>>> Las palabras %s y %s riman.\n' % (w1, w2))
    elif w1[len(w1)-2: len(w1)] == w2[len(w2)-2: len(w2)]:
        print('\n>>> Las palabras %s y %s riman un poco.\n' % (w1, w2))
    else:
        print('\n>>> Las palabras %s y %s no riman.\n' % (w1, w2))

palabra1 = str(input('>>> Escribe una palabra:\n >  '))
palabra2 = str(input('>>> Escribe otra palabra:\n >  '))

rimas(palabra1, palabra2)