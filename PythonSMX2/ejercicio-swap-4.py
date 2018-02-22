
#coding:utf8
#Jandry Joel
#21/02/18

#Hi assignem les variables
cajon1="movil"
cajon2="bocadillo"
cajon3="boli"
cajon4="bebida"
cajonextra="-"
#Fem un print de les variables abans de fer el swap
print "Cajon1=", cajon1
print "Cajon2=", cajon2
print "Cajon3=", cajon3
print "Cajon4=", cajon4
#Realitzem el swap
cajonextra=cajon1
cajon1=cajon3
cajon3=cajonextra
cajonextra=cajon2
cajon2=cajon4
cajon4=cajonextra
#Tornem a fer un print de les variables per veure el resultat
print "----------------------"
print "Cajon1=", cajon1
print "Cajon2=", cajon2
print "Cajon3=", cajon3
print "Cajon4=", cajon4
