""" Ejemplos """
numero = 10
texto = "Hola mundo!"

""" Cambiar el valor de una variable """
# numero = "Pepito"

""" Obtener el tipo de una variable """
tipo = type(numero)

""" Casting """
nuevo_numero = str(numero)
entero = int(nuevo_numero)
flotante = float(entero)

""" Nombrar variables """
nombreUsuario = "Pepito"
nombre_usuario = "Pepito"
_nombreUsuario = "Pepito"
NOMBRE_USUARIO = "Pepito"
nombre_usuario_2 = "Pepito"

""" Asignar multiples valores """
a, b, c = 1, "Hola", True
a = b = c = 1
letras = ["Hello", 100, True]
d, e, f = letras
print(d, e, f)