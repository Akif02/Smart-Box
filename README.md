# Raspberry Pi Pico – Smart Box 

Dieses Projekt verwandelt eine gewöhnliche Kiste oder ein Karton in eine „Smart Box“. Mithilfe eines Ultraschallsensors erkennt der Raspberry Pi Pico, wenn sich eine Hand oder ein Objekt nähert. Daraufhin öffnet ein kleiner Servo-Motor automatisch den Deckel, hält ihn für 3 Sekunden offen und schließt ihn danach wieder.

## 🎥 Projekt-Demo

https://github.com/user-attachments/assets/7707544b-b448-4aed-b2cc-13e65c8e877e

---

## 🌟 Features
* **Berührungslose Steuerung:** Öffnet sich automatisch per Ultraschall-Erkennung.
* **Auto-Close:** Schließt den Deckel selbstständig nach 3 Sekunden.
* **Anpassbarer Radius:** Die Erkennungsdistanz (aktuell 15 cm) kann im Code leicht geändert werden.
* Basiert auf MicroPython.

## 🛠 Hardware-Anforderungen
* Raspberry Pi Pico (oder Pico W)
* HC-SR04 Ultraschallsensor
* SG90 Micro-Servo (9g)
* Jumper-Kabel 
* Eine Kiste oder ein selbstgebastelter Karton

## 🔌 Verkabelung

Alle Bauteile werden schonend über den 3,3V-Ausgang des Raspberry Pi Picos mit Strom versorgt.

### HC-SR04 (Ultraschallsensor)
| Sensor Pin | Pico Pin |
| :--- | :--- |
| **VCC** | **3V3 (Pin 36)** |
| **GND** | **GND** |
| **TRIG** | **GPIO3** |
| **ECHO** | **GPIO2** |

### SG90 (Servo-Motor)
| Servo Kabel | Pico Pin |
| :--- | :--- |
| **Rot (VCC)** | **3V3 (Pin 36)** |
| **Braun/Schwarz (GND)** | **GND** |
| **Gelb/Orange (Signal)**| **GPIO15** |




## 💻 Software & Einrichtung

1. Installiere die MicroPython-Firmware auf deinem Raspberry Pi Pico.
2. Lade dir die [Thonny IDE](https://thonny.org/) herunter.
3. Kopiere den Code und speichere ihn unter dem Namen `main.py` direkt auf dem Pico.
4. Sobald der Pico Strom bekommt, startet das Programm automatisch.

## ⚙️ Funktionsweise des Codes
1. Der HC-SR04 sendet kontinuierlich Ultraschall-Impulse aus, um die Entfernung zu messen.
2. Das Skript wandelt die Laufzeit des Echos in Zentimeter um.
3. Wird ein Objekt näher als 15 cm erkannt, sendet der Pico ein PWM-Signal (Pulsweitenmodulation) an den Servo an GPIO15.
4. Der Servo dreht sich um 90 Grad (Deckel öffnet sich).
5. Nach einem `time.sleep(3)` (3 Sekunden Wartezeit) dreht der Servo zurück auf 0 Grad (Deckel schließt sich).

## 📁 Projektstruktur
```text
smart-box-pico
│
├── main.py
└── README.md
