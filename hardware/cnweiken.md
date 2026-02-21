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

---

## 📋 Zielsetzung der Konifguration
Wenn der Frequenzumrichter an Strom angeschlossen wird:
1.) Die FU wird durch den externen Schalter bedient
Schalter 1: Schaltet die Poolpumpe an / aus
(Am Schalter 1 ist X5 und DCOM angeschlossen)

2.) Modbus soll die Steuerung übernehmen (Automatik-Betrieb)
Schalter 2: Aktiviert den Automatik Betrieb (Modbus an)
(Am Schalter 2 sind X3 + X4 und DCOM angeschlossen)

3.) Die Bedienung soll vom Bedienfeld erfolgen
Schalter 1 = Aus
Schalter 2 = Aus
`MF. K / REV` wird einmalig gedrpückt




---

## 🛠 Grundparameter für die Steuerung

| Parameter | Wert | Bedeutung |
| --- | --- | --- |
| **P0-01** | 2 | Motor Control Mode to V/F |
| **P0-02** | 1 | Command Source: Terminal |
| **P0-03** | 4 | Frequenzeinstellung (Source X) |
| **P0-04** | 9 | Wählbare Frequenzeinstellung über einen AUX Eingang (Source Y) |
| **P0-07** | 7 | Frequenzquelle soll entweder Source X oder Source Y sein |
| **P0-08** | 25 | Voreingestellte Frequenz |
| **P0-10** | 50 | Maximale Frequenz |
| **P0-11** | 0 | Source = P0-12 |
| **P0-17** | 00.20 | Acceleration Time = 0.2s |
| **P0-18** | 03.00 | Deceleration Time = 3s |
| **P0-19** | 2 | Acceleration/Deceleration Time Unit = 0.01s |
| **P0-20** | 20 | **Undokumentiert:** Für Single Phase zwingend notwendig! |
| **P1-00** | 4 | **Undokumentiert:** Single Phase 230V bei max. Frequenz |
| **P1-01** | 0.75 | Leistungsaufnahme der Pumpe in kW |
| **P1-02** | 230 | Nennspannung in Volt |
| **P1-03** | 46027 | Stromaufnahme der Pumpe in Ampere (**Wichtigster Wert!**) |
| **P1-04** | 50.00 | Nennfrequenz in Hz |
| **P1-05** | 2850 | Nenndrehzahl bei 100% (U/min) |
| **P3-01** | 6 | Torque Boost (Spannungserhöhung bei kleinen Frequenzen) |
| **P3-02** | 20 | CutOff Torque Boost (Frequenzgrenze für Boost) |
| **P4-00** | 12 | X1 = Pc-02=75 (entspricht 37,5 Hz) |
| **P4-01** | 13 | X2 = Pc-02=55 (entspricht 27,5 Hz) |
| **P4-02** | 37 | X3 = Switch von Modbus zu Aux |
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

## 📱 Steuerungslogik & Betriebsmodi

### 1. AUX & Modbus Umschaltung

* **Standard:** AUX ist führend (Poti am Bedienfeld aktiv).
* **Modbus Aktivierung:** Schalter an **X3 / X4 / DCOM** schaltet Poti/AUX aus und Modbus aktiv.
* **Manueller Modus:** Die Taste **"MF K"** schaltet auf das Bedienfeld um (Modbus & AUX werden deaktiviert).


### 2. Status der "LOC/REM" LED

| LED Status | Modus | Beschreibung |
| --- | --- | --- |
| **Leuchtet** | **AUX Aktiv** | Schalter X3/X4 aus. Steuerung über X5 (Start/Stopp) + Poti möglich. |
| **Blinkt** | **Modbus Aktiv** | Schalter X3+X4 an DCOM an. Steuerung nur über Modbus. Bedienfeld inaktiv (außer Stopp). |
| **Aus** | **Bedienfeld Aktiv** | Aktiviert durch Taste "MF K. REV". Poti aktiv, Aux/Modbus inaktiv. |

---










