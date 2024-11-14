from enum import Enum

class DescuestoEnum(Enum): 
    ESTUDIANTE = ("estudiante", 0.2) 
    SENIOR = ("senior", 0.3) 
    REGULAR = ("regular", 0.1)

    @staticmethod
    def obtener(tipo_cliente):
        for descuento in DescuestoEnum:
            if descuento.value[0] == tipo_cliente:
                return descuento.value[1]
        return 0.0