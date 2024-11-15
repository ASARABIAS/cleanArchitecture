from desarrollador import Desarrollador
from gerente import Gerente
# Uso
if __name__ == "__main__":
    desarrollador = Desarrollador()
    gerente = Gerente()
 
    print(desarrollador.trabajar())
    print(desarrollador.tomar_descanso())
 
    print(gerente.trabajar())
    print(gerente.tomar_descanso())
    print(gerente.reportar())
