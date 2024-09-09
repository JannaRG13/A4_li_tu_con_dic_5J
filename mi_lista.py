print ("-- EJEMPLO DE LISTAS -- ")
arcoiris=["verde", "azul", "morado"]
print(arcoiris)
longitud=len(arcoiris)
print(longitud)
print("Elementos que contiene la lista arcoiris: ",longitud)
print(f"Elementos que contiene la lista arcoiris: {longitud}")
print(" -- ACCEDIENDO A UN ELEMENTO DE LA LISTA -- ")
print(arcoiris[1])
print(f"Elemento en la posición 0 es: {arcoiris[0]}")
print("Elemento en la posición 0 es:",arcoiris[0])
print(" -- AGREGAR UN ELEMENTO DE LA LISTA -- ")
arcoiris.append("naranja")
print(arcoiris)
print(" -- LISTAR LOS ELEMENTOS DE LA LISTA CICLO FOR -- ")
for ramirez in arcoiris:
    print (ramirez)
    