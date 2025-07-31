from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notificar', methods=['POST'])
def notificar():
    data = request.json
    nombre = data.get("nombre", "desconocido")
    print(f"📨 Notificando a {nombre}...")
    return jsonify({
        "notificacion": f"Se notificó a {nombre} exitosamente."})

# 👇 Importante: no pongas app.run() aquí
