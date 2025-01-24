""" Programación orientada a objetos """
""" Un objeto tiene atributos y métodos """

class Persona:
    """ Constructor """
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo # Atributo privado (Encapsulamiento)

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    """ Métodos privados (Encapsulamiento) """
    def __mostrar_saldo(self):
        print(f"Mi saldo es {self.__saldo}")

""" Instancia de la clase """
pepito = Persona("Pepito", 30, 100)
print(pepito.nombre, pepito.edad)
pepito.saludar()

""" Herencia """
class Alumno(Persona):
    def mostrar_notas(self):
        print(f"Las notas son aprobatorias")

alumno = Alumno(nombre="Miguel", edad=20, saldo=100)
alumno.saludar()
alumno.mostrar_notas()

""" Polimorfismo """
juanito = Persona(nombre="Juanito", edad=25, saldo=500)

def hablar(estudiante):
    estudiante.saludar()

hablar(juanito)

""" Abstracción: Consiste en enfocarse en los aspectos esenciales de un objeto
ignorando los detalles irrelevantes para su uso  """