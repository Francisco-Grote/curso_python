###
# 01 - Sentencias condicionales (if, elif, else)
# permiten ejecutar bloques de codigo solo si se cumple ciertas condiciones
###

# print("\n Sentencia simple condicional")

#edad = 18
#if edad >= 18:
#    print ("Eres mayor de edad")
# si no esta separado por sangria, sale del bloque del IF ejemplo

#edad2 = 15
#if edad2 >= 18:
#    print("Eres mayor de 18")

#print("Felicidades")

# Esto va a imprimir solamente el felicidades, ahora si lo metemos dentro del codigo no imprimira nada:

#edad2 = 15
#if edad2 >= 18:
#    print("Eres mayor de 18")
#    print("felicidades")


#print("\n Sentencia condicional else")
#edad = 15
#if edad >= 18:
#    print("Eres mayor de edad")
#else:
#    print("Eres menor de edad")
    
#nota = 9

#if nota >= 9:
#    print("Buenisima nota!")
#elif nota >= 7:
 #   print("Aprobado Notable")
#elif nota >= 5:
 #   print("Aprobado!")
#else:
 #   print("Desaprobado")


print("\nCondiciones multiples")

edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIA!")
# Or y And 
#en un pueblo
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la isla")
else:
    print("Podes pagarle al policia para conducir")
es_fin_de_semana = False
if not es_fin_de_semana:
    print("Anda a laburar!")
    
print("\nLa condicion ternaria:")
#es una forma concisa de un if-else en una linea de codigo
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple]
edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

