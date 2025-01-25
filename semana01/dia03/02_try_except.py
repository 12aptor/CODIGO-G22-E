""" Manejo de excepciones con try y except """
""" La finalidad de las excepciones es manejar errores de forma controlada """

# division = 10 / 0

def main():
    try:
        """ Todo lo que esté dentro del bloque try será ejecutado
        y si se produce un error, se ejecutará el bloque except """
        division = 10 / 0
    
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    except Exception as e:
        print("Exception:", e)
    finally:
        """ Este bloque se ejecutará siempre, incluso si se produce un error """
        print("Completado")

# main()

def evaluar_edad(edad):
    try:
        if edad < 18:
            raise Exception("Edad insuficiente")

        print("Usuario autorizado")
    except Exception as e:
        print("Error:", e)

evaluar_edad(edad=15)