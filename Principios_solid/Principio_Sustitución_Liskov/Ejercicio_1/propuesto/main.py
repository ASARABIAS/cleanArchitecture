from pinguino import Pinguino

# Uso
if __name__ == "__main__":
    pinguino = Pinguino()
    try:
        pinguino.mostrar_sonido()
    except NotImplementedError as e:
        print(e)
