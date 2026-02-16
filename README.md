# 🙏 Danksagung / Credits 
Ein Projekt wie dieses entsteht selten im Alleingang. Mein besonderer Dank gilt:

**Udo:** Für seinen stetigen Support, besonders in den schwierigen Phasen. Ein wahrer Lehrmeister, der Hilfe zur Selbsthilfe perfekt beherrscht! 🎓

**xxx:** Dein Code war das Fundament und die Inspiration für die gesamte Software-Entwicklung dieses Projekts. 🚀

**@hostcc:** Many thanks for the [esphome-component-dynamic-on-time](https://github.com/hostcc/esphome-component-dynamic-on-time). This dynamic time component made it incredibly easy to use the controller even without Home Assistant! ⏱️

**OpenAI (ChatGPT) & Google (Gemini)**: Ein großes Dankeschön an die Entwickler dieser KIs. Ohne diese Unterstützung wäre die Software in dieser Form nie entstanden. 🤖

---

# 🏊 DIY Pool-Steuerung mit ESPHome

Dieses Projekt ist der Versuch, eine vollautomatische Poolsteuerung auf Basis von **ESPHome** zu erstellen.

Der Controller ist so „codiert“, dass er **völlig autark** und unabhängig von einer Hausautomation (z.B. Home Assistant) funktioniert.

---

### 📑Detaillierte Informationen

Detaillierte Informationen sind unter folgenden Links zu finden:

* **[Die Hardware](https://github.com/autox86/poolparty_esphome/blob/main/hardware/readme.md)**
  * [BOM (Bill of Material)](https://github.com/autox86/poolparty_esphome/blob/main/hardware/bom.md)
  * [Anschlussplan, Eklärung und schematischer Aufbau DC / AC](https://github.com/autox86/poolparty_esphome/blob/main/hardware/wiring.md)
  * [Vorbereitung des Tuya W2839 & Rocketcontroller Astra](https://github.com/autox86/poolparty_esphome/blob/main/hardware/tuya_rocket_prepare.md)
  


* **[Die Software](https://github.com/autox86/poolparty_esphome/blob/main/software/readme.md)**
  * Ablaufplan
  * Sensoren
  * Sicherheitsfunktionen
  * Betriebsmodi
  * Webserver UI


* **[Handbücher der Komponenten](https://github.com/autox86/poolparty_esphome/blob/main/manuals/readme.md)**

---

## 🏛️ Highlevel Aufbau

<img width="1458" height="874" alt="image" src="https://github.com/user-attachments/assets/df9cd9b8-b4b7-45e0-bbb4-2964d131ecc5" />


---

## 🛠 Komponenten

| Komponente | Modell | Funktion | Protokoll/Anschluss |
| --- | --- | --- | --- |
| **Frequenzumrichter** | CNWeiken WK600D – 0022 – M1T | Steuerung der Poolpumpe (Frequenz) | Modbus RS485 |
| **Messgerät ORP/PH** | Tuya W2839 Watercontroller | Messung von pH, ORP und Temperatur | UART Serial (RX/TX) |
| **Energiemesser (DC)** | PEACEFAIR PZEM-017 | Überwachung der Salzelektrolyse (DC), Erkennung von Low Salt | Modbus RS485 |
| **Durchflussmesser** | YF-DN40 / S201 | Durchflussmessung Hauptstrom & Messzelle | Pulse Counter (GPIO) |
| **H-Brücke** | Display3000 D-PHB02-Opto | Professionelle H-Brücke zum Schalten und Umpolen der Salzelektrolyse | Output (GPIO 3,3V) |
| **Relais** | Eltako Relais (1 oder 2 Kanal) | Zum Schutz des Controllers werden Dauerströme über Eltako geschaltet | Stromstoß (200-250ms) |
| **Salzelektrolysezelle** | Zodiac LM2-40 | Salzelektrolysezelle für 40g/h | 24V Gleichstrom |
| **Netzteil 24V 10A** | Meanwell NDR – 240-24 | Spannungversorgung für Salzelektrolyse und Energiemesser | 230V In / 24V Out |
| **PH Pumpe** | *XxX* | Pumpe für PH Minus | 230V Relaisausgang |
| **Poolcontroller (ESP32)** | Rocketcontroller Astra (inkl. RS485) | Steuereinheit aller Funktionen | 230V |
| **Wärmepumpe** | Sunrain BYC035 TE3 | 3 Phasen 35KW Wärmepumpe | Modbus RS485 |

---

## ⚙️ Betriebsmodi (Work Modes)

Die Steuerung verfügt über vordefinierte Modi, die sowohl die Frequenz als auch die Sicherheitsfreigaben für Chemie steuern:

* **55% Stromsparen:** Niedriger Durchfluss, Chemie aktiv.
* **70% / 85% / 100% Badebetrieb:** Erhöhter Durchfluss für optimale Filterung.
* **0% Wartung:** Alles AUS, Skripte gestoppt, Dosierung gesperrt.
* **55% Winterbetrieb:** Frostschutzlauf, Chemie & Tuya-Sensoren deaktiviert.

---

## 🛡 Sicherheitslogik (Interlocks)

Die Dosierung (pH / Chlor) ist softwareseitig mehrfach abgesichert:

* **Pumpen-Check:** Grundvoraussetzung ist ein Status-Check des Frequenzumrichters und (wenn installiert) ein Durchflusscheck.
* **Watchdog:** Wir verlassen uns nicht auf angenommene Zustände, sondern validieren diese kontinuierlich.

---

## 📊 Übersicht: Sensor- und Schaltmöglichkeiten

* Frequenzsteuerung (Modbus Register)
* Energiemesser (Modbus Register)
* Chemische Werte (Tuya W2839)
* Salzelektrolyse (Zodiac LM2-40) – Ansteuerung über H-Brücke
* Durchflusssensoren für Pumpe und Messzelle (YF-DN40 / S201)
* Temperaturmessung (DS18B20 OneWire)
* PH-Dosierpumpe (230V Relais)
* Schalter für Wartungsmodus
* Taster für PH Tank Reset (nach Auffüllen)

---

## 🚀 Installation

1. Erstelle eine neue Datei `poolcontroller.yaml` in deinem ESPHome Verzeichnis.
2. Kopiere den Code aus der Config-Datei hinein.
3. Passe die **Substitutions** an deine Wünsche an.
*(Tipp: Siehe [ESPHome Secrets Guide](https://esphome.io/guides/yaml/#secrets-and-the-secretsyaml-file))*
```yaml
substitutions:
  device_name: "poolcontroller"
  friendly_name: "Pool"
  friendly_name_entity: "#"
  domain: !secret domain
  ssid1_ap: !secret wifi_ssid
  ssid1_pw: !secret wifi_pass

```


4. Flashe den ESP32 (OTA, ESPHome Web Flasher etc.).
