from flask import Flask, request, jsonify
from controladores.controlador_tarea import ControladorTarea

app = Flask(__name__)
controlador = ControladorTarea()

@app.route('/crear', methods=['POST'])
def crear_tarea():
    datos = request.json
    titulo = datos.get('titulo')
    descripcion = datos.get('descripcion')
    tarea = controlador.crear_tarea(titulo, descripcion)
    return jsonify({'tarea': tarea.to_dict()})

@app.route('/listar', methods=['GET'])
def listar_tareas():
    tareas = controlador.listar_tareas()
    # Convertir cada tarea a un diccionario utilizando el método 
    tareas_dict = [tarea.to_dict() for tarea in tareas] 
    return jsonify({'tareas': tareas_dict})

@app.route('/completar-tarea/<int:id_tarea>', methods=['POST'])
def completar_tarea(id_tarea):
    tarea = controlador.completar_tarea(id_tarea)
    if tarea:
        return jsonify({'tarea': tarea.to_dict()})
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
