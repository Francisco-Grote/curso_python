###
# 03 - Listas
# Secuencias mutables de elementos
# pueden contener elementos de diferentes tipos
###
import os
os.system("clear")
#Creacion de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzanas", "peras", "bananas"]
lista3 = [1, "hla", 3.14, True]

lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

### acceso a elementos de la lista
print("\nAcceso a alementos del indice")
print(lista2[0]) # manzanas
print(lista2[1]) # peras
print(lista2[-1]) # bananas

print(lista_de_listas[1][0])

# slicing
print(lista1[1:4]) # de inicio a inicio. Por eso entra el numero 2
print(lista1[:3])
print(lista1[:]) #copia la lista

#modificar una lista
lista1[0] = 20
print(lista1)
#añadir elementos a una lista
lista1 = lista1 + [4, 5, 6]
print(lista1)

lista1 += [7, 8 ,9]
print(lista1)

print("Longitud de la lista", len(lista1))
