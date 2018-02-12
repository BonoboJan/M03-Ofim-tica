#coding: utf8
#Jandry Joel Aguilar Serrano
#12/02/18

Dividendo=input("Escriba el dividendo: ")
Divisor=input("Escriba el divisor: ")

if Divisor == 0:
    print "No se puede dividir por 0."
elif Dividendo % Divisor == 0:
    print "La división es exacta.", "Cociente:" , Dividendo/Divisor

else :
    print "La división no es exacta.", "Cociente:", Dividendo/Divisor, "Resto:", Dividendo % Divisor
