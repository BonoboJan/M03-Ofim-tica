
#coding: utf8
#Jandry Joel Aguilar Serrano
#08/02/18

A=input("Introduzca el valor A: ")
B=input("Introduzca el valor B: ")
C=input("Introduzca el valor C: ")

if (A==B) or (A==C) :
    print "Hay dos valores iguales. Introduzca tres valores diferentes."
else :
    if ((A==B) and (B==C)) or (:
       print "Los tres valores son iguales. Introduzca tres valores DIFERENTES."
    else :
        if (A>B) and (A>C) :
            if (B<C) :
                print "El valor A es el mayor y el B es el menor"
            else :
                print "El valor A es el mayor y el C es el menor"
        else :
            if (B>A) and (B>C) :
                if (C<A) :
                    print "El valor B es el mayor y el C es el menor"
                else :
                    print "El valor B es el mayor y el A es el menor"
            else :
                if (C>A) and (C>B) :
                    if (B<A) :
                        print "El valor C es el mayor y el B es el menor"
                    else :
                        print "El valor C es el mayor y el A es el menor"
            
                    
            
            
