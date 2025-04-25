###
# o5 _Entrada de usuario input
# la funcion input() obtiene datos del usuario a traves de consola
###

nombre = input("Hola como te llamas?\n")
print(f"hola {nombre}, encantado de conocerte")

age = input("¿Cuantos años tienes?\n")
age = int(age)
print(f"Dentro de 20 años tendras: {age + 20}")

print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives\n").split()

print(f"Vives en {country}, {city}")
