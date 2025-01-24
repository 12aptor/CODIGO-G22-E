def suma(a, b):
    return a + b

print(suma(2, 3))

""" Funciones con argumentos arbitrarios """
def mi_funcion(*args):
    print(args)

mi_funcion(False, True, "Hola", 10.5)

""" Funciones con argumentos con clave """
def mi_funcion2(nombre, apellido):
    print(nombre, apellido)

mi_funcion2(nombre="Pepito", apellido="Perez")

""" Funciones con argumentos arbitrarios y con clave """
def mi_funcion3(**kwargs):
    print(kwargs)

mi_funcion3(nombre="Pepito", apellido="Perez", edad=30)