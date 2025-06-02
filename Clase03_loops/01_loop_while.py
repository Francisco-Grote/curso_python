# '''
# 01 - Bucles (while)
# Permiten ejecutar un bloque de codigo repetidamente mientras se cumple una condicion
# '''
from os import system
if system("clear") != 0: system("cls")

# print("\nBucle while:")

 #bucle con una simple condicion
# contador = 0
# while contador <= 5:
#     print(contador)
#     contador += 1 #importante! para no generar bucle infinito

# ## Break se utiliza para romper el bucle
# print("\nBucle while con break:")
# contador = 0
 
# while contador <= 100:
#     print(contador)
#     contador += 1
#     if contador % 5 == 0:
#         print("Es multiplo de 5")
#         break #sale del bucle

# ##salte iteracion y continua con el bloque
# print("\nBucle while con continue:")
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0: ## es multiplo de 2?
#         continue ## Si es multiplo de 2 continua
#     print(contador)
#     break

# print("\nBucle while con else:")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
#     break
# else:
#     print("El bucle a terminado")

# # pedirle al usuario un numero que tiene que ser positivo, sino no le dejamos en paz

# numero = -1
# while numero < 0:
#     numero = int(input("Escribe un numero positivo: "))
#     if numero < 0:
#         print("El numero tiene que ser positivo!")

# print(f"El numero que has introducido es: {numero}")

# numero = -1
# while numero < 0:
#     try:
#         numero = int(input("Ingrese un numero positivo:"))
#         if numero < 0:
#             print("El numero tiene que ser positivo! ")
#     except:
#         print("Lo que introduces debe ser un numero, sino KA BOOOM!")
# print("Lo que introduces debe ser un numero sino explota!!")

# print(f"El numero que has introducido es: {numero}")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
numero = 10
while numero >= 1:
    print(numero)
    numero -= 1
    
print("El bucle termino")


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numeros = 1
suma_pares = 0
while numeros <= 20:
    if numeros % 2 == 0:
        suma_pares += numeros
    numeros += 1

print(f"La suma de numeros pares es: {suma_pares}")


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

nusuario = int(input("Introduzca un número entero positivo!"))
factorial = 1
contador = 1

while contador <= nusuario:
    factorial *= contador
    contador +=1

print(f"El factorial del {nusuario} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

contrasenia = ""
while len(contrasenia) < 8:
    contrasenia= input(("Introduzca una contraseña de al menos 8 caracteres: "))
    if len(contrasenia) < 8:
        print("La contrasenia debe tener al menos 8 caracteres")

print("Contraseña valida")
# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

numero = int(input("Introduzca un numero"))
multiplicador = 1

while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f"{numero} X {multiplicador} = {resultado}")
    multiplicador += 1
    
