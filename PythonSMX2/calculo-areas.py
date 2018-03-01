#coding:utf8
#Jandry Joel
#01/03/18

from math import pi
import os
os.system("clear")
print """Calculadora de áreas:
--------------
a)Triangulo
b)Círculo"""
figura=raw_input("¿Qué figura quiere calcular(Escriba T o C): ")
if figura=="T" :
    base=input("Escriba la base: ")
    altura=input("Escriba la altura: ")
    if base < 0 or altura < 0:
        print "Introduzca números positivos."
    else :
        area=base*altura
        print "Un triángulo de base",base,"y altura",altura,"tiene un área de", round(area,2), "."
elif figura=="C" : 
    radio=input("Escriba el radio: ")
    if radio < 0:
        print "Introduzca números positivos"
    else:
        area=2*pi*radio
        print "Un círculo de radio",radio,"tiene un área de",round(area,2), "."
else:
    print "Opción no válida. Introduzca T o C."
