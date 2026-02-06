# 🏊 Pool-Steuerung ESPHome (VFD, Tuya, Modbus)

Dieses Repository enthält die Konfiguration für eine intelligente Pool-Steuerung basierend auf ESPHome. Es steuert einen Frequenzumrichter (FU), überwacht Wasserwerte via Tuya und misst den Durchfluss sowie den Energieverbrauch.

## 🛠 Features & Komponenten

| Komponente | Funktion | Protokoll/Anschluss |
| :--- | :--- | :--- |
| **VFD (Mr. WU)** | Steuerung der Poolpumpe (Frequenz/Modus) | Modbus RS485 |
| **Tuya W2839** | Messung von pH, ORP und Temperatur | Tuya Serial |
| **PZEM-017** | Überwachung der Salzelektrolyse (DC) | Modbus RS485 |
| **YF-DN40 / S201** | Durchflussmessung Hauptstrom & Messzelle | Pulse Counter (GPIO) |

---

## ⚙️ Betriebsmodi (Work Modes)

Die Steuerung verfügt über vordefinierte Modi, die sowohl die Frequenz als auch die Sicherheitsfreigaben für Chemie steuern:

* **35% Stromsparen:** Niedriger Durchfluss, Chemie aktiv.
* **57% - 100% Badebetrieb:** Erhöhter Durchfluss für optimale Filterung.
* **0% Wartung:** Alles AUS, Skripte gestoppt, Dosierung gesperrt.
* **35% Winterbetrieb:** Frostschutzlauf, Chemie & Tuya-Sensoren deaktiviert.

---

## 🛡 Sicherheitslogik (Interlocks)

Die Dosierung (pH / Chlor) ist softwareseitig mehrfach abgesichert:
1.  **Pumpen-Check:** Nur wenn `poolpump_ok` wahr ist.
2.  **Durchfluss-Check:** Validierung über die Flow-Sensoren.
3.  **Watchdog:** Tuya-Werte werden nur akzeptiert, wenn sie ungleich 0 und keine NaNs sind.

> [!IMPORTANT]
> Ein pH-Wert unter 1.0 oder ein "eingefrorener" Tuya-Wert führt zum sofortigen Stopp der Dosierung via Watchdog-Timer.

---

## 📊 Sensor-Übersicht (Auszug)

### Modbus Register (Inverter)
- **0x1001**: Aktuelle Frequenz ($Hz$)
- **0x1007**: Drehzahl ($U/min$)
- **0x2000**: Start/Stop Kommando

### Chemische Werte
- **pH-Wert:** Datapoint 106 (0.01 Multiplikator)
- **ORP:** Datapoint 131 ($mV$)
- **Temperatur:** Datapoint 8 ($°C$)

---

## 🚀 Installation

1. Erstelle eine neue Datei `pool_control.yaml` in deinem ESPHome Verzeichnis.
2. Kopiere den Code aus der Config-Datei hinein.
3. Passe die Substitutions (`friendly_name`, `yfdn40`, etc.) an deine Hardware an.
4. Flashe den ESP32/ESP8266.
