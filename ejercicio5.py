"""
	Ejercicio 5
	autor: jecueva11
"""
# datos
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
# sacar los promedios en una lista con un tuple
prom = (list(zip(tuple(map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA)), nombres)))
# presentacion de promedio
print (prom)
# presentacion de promedio maximo
print (max(prom))
# invertir datos
prom1 = reversed(prom)
# presentacion de los datos invertidos
print (list(reversed(prom)))