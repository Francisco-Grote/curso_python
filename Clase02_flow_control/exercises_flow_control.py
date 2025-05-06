

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("\nEjercicio 1: determinar numeros")
numero_1 = input("Ingresar un numero:")
numero_2 = input("Ingresar otro numero:")

if numero_1 > numero_2:
    print(f"{numero_1}")
elif numero_1 == numero_2:
    print("Son iguales")
else:
    print(f"{numero_2}")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado
print("\nEjercicio 2: calculadora")

primer_numero = input("Ingrese un numero: ")
primer_numero = int(primer_numero)
segundo_numero = input("Ingrese otro numero: ")
segundo_numero = int(segundo_numero)
operacion = input("ingrese +, -, / o *: ")
if operacion == "+":
    print(f"{primer_numero + segundo_numero}")
elif operacion == "-":
    print(f"{primer_numero - segundo_numero}")
elif operacion == "/":
    print(f"{primer_numero / segundo_numero}")
elif operacion == "*":
    print(f"{primer_numero * segundo_numero}")
else:
    print("Ingrese un numero o operador valido")
    
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
anio = input("Ingrese un año: ")
anio = int(anio)
es_bisiesto = float
if anio / 4:
    print("El año es bisiesto")
elif es_bisiesto:
    print("El año NO es bisiesto")
else:
    print("Ingrese algo valido")
    


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = input("Ingrese una edad:")
edad = int(edad)

if edad <= 2:
    print("Es un bebe")
elif edad >= 3:
    print("Es un niño")
elif edad >= 13:
    print("es un adolescente")
elif edad >= 18:
    print("es un adulto")
elif edad >= 65:
    print("es un mayor")
else:
    print("No ingresaste nada valido")
    