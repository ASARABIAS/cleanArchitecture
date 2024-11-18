class CalculadoraSalario: 
    def calcular_salario(self, empleado, horas_extras): 
        try: 
            salario = empleado.salario_base + (horas_extras * 20) 
            return salario 
        except TypeError: print("Error: Asegúrate de que las horas extras sean un número.") 
        return None