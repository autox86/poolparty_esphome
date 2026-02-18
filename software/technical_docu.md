# 📘 Poolsteuerung – Ablauf-Dokumentation (ESPHome)

Diese Dokumentation beschreibt die interne Logik der Poolsteuerung mit Fokus auf  
**Sicherheit**, **Automatik**, **Dosierung** und **Betriebsmodi**.

---

## 1️⃣ Workmode (Pumpenmodus)

### Zweck
Der **Workmode** definiert den globalen Betriebszustand der Anlage. Er steuert:

- Pumpenfrequenz (Inverter)
- Freigabe oder Sperre von:
  - pH-Dosierung
  - ORP / Chlorinator
  - Wärmepumpe
- Wartungs- und Winterlogik

---

### Verfügbare Modi

| Modus | Bedeutung | Pumpenfrequenz | Dosierung | Frostwächter
|-----|---------|---------------|-----------|-----------|
| 55 % Stromsparen | Normalbetrieb, energiesparend | 55 % | erlaubt | Inaktiv
| 70 % Badebetrieb | Standardbetrieb | 70 % | erlaubt | Inaktiv
| 85 % Badebetrieb | Hohe Umwälzung | 85 % | erlaubt | Inaktiv
| 100 % Badebetrieb | Maximale Leistung | 100 % | erlaubt | Inaktiv 
| 0 % Wartung | Service / Arbeiten | 100 %* | **gesperrt** | Inaktiv
| 55 % Winterbetrieb | Winter / Stillstand | 55 % | **gesperrt** | Aktiv

\* Im Wartungsmodus wird bewusst 100 % gesetzt, damit der Inverter **manuell** bedient werden kann (z. B. Rückspülen).

---

### Logik im Detail

- **Wartungsmodus**
  - Alle Aktoren werden gestoppt (`script_stopp_all`)
  - pH / ORP / Wärmepumpe gesperrt
  - Automatik deaktiviert

- **Winterbetrieb**
  - Keine Chemie-Dosierung
  - Tuya-Modul ausgeschaltet

- **Alle anderen Modi**
  - Automatik aktiv
  - Ziel-Frequenz wird an den Inverter geschrieben
  - pH & ORP freigegeben

Nach jeder Modusänderung:
- Ziel-Frequenz wird über `number_target_frequency` gesetzt
- Status wird geloggt

---

## 2️⃣ pH-Dosierung

### Ziel
Automatische Senkung des pH-Werts mittels Dosierpumpe **nur bei Bedarf und unter sicheren Bedingungen**.

---

### Auslöser (Intervall)

- Prüfintervall: `${checkIntervalPH}`
- Start nur wenn:
  - Uhrzeit bekannt
  - `glo_ph_allowed == true`
  - Poolpumpe läuft
  - Pumpenvorlauf abgeschlossen (`poolpump_ok`)
  - pH-Wert **über** Grenzwert
  - Tankfüllstand > 500 ml
  - Tages- und Zykluslimits nicht erreicht

---

### Dosierablauf

1. **Freigabeprüfung**
   - Sicherheitslogik verhindert Fehlstarts
2. **Start**
   - Relais schaltet
   - Zyklus-Zähler wird zurückgesetzt
3. **Überwachung (Sicherheitsintervall)**
   - Alle 5 Sekunden:
     - Fördermenge berechnen
     - Tages- & Zyklusmenge aktualisieren
     - Tankfüllstand reduzieren

---

### Abschaltbedingungen

Die pH-Dosierung wird **sofort** gestoppt bei:

- Ziel-pH erreicht
- Zykluslimit überschritten
- Tageslimit überschritten
- Tank-Reserve < 500 ml
- Pumpenstopp / kein Durchfluss
- Wartungsmodus
- Timer außerhalb der Laufzeit

Der Abschaltgrund wird **immer geloggt**.

---

## 3️⃣ ORP-Intervall / Chlorinator

### Ziel
Automatische Chlorproduktion basierend auf dem **ORP-Messwert**, angepasst an:

