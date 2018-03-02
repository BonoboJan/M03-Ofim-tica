#coding:utf8
# Inicializaciones
salir = "N"
num=1
limite=input("Introduzca un número límite: ")
if limite <= 0:
    salir =="S"
    print "Introduzca un número límite positivo."
else:
    while ( salir=="N" ):
        # Hago cosas
        print num
        # Incremento
        num= num +1
        # Activo indicador de salida si toca
        if ( num>limite ): # Condición de salida
            salir = "S"
