usuario = {
    "id": 1,
    "nombre": "Pepito",
    "edad": 30,
    "direccion": "Avenida los Girasoles",
    "estaCasado": False,
}
# print(usuario)

""" Constructor de diccionarios """
usuario2 = dict(id=2, nombre="Juanito", edad=25, direccion="Calle los Pinos", estaCasado=True)
# print(usuario2)

""" Iterar sobre diccionarios """
# for clave in usuario:
    # print(clave, usuario[clave])

# for clave, valor in usuario.items():
    # print(clave, valor)

""" Modificar diccionarios """
usuario["nombre"] = "Miguelito"

""" Agregar elementos a diccionarios """
usuario["email"] = "miguelito@gmail.com"

""" Eliminar elementos de diccionarios """
del usuario["email"]
usuario.pop("direccion")

""" Métodos de diccionarios """
print(usuario.keys()) # Devuelve una lista de claves
print(usuario.values()) # Devuelve una lista de valores
print(usuario.items()) # Devuelve una lista de tuplas (clave, valor)
print(usuario.copy()) # Devuelve una copia del diccionario
# print(usuario.clear()) # Limpia el diccionario
print(usuario.get("estado", False)) # Devuelve el valor de la clave "id"
usuario.update({"nombre": "Luis", "direccion": "Avenida la Marina"}) # Actualiza el diccionario
print(usuario)