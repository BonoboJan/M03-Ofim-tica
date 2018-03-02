#coding:utf8
# Inicializaciones
salir = "N"
num=1
while ( salir=="N" ):
    # Hago cosas
    print num, "+", num
    # Incremento
    num= num +1
    # Activo indicador de salida si toca
    if ( num>5 ): # Condición de salida
        salir = "S"
