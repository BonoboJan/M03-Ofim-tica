#coding:utf8
#Jandry Joel
#23/02/18

num1=input("Introduzca el primer valor: ")
num2=input("Introduzca el segundo valor: ")

if (num1==0) or (num2==0) :
    print "Introduzca valores diferentes a 0."
else:
    if num1>num2 :
        mayor=num1
        menor=num2
    else:
        mayor=num2
        menor=num1
    if mayor%menor==0:
        print mayor,"es múltiplo de ", menor
    else:
        print mayor,"no es múltiplo de ", menor
