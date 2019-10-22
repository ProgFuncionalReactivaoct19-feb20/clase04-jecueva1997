"""
	Ejercicio 1
	autor: jecueva11

"""
# datos
listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]
# cambio del orden las listas
lista1 = sorted(listaA)
lista2 = sorted(listaB, reverse=True)

res = list(zip(lista1, lista2))
# se saca el maximo
m = max(res)
# pressentacion de resultados
print(res)
print(m)