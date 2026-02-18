# 📘 Poolsteuerung – Funktionsübersicht

Dieser Controller steuert eine Poolanlage bestehend aus **Poolpumpe (FU/Modbus)**, **pH-Dosierung**, **Chlorinator (ORP-geführt)** sowie **Zeit- und Sicherheitslogik**.  
Die Architektur ist **zustands- und sicherheitsorientiert**, mit klarer Trennung zwischen **Automatik**, **manuellen Eingriffen** und **Failsafe-Mechanismen**.

---

## 🔑 Grundprinzipien

- **Automatik hat immer Vorrang**, manuelle Schalter sind **Test / Debug only**
- **Sicherheitsbedingungen werden vor jeder Aktion geprüft**
- **Alle Grenzwerte sind parametrierbar (HA / Webserver)**
- **Keine „blinden“ Aktoraktionen** – alles ist sensor- & statusabhängig
- **Restart-sicheres Verhalten** (kein unkontrolliertes Anlaufen)

---

## 🚀 On_Boot Verhalten (Besonderheit)

Beim Start oder Reboot des ESP:

- ❌ **Keine Aktoren starten automatisch**
- ❌ Chlorinator & pH-Pumpe bleiben **hart AUS**
- ❌ 24 V Netzteil bleibt **aus**
- ❌ H-Brücke ist stromlos & richtungslos
- ✅ Zähler & States werden initialisiert
- ✅ Online-Status der Subsysteme wird neu bewertet
- ✅ Automatik entscheidet **erst nach vollständiger Initialisierung**

➡️ **Kein gefährlicher Zustand nach Stromausfall oder Flash!**

---

## ⚙️ Subsysteme im Überblick

---

## 🌀 Poolpumpe / Frequenzumrichter (Modbus)

### Funktionen
- Start / Stop über **Modbus Write Register**
- Ziel-Frequenz einstellbar (in %)
- Vorlaufzeit vor Dosierung / Chlorung
- Automatischer Start über **Zeitplan**
- Optionaler Restart nach ESP-Reboot

### Besonderheiten
- **5-Sekunden-Schutzlogik** gegen Web-Doppelclicks
- Anzeige unterscheidet zwischen:
  - *User-Aktion*
  - *echtem Inverter-Status*
- Kein automatischer Neustart bei aktivem „kein Autostart“-Schalter

---

## ⏱️ Zeitsteuerung (Timer)

### Funktionen
- Frei definierbare Start- & Stoppzeit (HH:MM)
- Wochenplan (Mo–So)
- Über-Mitternacht-Betrieb möglich
- Dynamische Zeitkomponente (`dynamic_on_time`)

### Logik
Timer ist **nur aktiv**, wenn:
`Zeitfenster OK
UND Wochentag erlaubt
UND Timer nicht deaktiviert`


### Besonderheiten
- Triggert **definierte Scripts**, keine direkten Schaltaktionen
- Einheitliche Quelle für:
  - Pumpenlauf
  - Chlorfreigabe
  - pH-Freigabe

---

## 🧪 pH-Dosierung

### Funktionen
- pH-Regelung über:
  - pH-Istwert
  - Min / Max Grenzwerte
- Dosiermenge:
  - max. pro Zyklus
  - max. pro Tag
- Förderleistung parametrierbar (l/h → intern ml/s)
- Tanküberwachung

### Sicherheitslogik
- ❌ Keine Dosierung ohne laufende Pumpe
- ❌ Keine Dosierung bei leerem Tank
- ❌ Sperre nach Zyklus (Beruhigungsphase)
- ❌ Tageslimit verhindert Überdosierung

### Besonderheiten
- Tankgröße **dynamisch änderbar**
- Tank-Reset physisch **oder** per Web
- Letzter Zyklus wird geloggt (ml)

---

## ⚡ Chlorinator / ORP-Regelung

