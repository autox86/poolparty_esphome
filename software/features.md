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
