#coding: utf8
#Jandry Joel
#22/02/18
import os
os.system("clear")
print "Qué tipo de gasolina quiere? Esto es lo que ofrecemos: "
print """-Super:Normal(1)[1,5€/L] 
Turbo(2)[1,55€/L]
-Sin plomo: Normal(3)[1,6€/L]
Con aditivos(sabor naranja)(4)[1,65€/L]
-Diesel:Normal(5)[1,7€/L] 
Fast & Furious(6)[1,75€/L]"""
tipo=input("Qué tipo de gasolina quiere?[1-6]: ")
if tipo == 1 :
    print "Ha seleccionado la gasolina Super:Normal"
    litros=input("Cuántos litros de gasolina quiere?: ")
    if litros==0 :
        print "Este valor no es correcto."
    else:
        print "De acuerdo, serán: ", 1.5*litros, "€"
elif tipo==2 :
    print "Ha seleccionado la gasolina Super:Turbo"
    litros=input("Cuántos litros de gasolina quiere?: ")
    if litros==0 :
        print "Este valor no es correcto."
    else:
        print "De acuerdo, serán: ", 1.55*litros, "€"
elif tipo==3 :
    print "Ha seleccionado la gasolina Sin plomo:Normal"
    litros=input("Cuántos litros de gasolina quiere?: ")
    if litros==0 :
        print "Este valor no es correcto."
    else:
        print "De acuerdo, serán: ", 1.6*litros, "€"
elif tipo==4 :
    print "Ha seleccionado la gasolina Sin plomo:Con aditivos(sabor naranja)"
    litros=input("Cuántos litros de gasolina quiere?: ")
    if litros==0 :
        print "Este valor no es correcto."
    else:
        print "De acuerdo, serán: ", 1.65*litros, "€"
elif tipo==5 :
    print "Ha seleccionado la gasolina Diesel:Normal"
    litros=input("Cuántos litros de gasolina quiere?: ")
    if litros==0 :
        print "Este valor no es correcto."
    else:
        print "De acuerdo, serán: ", 1.7*litros, "€"
elif tipo==6 :
    print "Ha seleccionado la gasolina Diesel:Fast&Furious"
    litros=input("Cuántos litros de gasolina quiere?: ")
    if litros==0 :
        print "Este valor no es correcto."
    else:
        print "De acuerdo, serán: ", 1.75*litros, "€"
else:
    print "Introduzca un valor del 1 al 6, porfavor."

    
    
        
    
