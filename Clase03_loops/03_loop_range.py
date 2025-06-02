###
#### range()
###

from os import system
if system("clear") != 0: system("cls")

# print("\n range:")

# nums = range(10)  # Crea un objeto range de 0 a 9

# print(nums)  # range(0, 10) 

#genero una secuencia de numeros del 0 al 9
# for num in range(5, 10):
#     print(num)
# #range (inicio, fin, salto)
# for num in range(0, 10, 2):
#     print(num)

for num in range(-5, 0):
    print(num)
# for num in range(10, 0, -1):
#     print(num)

nums = range (10)  # Crea un objeto range de 0 a 9
list_nums = list(nums)  # Convierte el objeto range a una lista
print(list_nums)  # Imprime la lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]