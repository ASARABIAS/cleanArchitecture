from flask import Flask, render_template, request, redirect, url_for
from controladores.producto_controller import ProductoController

app = Flask(__name__)
controlador = ProductoController()

@app.route('/')
def index():
    productos = controlador.obtener_todos_los_productos()
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        controlador.agregar_producto(nombre, precio, cantidad)
        return redirect(url_for('index'))
    return render_template('agregar_producto.html')

@app.route('/eliminar/<int:id_producto>')
def eliminar_producto(id_producto):
    controlador.eliminar_producto(id_producto)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
