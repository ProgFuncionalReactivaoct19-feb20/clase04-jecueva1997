"""
	Ejercicio 4
	autor: jecueva11
"""
# datos
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
# sacar los promedios de los paralelos con un tuple
promedio = tuple(map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA))
# presentcion de una lista con un zip
print(list(zip(promedio, nombres)))