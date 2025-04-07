from flask import Flask, render_template, jsonify
import Adafruit_DHT

app = Flask(__name__)
sensor = Adafruit_DHT.DHT22
pin = 4  # GPIO4

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return jsonify({"temperature": round(temperature, 1), "humidity": round(humidity, 1)})
    else:
        return jsonify({"temperature": "N/A", "humidity": "N/A"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
