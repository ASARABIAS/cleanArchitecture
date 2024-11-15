from pinguino import Pinguino
from ave_voladora import AveVoladora
# Uso
if __name__ == "__main__":
    pinguino = Pinguino()
    golondrina = AveVoladora()
 
    # Uso polimrfico del mtodo moverse
    print(f"Pingino: {pinguino.moverse()}")
    print(f"Golondrina: {golondrina.moverse()}")
