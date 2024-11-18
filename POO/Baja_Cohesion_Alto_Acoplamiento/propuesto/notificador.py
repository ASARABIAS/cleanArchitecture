class Notificador: 
    def enviar_notificacion(self, empleado, mensaje): 
        if isinstance(mensaje, str): 
            print(f"Enviando notificación a {empleado.nombre}: {mensaje}") 
        else: 
            print("Error: El mensaje debe ser una cadena de texto.")