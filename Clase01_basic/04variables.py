## Tipo de variables
## las variables sirven para guardar datos en memora
# Python es de tipado dinamico

# asignar una variable
# solo hace falta pasar nombre de variable y valor

my_name = "Francisco"
my_Surname = "Grote"
my_age = 20
print(my_name + " " + my_Surname + " " + str(my_age))

## las variable se pueden reasignar y pueden cambiarse ejemplo:
age = 20
age = 21 ## toma la ultima variable declarada
print(age)

# tipado dinamico: el tipo de dato se determine
# no tienes que declararlo explicitamente
name = "carlos"
print(type(name))
name = 20
print(type(name))

## tipado fuerte no realiza conversiones estaticas
## f-string (literal de cadena de formato)
print(f"hola {my_name}, tengo {age + 20} años")
## Convenciones de nombres de variables
mi_nombre_de_variable = "okkkk" #snake_case

## python NO TIENE CONSTANTES.

MI_CONSTANTE = "SOY UNA CONSTANTE" #Cuando hay que declarar constantes se hace de esta manera


