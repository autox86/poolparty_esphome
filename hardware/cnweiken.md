# 🛠️ Hardware-Vorbereitungen

## 🔌 CNWeiken WD600k 2,2kw - 230V 1-Phasig

Der Frequenzumrichter von CNWeiken ist ein leistungsstarkes Werkzeug, besonders wenn man die geringen Anschaffungskosten betrachtet. Er arbeitet zuverlässig im manuellen Modus sowie über Modbus RS485-Steuerung. Da die mitgelieferte Dokumentation nicht alle Details abdeckt, sind die folgenden Einstellungen entscheidend, um den Umrichter korrekt für beide Betriebsarten zu konfigurieren.

### ⚙️ Menüführung und Bedienung

Um die Parameter des Umrichters anzupassen, nutzen Sie die Tasten am Bedienpanel wie folgt:

* **PRG / ECS:** Öffnet das Programmier-Menü oder kehrt zur vorherigen Ebene zurück.
* **RD / WT:** Bestätigt die Auswahl eines Untermenüs oder speichert einen geänderten Wert.
* **Pfeiltasten (Hoch/Runter):** Navigieren durch die Menüpunkte oder ändern die Werte der Parameter.

**Beispiel für die Einstellung (P0-20 auf 20 setzen):**
Drücken Sie `PRG` -> wählen Sie `P0` -> `RD/WT` -> nutzen Sie die Pfeiltasten bis `P0-20` erscheint -> `RD/WT` -> Wert auf `20` anpassen -> mit `RD/WT` bestätigen.

