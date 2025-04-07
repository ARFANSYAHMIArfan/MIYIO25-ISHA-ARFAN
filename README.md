PETI AIS PINTAR 101 (MIYIO 2025)

✅ 1. Hardware Setup
🧠 Komponen:
Raspberry Pi 3/4/5 + microSD card

DHT11/DHT22 sensor (suhu + kelembapan)

Kamera (PiCam atau USB)

Magnetic door sensor (optional)

Power supply

Telefon lama (untuk jadi skrin)

Breadboard + jumper wires

⚙️ 2. Wiring Sensor DHT11/DHT22
Guna 3 pin (jika pakai DHT22):

VCC → 5V Raspberry Pi (pin 2)

DATA → GPIO pin (cth: GPIO4 - pin 7)

GND → Ground Raspberry Pi (pin 6)


💻 3. Software - Backend Setup (Python + Flask)
📦 Install ke Raspberry Pi: [bashdownload.txt]
Kod Flask (backend.py)


🌐 4. Frontend (Dashboard UI) - HTML + JS

![image](https://github.com/user-attachments/assets/93711d9b-1106-4054-bdac-51e17d4ee0d8)

📱 5. Jadikan Telefon Sebagai Display
🅰️ Cara paling senang: Guna browser + WiFi
Connect phone & Pi ke WiFi sama

Jalankan Flask (python3 backend.py)

Buka browser phone dan pergi ke http://<IP-RaspberryPi>:5000

Letak shortcut ke homescreen → full screen kiosk mode

💡 Optionally boleh install Android kiosk app kalau nak tutup semua bar/menu


![image](https://github.com/user-attachments/assets/d076cb3d-a536-46da-a06c-31a0f0536fe9)


![image](https://github.com/user-attachments/assets/65fe971f-bbbc-46b1-b02c-cda66b4624e8)

