'''
01 - Bucles (while)
Permiten ejecutar un bloque de codigo repetidamente mientras se cumple una condicion
'''
from os import system
if system("clear") != 0: system("cls")

print("\nBucle while:")

#bucle con una simple condicion
contador = 0
while contador <= 5:
     print(contador)
     contador += 1 #importante! para no generar bucle infinito

## Break se utiliza para romper el bucle
print("\nBucle while con break:")
contador = 0
 
while contador <= 100:
    print(contador)
    contador += 1
    if contador % 5 == 0:
        print("Es multiplo de 5")
        break #sale del bucle

##salte iteracion y continua con el bloque
print("\nBucle while con continue:")
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0: ## es multiplo de 2?
        continue ## Si es multiplo de 2 continua
    print(contador)