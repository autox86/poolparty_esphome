# Der Aufbau
Frei nach dem Familienmotto: **"Nicht schön, aber selten!"**

Auch wenn das optische Kabelmanagement vielleicht noch Spielraum für Perfektion lässt, wurde bei der technischen Umsetzung höchste Sorgfalt auf Sicherheit und Funktionalität gelegt. Das Ziel war ein stabiler, ordentlicher Aufbau, der im Alltag hält, was er verspricht.

Hier ein Blick auf das fertige Projekt:

<img width="630" height="821" alt="image" src="https://github.com/user-attachments/assets/1d76f49f-c439-407e-abf8-0497038ee118" />


## Die DC Seite: Schematisch
Damit der Funke (nur metaphorisch!) überspringt, habe ich hier einen ordentlichen Schaltplan der Gleichstromseite erstellt. Ideal für alle, die das Projekt als Inspiration für den eigenen Nachbau nutzen möchten:
<img width="945" height="442" alt="image" src="https://github.com/user-attachments/assets/9c85b5f7-a7cd-44f1-a138-901f11073fa0" />


Hier ist eine strukturierte und professionell formulierte Fassung für dein GitHub-Repository. Ich habe die Erklärungen präziser gestaltet und die FAQ-Sektion in ein modernes Design gebracht.

---

## Technische Funktionsweise & Logik

### Spannungsversorgung und Steuerung

Das **24V-Netzteil** bildet das Herzstück der DC-Versorgung. Es speist direkt die H-Brücke sowie den **PZEM-017 Energiemesser**, wobei letzterer zur Stabilisierung über ein **Step-Down-Modul auf 5V** versorgt wird.

### Die H-Brücke: Das Stellglied der Elektrolyse

Die H-Brücke fungiert als intelligenter „Schalter“ und „Umpoler“ für die 24V-Versorgung der Salzelektrolysezelle. Die Steuerung erfolgt über zwei primäre Signale des ESP32:

* **Richtungsschaltung (Pin „Phase“):** * **Low (0V):** Die Zelle wird in Richtung „Links“ gepolt.
* **High (3,3V):** Die Polung wird invertiert („Rechts“).


* **Aktivierung (Pin „PWMH“):** * Die H-Brücke schaltet die 24V zum Ausgang erst durch, wenn ein **High-Pegel (3,3V)** anliegt. Dies dient als Sicherheitsfeature: Ohne aktives Signal des Controllers findet keine Elektrolyse statt.

> [!NOTE]
> **Fehler-Reset:** Die H-Brücke verfügt über eine integrierte Fehlerüberwachung (LED-Anzeige). Über einen Taster zwischen **„Reset“ und „GND“** kann im Fehlerfall ein manueller Reset durchgeführt werden. Details hierzu finden sich in der Dokumentation des Herstellers.

---

## FAQ – Häufige Fragen

<details>
<summary><b>1. Warum eine H-Brücke statt klassischer Relais oder Schütze?</b></summary>
Sicherheit und Langlebigkeit. Sollte der Controller abstürzen, fällt der High-Pegel sofort ab und die Elektrolyse schaltet augenblicklich ab (Fail-Safe). Zudem vermeiden wir mit der Halbleiter-Lösung schädliche induktive Effekte, die beim Schalten hoher Ströme via Relais auftreten könnten.
</details>

<details>
<summary><b>2. Warum muss die Zelle umgepolt werden?</b></summary>
Dies dient der Selbstreinigung. Je nach Kalkgehalt des Wassers bilden sich Ablagerungen an den Platten der Zelle. Durch das regelmäßige Umpolen (alle 4 bis 8 Betriebsstunden) werden diese Ablagerungen abgestoßen.
</details>

<details>
<summary><b>3. Nimmt die Zelle durch das Umpolen Schaden?</b></summary>
Nein, die Elektrolysezelle selbst hat keine feste Polarität. Wichtig ist jedoch eine **Schaltpause**: Vor jedem Polwechsel wartet die Software 1–2 Minuten, um die Hardware zu schonen.
</details>

<details>
<summary><b>4. Warum die Wahl auf ein Qualitätsprodukt von Display3000?</b></summary>
Bei der Poolsteuerung mache ich keine Kompromisse. Die Produkte von <i>Speed IT up / Display3000</i> (Herr Küsters) sind hervorragend dokumentierte Ingenieursarbeit. Die Zuverlässigkeit und die Qualität der Dokumentation rechtfertigen den Preis gegenüber günstigen Import-Modulen bei weitem.
</details>

<details>
<summary><b>5. Welchen Zweck erfüllt die Messung von Spannung, Strom und Leistung (DC)?</b></summary>
Die Überwachung durch den PZEM-017 hat zwei zentrale Aufgaben:

1. **Status-Verifizierung:** Wir prüfen real, ob tatsächlich Strom fließt, wenn das Netzteil aktiv ist.
2. **Salz-Monitor (LowSalt):** Mit sinkendem Salzgehalt nimmt die Stromstärke ab. Sinkt der Wert unter eine Schwelle von ca. 7,5A, generiert das System eine Meldung zum Nachfüllen von Salz.
</details>

---
