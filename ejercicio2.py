"""
	Ejercicio 2
	autor: jecueva11

	# encontrar la siguiente estructura
	# [("a", (30, 1)), ("b", (100, 2)), ("c", (20, 4))]

"""
# datos
lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]

# presentacion de una lista ordenada
print(list(zip(sorted(lista2), sorted(lista, key=lambda x: x[1]),)))
