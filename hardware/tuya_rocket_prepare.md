# 🛠️ Hardware-Vorbereitungen

## 🧪 Tuya W2839: Modifikation für die Datenkommunikation

Um das preiswerte Messgerät für ORP und pH mit unserem ESP32 (Astra Controller) kompatibel zu machen, sind zwei wesentliche Schritte notwendig.

### 1. Rückbau der Laststeckdosen (Sicherheitsaspekt) ⚠️

Nach genauerer Betrachtung der internen Verarbeitung stufen wir die schaltbaren Steckdosen als potenziell unsicher ein. Daher entfernen wir diese komplett:

* **Kabel trennen:** Schneide das Zuleitungskabel der Steckdosen nah am Gehäuse der **Steckdosen** ab.
* **Adern vorbereiten:** Nach dem Abisolieren kommen vier Adern zum Vorschein (Gelb, Grün, Blau, Rot).
* **Sichern:** Die Adern **Gelb** und **Grün** werden jeweils einzeln mit **Wago-Klemmen (Serie 221)** gesichert.
* **Konfektionieren:** Die Adern **Rot (Phase)** und **Blau (Neutralleiter)** werden abisoliert und fachgerecht mit **Aderendhülsen (0,50 mm²)** versehen.

> **Das Ergebnis der Modifikation:**

<img width="900" height="581" alt="image" src="https://github.com/user-attachments/assets/52359c3a-3777-42a7-82f0-2b07ed8b3e06" />



### 2. Datenleitungen herausführen 🔌

Damit der Controller die Messwerte auslesen kann, müssen wir direkt auf die Platine zugreifen:

<img width="430" height="259" alt="image" src="https://github.com/user-attachments/assets/b265af57-380a-432c-b12c-c6b958d7e6f2" />


* **Gehäusebearbeitung:** Öffne das Gehäuse des W2839 und fräse mit einem Dremel oder einem ähnlichen Werkzeug eine kleine Durchführung für die Kabel.
* **Lötarbeiten:** Löte drei Kabel an die Kontakte **TX**, **RX** und **GND**. Achte auf eine saubere Zugentlastung.
* **Heißklebe:** Wenn verfügbar nutze eine Heißklebepistole um die Kabel zu fixieren


> **Das Ergebnis der Modifikation:**
<img width="450" height="800" alt="image" src="https://github.com/user-attachments/assets/473c49e1-72b8-4ade-9712-795fb7c19c9f" />




---

## 🚀 RocketController Astra: Anschluss & Pin-Belegung

Der Astra Controller ist extrem kompakt und vielseitig. Um die wertvollen GPIOs der Hauptklemmleiste für andere Funktionen frei zu halten, nutzen wir für den Tuya W2839 die Pins im Gehäusedeckel.

<img width="900" height="909" alt="image" src="https://github.com/user-attachments/assets/0c3790b4-3817-43dc-a785-855c37f3ff15" />


### Montage und Verkabelung

* **Gehäuseöffnung:** Bohre vorsichtig ein Loch in die Seite des Astra-Gehäuses.
* **Verkabelung:** Führe drei Dupont-Kabel (idealerweise in den gleichen Farben wie am Tuya) durch die Öffnung.
* **Pin-Mapping:** Verbinde die Kabel im Deckel des Controllers nach folgendem Schema:
* **GND** an **GND**
* **TX (Tuya)** an **RX (Astra - GPIO 03)**
* **RX (Tuya)** an **TX (Astra - GPIO 01)**


> **Fertiger Aufbau des Controllers:**
<img width="757" height="708" alt="image" src="https://github.com/user-attachments/assets/17dc3aa1-cdce-4c9a-a918-bf68d94ccff1" />

<img width="1269" height="502" alt="image" src="https://github.com/user-attachments/assets/5fa6dcdc-ed59-4737-8266-ef5ce4d7c40f" />

---