Hier auch ein Video des Herstellers: [VFD Single Phase 220V Input and Output Frequency Converter Drives For Single-Phase 220V Motor](https://www.youtube.com/watch?v=KAJoE-C64vI&t=2s)

<br>

> ***Hinweis:** Der WD600k ist in der Lage, wie folgt betrieben zu werden:*
> * **1-phasiger Input / 1-phasiger Output**
> * **1-phasiger Input / 3-phasiger Output**
> * **3-phasiger Input / 3-phasiger Output** *(Warte auf Bestätigung des Herstellers, dass keine Hardware-Änderungen erforderlich sind)*
> 
> 
> *Diese Konfiguration gilt nur für: **1-phasiger Input / 1-phasiger Output***

<br>

---

## 📋 Zielsetzung der Konifguration

### Betriebsmodi des Frequenzumrichters (WK600)

---

#### 0. Status der "LOC/REM" LED

| LED Status | Modus | Beschreibung |
| --- | --- | --- |
| **Leuchtet** | **AUX Aktiv** | Schalter X3/X4 aus. Steuerung über X5 (Start/Stopp) + Poti möglich. |
| **Blinkt** | **Modbus Aktiv** | Schalter X3+X4 an DCOM an. Steuerung nur über Modbus. Bedienfeld inaktiv (außer Stopp). |
| **Aus** | **Bedienfeld Aktiv** | Aktiviert durch Taste `MF. K / REV`. Poti aktiv, Aux/Modbus inaktiv. |



#### 1. Manueller Betrieb (Externer Schalter)

Dieser Modus wird verwendet, wenn du die Pumpe direkt am Poolhaus steuern möchtest.

* **Voraussetzung:** **Schalter 1 (Automatik Modus)** ist **AUS** (X3 + X4 gegen DCOM geschlossen).
* **Funktion:** Die Steuerung wird vom Modbus auf die lokalen Terminals gelegt.
* **Bedienung:** Mit **Schalter 2 (X5)** schaltest du die Pumpe ein oder aus. Die Drehzahl wird über das Poti am Bedienfeld gesteuert, sollte aber ganze rechts sein und damit auf 50hz.

---

#### 2. Automatik-Betrieb (Modbus / Home Assistant)

Dieser Modus ist für den normalen Alltagsbetrieb über deine Hausautomatisierung vorgesehen.

* **Voraussetzung:** **Schalter 1 (Automatik Modus)** ist **AN** (X3 + X4 offen).
* **Funktion:** Der Umrichter akzeptiert Befehle und Frequenzvorgaben über die **Modbus-Schnittstelle**.
* **Bedienung:** Die Pumpe wird über Home Assistant (ESPHome) gesteuert. Schalter 2 hat in diesem Zustand keine Funktion.

---

#### 3. Lokal-Betrieb (Bedienfeld am Gerät)

Dieser Modus ist zum steuern am Bedienteil vorgesehen, z.B. wenn man keine externen Schalter braucht.

* **Voraussetzung:** Schalter 1 und Schalter 2 sind **AUS**.
* **Aktivierung:** Drücke einmalig die Taste **`MF. K / REV`**.
* **Funktion:** Der Umrichter wechselt in den "Local"-Modus (erkennbar an der LED am Display).
* **Bedienung:** Die Pumpe wird nun über die grünen **RUN** und roten **STOP** Tasten am Bedienfeld gestartet und gestoppt.

---

## 🛠 Grundparameter für die Steuerung

| Parameter | Wert | Bedeutung |
| --- | --- | --- |
| **P0-01** | 2 | Motor Control Mode to V/F |
| **P0-02** | 1 | Command Source: Terminal |
| **P0-03** | 4 | Frequenzeinstellung (Source X) |
| **P0-04** | 9 | Wählbare Frequenzeinstellung über einen AUX Eingang (Source Y) |
| **P0-07** | 2 | Frequenzquelle soll entweder Source X oder Source Y sein |
| **P0-08** | 50 | Voreingestellte Frequenz |
| **P0-10** | 50 | Maximale Frequenz |
| **P0-11** | 0 | Source = P0-12 |
| **P0-17** | 00.20 | Acceleration Time = 0.2s |
| **P0-18** | 03.00 | Deceleration Time = 3s |
| **P0-19** | 2 | Acceleration/Deceleration Time Unit = 0.01s |
| **P0-20** | 20 | **Undokumentiert:** Für Single Phase zwingend notwendig! |
| **P1-00** | 4 | **Undokumentiert:** Single Phase 230V bei max. Frequenz |
| **P1-01** | 1.1 | Leistungsaufnahme der Pumpe in kW |
| **P1-02** | 230 | Nennspannung in Volt |
| **P1-03** | 5.1 | Stromaufnahme der Pumpe in Ampere (**Wichtigster Wert!**) |
| **P1-04** | 50.00 | Nennfrequenz in Hz |
| **P1-05** | 2850 | Nenndrehzahl bei 100% (U/min) |
| **P3-01** | 6 | Torque Boost (Spannungserhöhung bei kleinen Frequenzen) |
| **P3-02** | 20 | CutOff Torque Boost (Frequenzgrenze für Boost) |
| **P4-00** | 12 | X1 = Pc-02=75 (entspricht 37,5 Hz) |
| **P4-01** | 13 | X2 = Pc-02=55 (entspricht 27,5 Hz) |
| **P4-02** | 37 | X3 = Switch von Aux zu Modbus |
| **P4-03** | 18 | X4 = Frequenzquelle ändern |
| **P4-04** | 1 | X5 = Start (forward) / Pc-00=100 (entspricht 50 Hz) |
| **P4-05** | 0 | X6 = Stopp (reverse) |
| **P6-00** | 0 | Start Mode: Immer sofort |
| **P6-03** | 010 | Startup Frequenz max. 10Hz |
| **P7-01** | 1 | MF.K Key - Wechsel zwischen AUX/Modbus und Bedienfeld |
| **P7-02** | 1 | Stopp Key in allen Modi aktiv |
| **P9-08** | 410 | Unbekannter Parameter (von 380 auf 410V) - hilft bei Startproblemen |

<img width="1007" height="1780" alt="image" src="https://github.com/user-attachments/assets/d00a5ccb-ef25-49ae-acfc-2a314f6543eb" />

<img width="1097" height="196" alt="image" src="https://github.com/user-attachments/assets/16ddd29d-5e99-498b-ad30-5037f5896e42" />

<img width="987" height="1442" alt="image" src="https://github.com/user-attachments/assets/8744bfac-b153-420d-80fd-afd331ee6606" />

<img width="996" height="1204" alt="image" src="https://github.com/user-attachments/assets/0c38c035-ffb3-49e7-b21c-2eed90e6a848" />

<img width="997" height="530" alt="image" src="https://github.com/user-attachments/assets/e7bac217-46e1-4b15-b49c-6cde2cc06269" />

---
<br><br>

<img width="997" height="728" alt="image" src="https://github.com/user-attachments/assets/66487942-6fdd-485a-8212-8f1182191ba4" />

## Hardware Modifikation

Da der Lüfter extremst laut war, habe ich diesen gegen einen Noctua NF-A4x10 24V PWM 40x40x10 Lüfter getauscht

Ein Bild vom Innenleben mit altem Lüfter:
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/cab2e7f3-5910-49a5-9c3a-756836755386" />












