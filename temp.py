
import Adafruit_DHT
from flask import Flask, jsonify
import time

# Configurações do sensor
DHT_SENSOR = Adafruit_DHT.DHT11  # Ou Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO onde o sensor está conectado

app = Flask(__name__)

def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return {'temperature': round(temperature, 2), 'humidity': round(humidity, 2)}
    return {'error': 'Falha na leitura do sensor'}

@app.route('/data', methods=['GET'])
def data():
    return jsonify(get_sensor_data())

@app.route('/')
def index():
    return "<h1>Monitor de Temperatura e Umidade</h1><p>Acesse /data para ver os dados.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
