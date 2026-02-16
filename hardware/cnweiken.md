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

### 📋 Erforderliche Parameter-Einstellungen

Für den kombinierten Betrieb (Modbus und Handbetrieb) müssen die folgenden Parameter gesetzt werden:

| Parameter | Wert | Beschreibung |
| --- | --- | --- |
| **P0-01** | 2 | Betriebsart-Einstellung |
| **P0-02** | 2 | Auswahl der Kommunikationsquelle |
| **P0-20** | 20 | Undokumentierter, aber funktionaler Parameter |
| **P0-03** | 09 | Frequenzvorgabe |
| **P0-04** | 04 | Frequenzvorgabe |
| **P0-07** | 2 | Frequency Source Selection |
| **P0-08** | 25 | Preset-Frequency |
| **P1-00** | 4 | Steuermodus (4 = Single Phase at 230V at max Frequency) |
| **P4-00** | 12 | Eingangsanschluss-Einstellung |
| **P4-01** | 18 | Umschaltfrequenz von X zu Y |
| **P4-02** | 14 | Eingangsanschluss-Einstellung |
| **P4-03** | 9 | Eingangsanschluss-Einstellung |
| **P4-04** | 1 | Eingangsanschluss-Einstellung |
| **P4-05** | 0 | Eingangsanschluss-Einstellung |
| **P7-01** | 1 | Anzeige-Parameter |
| **P0-28** | 0 | Motor-Parameter |
| **PD-00** | 6005 | Modbus-Adresse |
| **PD-01** | 0 | Modbus-Kommunikationsformat |
| **PD-02** | 005 | Modbus-Baudrate |
| **PD-03** | 02 | Modbus-Zeitüberschreitung |
| **PD-04** | 000 | Modbus-Antwortverzögerung |
| **PD-05** | 31 | Modbus-Datenformat |
| **P6-00** | 1 | Start/Stopp Control |
| **P6-01** | 2 | Start/Stopp Control |
| **P6-03** | 10.00 | Startup Frequency |


### 📋 Ergebnis der Parameter

* **Kommunikation:** Die primäre Kommunikation ist nun Modbus und die SlaveID ist "05".
* **MF.K / REV:** Stellt den Kommunikationsmode von Modbus auf lokales Panel um
* **Schalter zwischen X2 und DCOM:** Aktiviert die Frequenzkontrolle am Poti des Panels, statt Modbus

**Fazit:** Somit ist garantiert, dass die Frequenzsteuerung selbst bei Ausfall des Poolcontrollers möglich ist.


---



**Detailierte Informationen zu den möglichen Optionen:**
[Manual WD600](https://github.com/autox86/poolparty_esphome/blob/main/manuals/WK600-Single-manual.pdf)