- pH-Wert
- Wassertemperatur
- Pumpenleistung
- Tages- und Zykluslimits

---

### ORP-Intervall

- Prüfintervall: `${checkIntervalORP}`
- Start nur wenn:
  - Uhrzeit bekannt
  - `glo_orp_allowed == true`
  - Poolpumpe läuft
  - Pumpenvorlauf abgeschlossen
  - ORP < Minimalwert
  - Tageslimit nicht erreicht

---

### Laufzeitberechnung

Script: `script_calc_chlorinator_runtime`

Einflussfaktoren:

- ORP-Differenz zum Zielwert
- Poolvolumen
- Chlorleistung der Zelle
- Effizienzfaktoren:
  - pH-Wert
  - Wassertemperatur
  - Umwälzleistung

Begrenzungen:
- Maximale Laufzeit pro Zyklus
- Verbleibendes Tagesbudget

> Ergibt die Berechnung eine Laufzeit < ca. 30 Minuten, erfolgt **kein Start**.

---

### Startsequenz

1. 24 V-Netzteil einschalten (falls aus)
2. Polarität wechseln (Zellschutz)
3. 10 Sekunden Dead-Time
4. H-Brücke aktivieren
5. Countdown starten

---

### Abschaltbedingungen

Der Chlorinator stoppt sofort bei:

- Ziel-ORP erreicht
- Countdown abgelaufen
- Tagesmaximum erreicht
- Pumpenstopp / kein Durchfluss
- Wartungsmodus
- Timer außerhalb der Laufzeit

---

## 4️⃣ Sicherheitsintervall (Zentrale Instanz)

### Zweck
Das **Sicherheitsintervall** ist die höchste Instanz der Anlage.  
Es überwacht **alle kritischen Zustände** und greift sofort ein, wenn etwas unsicher wird.

- Intervall: **alle 7 Sekunden**

---

### Überwachte Zustände

- Pumpenstatus & Durchfluss
- Chlorinator aktiv?
- pH-Pumpe aktiv?
- Timer-Freigabe
- Frostschutz
- Tages- & Zykluslimits
- Countdown-Timer

---

### Hauptfunktionen

#### A) Gemeinsame Sicherheit
- Pumpe aus **oder** kein Durchfluss → **alle Aktoren aus**

#### B) Chlorinator-Überwachung
- Laufzeit hochzählen
- Countdown reduzieren
- Stopp bei:
  - Ziel-ORP
  - Tagesmaximum
  - Countdown = 0

#### C) pH-Dosierung
- Fördermenge berechnen
- Tages- & Zyklusmengen überwachen
- Tankfüllstand aktualisieren
- Stopp bei Grenzwertverletzung

#### D) Cleanup-Logik
- Pumpe läuft ohne Bedarf → Stop
- Manueller Betrieb wird erkannt und nicht überschrieben

#### E) Timer-Abschaltung
- Außerhalb der Zeitfenster → kontrollierter Stopp

#### F) Frostschutz
- Aktivierung bei ≤ −5 °C
- Deaktivierung erst bei ≥ −2 °C

---

## 5️⃣ Status-Logging

Alle 7 Sekunden wird ein vollständiger Status aktualisiert:

- Aktiver Workmode
- Pumpenvorlauf
- pH- & ORP-Bedarf
- Tages- & Zykluswerte
- Chlorinator-Polarität
- Restlaufzeiten
- Timer-Status

Zusätzlich:
- UI-Sensoren werden aktualisiert
- Offline-Zustände korrekt dargestellt

---

## ✅ Zusammenfassung

Diese Architektur bietet:

- ✔ klare Trennung von **Logik**, **Berechnung** und **Sicherheit**
- ✔ echte **Fail-Safe-Mechanismen**
- ✔ vollständige Nachvollziehbarkeit im Log
- ✔ saubere Wartungs- und Wintermodi
- ✔ Schutz vor Überdosierung und Fehlbedienung

---

