""" Crear un programa que simule el funcionamiento de un cajero automático.
Deberá tener un menú con las siguiente opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar saldo disponible
Iniciar con un saldo de $1000 """

class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad no válida")
            return
        self.saldo += cantidad
        print("Depósito realizado")
        self.mostrar_saldo()

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad no válida")

        if cantidad > self.saldo:
            print("Saldo insuficiente")
        
        self.saldo -= cantidad
        print("Retiro realizado")
        self.mostrar_saldo()

    def mostrar_saldo(self):
        print(f"Saldo disponible: {self.saldo}")

def main():
    cajero_bcp = Cajero(saldo=1000)

    while True:
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = int(input("\nIngresa una opción: "))

        if opcion > 4:
            print("Opción no válida")
            continue
        elif opcion == 1:
            cajero_bcp.mostrar_saldo()
        elif opcion == 2:
            monto = float(input("¿Cuánto quieres depositar?: "))
            cajero_bcp.ingresar(monto)
        elif opcion == 3:
            monto = float(input("¿Cuánto quieres retirar?: "))
            cajero_bcp.retirar(monto)
        elif opcion == 4:
            print("Gracias por visitarnos")
            break

main()