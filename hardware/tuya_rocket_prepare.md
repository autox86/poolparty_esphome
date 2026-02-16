# 🛠️ Hardware-Vorbereitungen

## 🧪 Tuya W2839: Modifikation für die Datenkommunikation

Um das preiswerte Messgerät für ORP und pH mit unserem ESP32 (Astra Controller) kompatibel zu machen, sind zwei wesentliche Schritte notwendig.

### 1. Rückbau der Laststeckdosen (Sicherheitsaspekt) ⚠️

Nach genauerer Betrachtung der internen Verarbeitung stufen wir die schaltbaren Steckdosen als potenziell unsicher ein. Daher entfernen wir diese komplett:

* **Kabel trennen:** Schneide das Zuleitungskabel der Steckdosen nah am Gehäuse ab.
* **Adern vorbereiten:** Nach dem Abisolieren kommen vier Adern zum Vorschein (Gelb, Grün, Blau, Rot).
* **Sichern:** Die Adern **Gelb** und **Grün** werden jeweils einzeln mit **Wago-Klemmen (Serie 221)** gesichert.
* **Konfektionieren:** Die Adern **Rot (Phase)** und **Blau (Neutralleiter)** werden abisoliert und fachgerecht mit **Aderendhülsen (0,50 mm²)** versehen.

### 2. Datenleitungen herausführen 🔌

Damit der Controller die Messwerte auslesen kann, müssen wir direkt auf die Platine zugreifen:

* **Gehäusebearbeitung:** Öffne das Gehäuse des W2839 und fräse mit einem Dremel oder einem ähnlichen Werkzeug eine kleine Durchführung für die Kabel.
* **Lötarbeiten:** Löte drei Kabel an die Kontakte **TX**, **RX** und **GND**. Achte auf eine saubere Zugentlastung.

> **Das Ergebnis der Modifikation:**




---

## 🚀 RocketController Astra: Anschluss & Pin-Belegung

Der Astra Controller ist extrem kompakt und vielseitig. Um die wertvollen GPIOs der Hauptklemmleiste für andere Funktionen frei zu halten, nutzen wir für den Tuya W2839 die Pins im Gehäusedeckel.

### Montage und Verkabelung

* **Gehäuseöffnung:** Bohre vorsichtig ein Loch in die Seite des Astra-Gehäuses.
* **Verkabelung:** Führe drei Dupont-Kabel (idealerweise in den gleichen Farben wie am Tuya) durch die Öffnung.
* **Pin-Mapping:** Verbinde die Kabel im Deckel des Controllers nach folgendem Schema:
* **GND** an **GND**
* **TX (Tuya)** an **RX (Astra - GPIO 03)**
* **RX (Tuya)** an **TX (Astra - GPIO 01)**



> **Fertiger Aufbau des Controllers:**


---

Soll ich dir noch die passenden **YAML-Konfigurationszeilen für ESPHome** erstellen, damit die Kommunikation über GPIO 01 und 03 sofort funktioniert?
