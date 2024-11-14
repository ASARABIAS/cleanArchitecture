from descuentoEnum import DescuestoEnum

class CalculadoraDescuento:
    
    @staticmethod
    def calcular(tipo_cliente, monto):
        return monto * (1.0 - DescuestoEnum.obtener(tipo_cliente))