#coding:utf8
# Inicializaciones
salir = "N"
num=0
limite=input("Introduzca el límite: ")
if limite <= 0:
    salir =="S"
    print "Introduzca un número límite positivo."
else:
    while ( salir=="N" ):
        # Hago cosas
        print num
        # Incremento
        num = num + 2
        # Activo indicador de salida si toca
        if ( num > limite): # Condición de salida
            salir = "S"
