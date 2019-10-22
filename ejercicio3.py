"""
	Ejercicio 3
	autor: jecueva11

	# encontrar la siguiente estructura
	# [((20, 4), "c"), ((30, 1), "b"), ((100, 2), "a")]

"""
# datos
lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]
# utilizacion del map para transformar en mayusculas
listaM = map(lambda x: x.upper(), lista2)
# presentacion de una lista con un zip y un sorted para ordenar
print(list(zip(sorted(lista, key=lambda x: x[1]), sorted(listaM, reverse=True))))