"""
	Ejercicio 6
	autor: jecueva11
"""
# datos
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]
# sacar promedios
prom = list(map(lambda x: sum(x) / len(x), paraleloA))
# sacar la suma de las notas
suma = list(map(lambda x: sum(x), paraleloA))
# union de todos los componentes
funciones = (list(zip(prom, suma, nombres)))
# presentacion de datos en una lista con datos filtrados
print(list(filter(lambda x: x[0] <= 5, funciones)))

