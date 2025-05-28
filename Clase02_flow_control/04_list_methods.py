from os import system
if system("clear") != 0: system("cls")

lista1 = [1, 2, 3, 4, 5]

lista1.append(6) ## añade un elemento al final
print(lista1)

lista1.insert(1, '!!') # inserta un elemento en la posicion que le indiquemos como primer argumento
print(lista1)

## lista1.extends(['12123', '3asd'])
print(lista1)

#ELIMINAR ELEMENTOS DE UNA LISTA
lista1.remove('!!')
print(lista1) #elimina la primera declaracion de este elemento

lista1.pop() ##te elimina el ultimo elemento de la lista
print(lista1)


lista1.clear() #elimina todo los elementos de la lista
print(lista1)

#Eliminar rango de elementos
lista1 = [ '1', 'asd', 'francsico','Carlos']
del lista1[1:3]
print(lista1)

## mas metodos utiles
print("Ordenar listas modificando la original")
numbers = [3 ,1 ,2 ,4 ,5]
numbers.sort()
print(numbers)

print("Ordenar listas creando nueva lista")
numbers = [3 ,1 ,2 ,4 ,5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar listas de texto (todo minuscula)")
frutas = ["peras", "bananas","manzanas"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar listas de texto (mezclado mayuscula)")
frutas = ["Peras", "Bananas","manzanas"]
frutas.sort(key=str.lower)
print(frutas)

### mas metodos utiles
animals = ["gatos", "perros", "perros", "dinosaurios"]
print(len(animals))
print(animals.count("perros"))
print("gatos" in animals)
print("ave" in animals)



###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("EJERCICIO 1: ")
#variable:
lista = [1, 2, 3, 4, 5]

lista.append(6)
lista.insert(1, 10)
lista.remove(10)
lista.insert(0, 10)
print(lista)
# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print("EJERCICIO 2: ")
#variables
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
#ejercicio
lista_a.extend(lista_b)
lista_a.remove(1)
lista_a.pop(2)
lista_b.clear()
print(lista_a)
print(lista_b)


# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print("EJERCICIO 3:")
#Variables:
listaej3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ejercicio
del listaej3[2:4]
print(listaej3)


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print("EJERCICIO 4:")
#Variables:
listaej4 = [5, 2, 8, 1, 9, 4, 2]
#ejercicio
listaej4.sort()
lista.count(2)
print(listaej4)
print(listaej4.count(2))
print(7 in listaej4)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("EJERCICIO 5:")
#Variables:
original = [1, 2, 3]
#ejercicio
copia1 = original[0:3]
copia2 = original.copy()
referencia = original[0:3]
referencia[0] = 10
print(original)
print(copia1)
print(copia2)
print(referencia)
# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print("EJERCICIO 6:")
listaej6 = ["Manzana", "Pera", "BANANA", "naranja"]
listaej6.sort(key=str.lower)
print(listaej6)