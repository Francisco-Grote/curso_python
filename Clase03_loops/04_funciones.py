"""
04 - Funciones
Bloques de codigo reutilizables que realizan una tarea específica.
"""

""" Definicion  de una funcion
def nombre_de_funcion(parametro1, parametro2):
    #docstring
    cuerpo de la funcion
    return valor_de_retorno #opcional
"""
from os import system
if system("clear") != 0: system("cls")

#Ejemeplo de una funcion para imprimir algo en consola
def saludar():
        print("Hola, mundo!")

# Ejemeplo mio
def suma():
        numero1 = 1
        numero2 = 1
        print(f"La suma de {numero1} + {numero2} es = {numero1 + numero2}")
# ejemplo de funcion con parametro
def saludar_a(nombre):
    print(f"Hola, {nombre}!")

saludar_a("Juan")
saludar_a("Maria")
saludar_a("Pedro")
saludar_a("Ana")
#El parametro es una variable que se pasa a la funcion
#El argumento es el valor que se pasa al parametro

# Funciones con mas parametros
# Funcion que suma dos numeros
def sumar(a, b):
    suma = a + b
    return suma
print(sumar(5, 10))

# docuemntar las funciones con docstring
def restar(a,b):
    """Resta dos numeros y devuelve el resultado."""
    return a- b
print(restar.__doc__)  # Imprime la documentacion de la funcion restar

# parametros por defecto
def multiplicar(a, b=2):
    return a * b
print(multiplicar(5))  # Imprime 10, ya que b toma el valor por defecto de 2
print(multiplicar(5, 3))  # Imprime 15, ya que b toma el valor de 3

#argumentos por clave
def describir_persona(nombre, edad, ciudad="Desconocida"):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
describir_persona("Alice", 30)  # Usa el valor por defecto para ciudad
describir_persona("Bob", 25, "Madrid")  # Especifica todos los argumentos

#arugmentos por clave
# parametros nombrados
describir_persona(nombre="Alice", edad=30, ciudad="Barcelona")

#Argumentos de longitud de variable (args y kwargs)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma
print(sumar_numeros(1, 2, 3, 4, 5))  # Imprime 15
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
mostrar_informacion_de(nombre="Alice", edad=30, ciudad="Barcelona", profesion="Ingeniera")

"""
el ejercicio es volver a ejercicios anteriores y crear funciones que realicen las tareas"""
