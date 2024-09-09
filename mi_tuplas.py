print (" -- EJEMPLOS DE TUPLAS --")
canciones=("Te amo", "El Noa Noa", "Amor Eterno")
print(canciones)

y = list(canciones)
print(y)
y[1] = "La puerta negra"
x = tuple(y)
print(x)