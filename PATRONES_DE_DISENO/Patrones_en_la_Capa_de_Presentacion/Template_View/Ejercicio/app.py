from flask import Flask, render_template
from modelo.cliente_modelo import Cliente, ClienteModelo

app = Flask(__name__)

# Crear una instancia del modelo
modelo = ClienteModelo()

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/clientes')
def lista_clientes():
    clientes = modelo.obtener_clientes()
    print("Clientes en el sistema:", clientes)  # Para verificar si los clientes están cargados
    return render_template('lista_clientes.html', clientes=clientes)

@app.route('/cliente/<int:id_cliente>')
def detalle_cliente(id_cliente):
    cliente = modelo.obtener_cliente_por_id(id_cliente)
    if cliente:
        return render_template('detalle_cliente.html', cliente=cliente)
    else:
        return "Cliente no encontrado", 404

if __name__ == '__main__':
    # Cargar algunos datos iniciales
    print("Cargando clientes iniciales...")
    modelo.agregar_cliente(Cliente(1, "Rodrigo Silva", "rodrigo@example.com", "+56 9 1234 5678"))
    modelo.agregar_cliente(Cliente(2, "Maria Lopez", "maria@example.com", "+56 9 8765 4321"))
    print("Clientes cargados:", modelo.obtener_clientes())
    # Iniciar la aplicación Flask
    app.run(debug=True, port=5013)
