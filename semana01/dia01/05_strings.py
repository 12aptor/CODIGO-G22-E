""" Strings """
texto = "Python es un lenguaje de programación"
otro_texto = "Rust es un lenguaje de programación"

""" Recorrer una cadena """
# for caracter in texto:
#     print(caracter)

""" Concatenar cadenas """
texto = texto + " muy popular"
# print(texto)

""" Formatear cadenas """
nombre = "Pepito"
edad = 50
saludo = "Hola {}, tu edad es {}".format(nombre, edad)
segundo_saludo = f"Hola {nombre}, tu edad es {edad}"
tercer_saludo = "Hola %s, tu edad es %d" % (nombre, edad)

""" Métodos de cadena """

""" Mayúsculas """
print(texto.upper())

""" Minúsculas """
print(texto.lower())

""" Capitalización (primera letra en mayúscula) """
print(texto.capitalize())

""" Ocurrencias """
print(texto.count("programación"))

""" Encontrar la posición """
print(texto.find("programación"))

""" Reemplazar """
print(texto.replace("o", "0"))

""" Separar "Hola mundo".split(" ") => ["Hola", "mundo"] """
print(texto.split(" "))

""" Eliminar espacios " Hola mundo " => "Hola mundo" """
print(" Hola mundo ".strip())

""" Comprobar si es un número """
print(texto.isdigit())

""" Comprobar si es alfabético """
print(texto.isalpha())