# Die Software: Das Gehirn des Pools 🧠

Eigentlich ist die Software "nur" eine Konfiguration in **ESPHome**. Klingt simpel, oder? 
Wer sich aber intensiver mit einer Steuerung bschäftigt, dem wird klar, dass einfache Konfiguration von der Stange ohne etwas Zauber (lambda C++ Code) kaum eine Chance hat...

Wie jedes gute Projekt beginnen wir mit den "MustHave" Andorderungen und erweitern diese um logische Bedingungen.

<br>

---

<br>

## MustHave Anforderungen 📊

Hier sind die Hard-Facts, was das System ständig im Griff haben muss:

| Baustein | Job-Beschreibung |
| --- | --- |
| **Aktor** 🔌 | PH-Dosierpumpe anwerfen |
| **Aktor** ⚡ | Salzelektrolyse steuern |
| **Aktor** 🔄 | Poolpumpe via Frequenzumrichter (FU) regeln |
| **Aktor** 📱 | Tuya W2829 schalten |
| **Aktor** 📱 | Wärmepumpe schalten / regeln |
| **Sensor** 🌊 | Durchfluss im Hauptstrom & in der Messzelle checken |
| **Sensor** 🧪 | ORP (Redox) & PH-Werte messen |
| **Sensor** 🌡️ | Temperaturen (Wasser, Raum, Außen) im Blick behalten |
| **Sensor** 🧂 | "Low Salt"-Alarm via Stromstärke auslösen |

<br>

---

<br>

## Vertrauen ist gut, Kontrolle ist besser! ✅

Richtig spannend wird es bei der **Validierung**. Der Controller fragt sich ständig: "Passiert das gerade wirklich?"

* **Pumpe:** Läuft sie echt? (Abgleich: FU-Status + Durchflussmesser). 💧
* **Elektrolyse:** Produziert sie gerade Chlor? (Check via Strommessung & H-Brücke).
* **PH-Pumpe:** Läuft das Teil oder klemmt das Relais? 🧐
* **System-Check:** Ist das 24V-Netzteil an und der Tuya-Controller überhaupt online? (UART-Check).
* **Tank leer?** Der Controller berechnet den Verbrauch und sagt dir Bescheid, bevor die Säure ausgeht. 🧪

<br>

---

<br>

## Die Logik: Mehr als nur "An und Aus" 🤖

Die echte Magie passiert bei den Abhängigkeiten. Ein paar Beispiele aus dem Alltag des Controllers:

* **Sanfter Start:** Die Pumpe darf nur ran, wenn Timer & Modus grünes Licht geben. Dann startet sie erst kurz mit 100 % Power (zum "Wachwerden"), bevor sie nach 2–5 Minuten in den gemütlichen Stromsparmodus (z. B. 55 %) wechselt. 😴 energy-save!
* **Teamwork:** Chlorinator und PH-Dosierung dürfen nur spielen, wenn die Pumpe bereits läuft und die Werte wirklich eine Korrektur brauchen.
* **Timing:** Die Laufzeiten werden exakt berechnet. Sobald die Zeit abgelaufen ist oder der Zielwert erreicht ist, schalten wir ab 🛑
* **Unvohergesehenes ist unsere Erwartung:** Murphy’s Law als Standard-Einstellung🛠️. Beispiel: Wir werten einen plötzlichen Reboot des Controllers aus und entscheiden dann ob der Betrieb wieder aufgenommen werden darf.


> **Sicherheit geht vor:** 🛡️ Damit dein Pool nicht zur Chemiefabrik wird, sind smarte Sicherheitsmechanismen eingebaut. Wenn ein Bauteil disfunktional ist, geht das System sofort in den Shutdown-Modus. Sicher ist sicher!




<br>

---

<br>

## ESPHome WebServer - Poolcontroller

Die Logik ist wichtig, aber am Ende ist es entscheidend was wir sehen und Einstellen können.

<br>

<img width="1935" height="2338" alt="image" src="https://github.com/user-attachments/assets/c263f5f3-a0ba-4398-8d0c-aaab4d5ff549" />

<br>

<br>

### Der Status Log im WebServer
<img width="2814" height="1162" alt="image" src="https://github.com/user-attachments/assets/51157e21-4e9f-472c-b678-f8aa5c05d777" />

<br>

<br>

### Der Status Log in ESPHOME (etwas hübscher)
<img width="1428" height="715" alt="image" src="https://github.com/user-attachments/assets/18d227a4-0c07-4eaf-a291-879c676178a5" />








---

<br>
