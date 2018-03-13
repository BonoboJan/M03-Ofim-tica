#coding:utf8
# Inicializaciones
salir = "N"
num=1
suma = 0
while ( salir=="N" ):
    # Hago cosas
    print num, "+" , 
    # Incremento
    suma = suma + num
    num= num +1
    # Activo indicador de salida si toca
    if ( num>5 ): # Condición de salida
        print "=" , suma
        salir = "S"
