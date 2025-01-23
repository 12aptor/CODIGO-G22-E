lista = ["Python", "Rust", "Javascript", "C++"]

""" Acceso a elementos """
print(lista[0]) # Primer elemento

""" Acceso a rango de elementos """
print(lista[0:3]) # Rango de elementos

""" Acceso a rango de elementos con saltos """
print(lista[0:4:2]) # Rango de elementos con saltos

""" Acceso a elementos desde el final """
print(lista[-1]) # Último elemento

""" Acceso a rango de elementos desde el final """
print(lista[-3:]) # Rango de elementos desde el final

""" Agregar elementos """
lista.append("C#")

""" Eliminar elementos por índice """
lista.pop(2)

""" Eliminar elementos """
lista.remove("C#")

""" Eliminar todos los elementos """
lista.clear()

""" Invertir lista """
lista.reverse()

""" Ordenar lista """
lista.sort()