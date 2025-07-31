from flask import Flask, request, jsonify

app = Flask(__name__)  # <-- nombre exacto: app

@app.route('/notificar', methods=['POST'])
def notificar():
    data = request.json
    nombre = data.get("nombre", "desconocido")
    return jsonify({"notificacion": f"Se notificó a {nombre} exitosamente."})
