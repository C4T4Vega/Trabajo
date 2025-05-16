#Estructuras de control

#Condicionales
#if
'''if True:
    print("Tambien puede ser False")
'''
'''
x = 10
if x > 5:
print("Es verdad")
'''
#if-else
'''
edad = 18
if edad >=18:
 print("mayor de edad")
else:
 print("menor de edad") 
'''
#if-elif-else, se puede usar más de un elif
''' 
x = 123:
if x > 10:
    print("X mayor a 10")
elif x == 10:
    print("X igula a 10")
else:
    print("X menor a 10")
'''

#while
'''
while True:
    print("Sección de codigo")
'''
""" Agrega condición para evitar bucle infinito

contador = 0
while contador < 5:
    print("El contador es: ", contador)
    contador = contador + 1
"""

#For 
''' Tiene inicio y final

for i in range(1,6):
    print("Indice es: ",i)
'''
'''En listas, tuplas

frutas = ['manzanas', 'peras', 'naranjas']
for fruta in fruta:
    print(frutas)
'''
'''En diccionarios

diccionario = {'a':1, 'b':2, 'c':3}
for clave, valor in diccionario.items():
    print("clave: ", clave, " Valor: ", valor)
'''