class CalculadoraDescuento:
    def calcular(self, tipo_cliente, monto): # el metodo estatico
        if tipo_cliente == "estudiante":
            return monto * 0.8 # 20% de descuento
        elif tipo_cliente == "senior":
            return monto * 0.7 # 30% de descuento
        elif tipo_cliente == "regular":
            return monto * 0.9 # 10% de descuento
        else:
            return monto # Sin descuento
# Uso
if __name__ == "__main__":
 calculadora = CalculadoraDescuento()
 total = calculadora.calcular("estudiante", 100)
 print(f"Total con descuento: {total}")

 #¿Cómo podrías modificar este diseño para permitir la extensión de los tipos de descuento sin necesidad de modificar la clase CalculadoraDescuento?
 #Lo podriamos implementar por una clase Emun DescuentosEmun donde de indique dos propiedades como son tipoCliente y porcentaje de descuento

 #Considera el uso de clases específicas para cada tipo de descuento que puedan ser utilizadas por CalculadoraDescuento.
 #trambien seria un buena estrategia

