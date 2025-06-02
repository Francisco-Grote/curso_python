### 
#01 - bucles for
# permiten ejecutar un bloque de codigo repetidamente mientras itera un iterable o una lista
###
from os import system
if system("clear") != 0: system("cls")

print("\nBucle for:")

## iterar una lista

frutas = ["manzanas", "bananas"]
for fruta in frutas:
    print(fruta)


    #iterar sobre cualquier cosa que sea iterable
cadena = "fran"
for caracter in cadena:
    print(caracter)


#Recuperar el indice con for
perros = ["cairo", "moshi"]
for index, perro in enumerate(perros):
    print(f"el indice es {index} y el perro es {perro}")

# bucles anidados

letras = ["a", "b", "c"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

print("\nBucle for con break:")
animales = ["loro", "gato", "perro"]
for index, animal in enumerate(animales):
    print(animal)
    if animal == "gato":
        print(f"El gato se encuentra en el indice {index}")
        # si se encuentra el gato, se sale del bucle
        break

#continue
print("\nBucle for con continue:")
animales = ["loro", "gato", "perro"]
for index, animal in enumerate(animales):
 if animal == "loro":
     continue
print(animal)

print("\nComprension de listas:")
animales = ["loro", "gato", "perro"]
animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)
#muestra los numeros pares
pares = [numero for numero in range(10) if numero % 2 == 0]
print(pares)

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for numero_par in numeros:
    if numero_par % 2 == 0:
        print(numero_par)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
suma = 0
for numero in numeros:
    suma += numero
    media = suma / len(numeros)
print(f"La media de los números es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
maximo = 0
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(f"El número máximo en la lista es: {maximo}")
# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(f"Palabras con más de 5 letras: {palabras_largas}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower()
contador = 0
for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1
print(f"Hay {contador} palabras que empiezan con la letra '{letra}'.")