""" Crear un juego de adivinanza de números. EL programa debe generar un número
aleatorio entre 1 y 10 y luego debe ayudarte con ES MENOR y ES MAYOR """

import random

def adivinar():
    numero_aleatorio = random.randint(1, 10)
    intentos = 0
    print("¡Bienvenido a la adivinanza!")
    print("Estoy pensando en un numero entre 1 y 10, intenta adivinarlo")

    while True:
        resultado = int(input(f"Adivina el número: "))
        intentos += 1

        if numero_aleatorio == resultado:
            print(f"Felicidades, has adivinado en el intento {intentos}")
            break
        elif resultado < numero_aleatorio:
            print("El número es mayor")
        else:
            print("El número es menor")

# adivinar()


""" Crear un generador de contraseñas seguras. El
programa debe pedir la longitud de la contraseña """

import string

def generar_contrasena():
    longitud = int(input("Ingresa la londitud de la contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)

    print(f"Tu contraseña segura es: {contrasena}")


generar_contrasena()