### Funktionen
- ORP-geführte Chlorproduktion
- Laufzeitberechnung abhängig von:
  - ORP-Differenz
  - Poolvolumen
  - Pumpenleistung
  - pH-Wert
  - Wassertemperatur
- Zyklische Polaritätsumkehr (Zellschutz)
- Tages- & Zykluslimit

### Sicherheitslogik
- ❌ Keine Produktion ohne Pumpenvorlauf
- ❌ Kein Betrieb im Wartungsmodus
- ❌ Kein Betrieb unter Mindestlaufzeit (~30 min)
- ❌ Kein Überschreiten des Tageslimits
- ❌ Sofortiger Stopp bei Fehler / Timer-Ende

### Besonderheiten
- **Dead-Time (10 s)** vor Einschalten der H-Brücke
- 24 V Netzteil wird **nur bei Bedarf** aktiviert
- Laufzeit wird **dynamisch gekürzt**, wenn Tagesbudget fast erreicht

---

## 🔄 Wartungsmodus (Besonderheit)

### Verhalten
- Sperrt **alle Automatikfunktionen**
- Verhindert:
  - Chlorproduktion
  - pH-Dosierung
  - Pumpenautomatik
- Aktivierbar:
  - physischer Taster
  - Web / HA

➡️ **Zentraler „Alles sicher“-Modus**

---

## 📡 Online- & Statusüberwachung

### Überwachte Komponenten
- Frequenzumrichter (Pumpe)
- Chlorinator-Netzteil (24 V)
- Tuya-Modul
- Wärmepumpe
- PV-Zähler

### Verwendung
- Statusanzeige im Web / HA
- Entscheidungsgrundlage für Automatik
- Anzeige im Status-Script (Debug)

---

## 🧯 Sicherheits- & Failsafe-Mechanismen

- Alle Aktoren:
  - **ALWAYS_OFF** bei Boot
- Keine verdeckten Abhängigkeiten
- Manuelle Schalter sind:
  - **nicht** für Dauerbetrieb gedacht
  - zusätzlich abgesichert
- Emergency-Stop bei:
  - Pumpenausfall
  - Timer-Ende
  - Wartung
  - Sensor-Fehler

---

## 🧠 Architektur-Highlights

- Klare Trennung:
  - **Sensorik**
  - **Entscheidungslogik**
  - **Aktorsteuerung**
- State-Machine-ähnliches Verhalten ohne Overengineering
- Vollständig HA- & Web-konfigurierbar
- Debug-freundlich (Status-Script, Logs, Textsensoren)

---


## 🧩 Konfig-Matrix – Welcher Parameter wirkt wo?

Diese Matrix ist Gold wert für Wartung & spätere Erweiterungen.

| PARAMETER                  | WIRKT AUF                               |
|----------------------------|----------------------------------------|
| timer_start / stop         | Pumpenstart, Chlor-, pH-Freigabe       |
| allowed_weekdays           | Gesamte Automatik                       |
| maintenance_mode           | Sperrt alle Scripts                     |
| pump_min_runtime           | Chlor & pH Freigabe                     |
| pump_target_frequency      | FU Modbus Write                         |
| pump_restart_allowed       | Verhalten nach Reboot                   |
| ph_target                  | pH Regelung                             |
| ph_min / ph_max            | Dosierfreigabe                          |
| ph_max_ml_per_cycle        | Dosierdauer                             |
| ph_max_ml_per_day          | Tageslimit                              |
| ph_tank_size               | Reichweitenberechnung                   |
| ph_pause_time              | Beruhigungsphase                         |
| orp_target                 | Chlor Laufzeit                          |
| orp_min_runtime            | Chlorfreigabe                           |
| chlor_max_runtime_day      | Tageslimit                              |
| chlor_dead_time            | H-Brücken-Schutz                        |
| chlor_polarity_interval    | Zellschutz                              |
| water_temperature          | ORP Laufzeitkorrektur                   |
| pool_volume                | Chlor Laufzeit                           |
| pump_flow_rate             | Chlor Effizienz                          |


