#Listas 
lista_1 = [1, 2, "A", 'a']
#las listas se comienzan a leer desde 0
#Imprimibles, completas o especificas
#Selecciona elemento: lista_1[3]  por posición 
#Modifica: ej: lista_1[3] = 'b'
#añade: lista_1.append(5)
#Elimina: lista_1.remove("A")

#Tuplas
tupla = (1, 3.5, "A")
#Comienza a leer desde 0
#Im2primibles, completas o especificas

#Diccionarios
diccionario_1 = {
    "clave1" : 1,
    "clave2" : 2,
    "clave3" : 'Hola',
    "nombre"  : 'S I'
}
#Imprimibles, completas o especificas
#Modifica: diccionario1["clave1"] = "Algo"
#Añade: diccionario1["clave5"] = 'N O' 

#Conjuntos
conj_1 = {1, 2 ,3}
conj_2 = {3, 4, 5}
#Imprimible (no imprime repetidos: ej- 3)
union = conj_1.union(conj_2)
#Une datos pero sin repetir
interseccion = conj_1.intersection(conj_2)
#Encuentra Valor en común
diferencia = conj_2.difference(conj_1)
#Retorna los valores diferentes ej: 4, 5
