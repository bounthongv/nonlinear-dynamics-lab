

## Page 61

### Anhang V: Installations-Checkliste für den Laborbetrieb

Um einen reibungslosen Ablauf bei der Durchführung der Experimente im Praktikum zu garantieren, gehen Sie vor dem Eintreffen der Studierenden die folgende Checkliste durch.

#### V.1 Technische Vorbereitung der Arbeitsplätze

* [ ] **Betriebssystem-Ebene:** Überprüfen Sie, ob der Treiber `ANSI.SYS` in der Datei `CONFIG.SYS` geladen ist (`DEVICE=C:\DOS\ANSI.SYS`). Dieser wird für die korrekte farbliche Darstellung einiger Textmenüs zwingend benötigt.
* [ ] **Speicher-Konfiguration:** Stellen Sie sicher, dass mindestens $580\text{ KB}$ konventioneller DOS-Speicher frei sind. Nutzen Sie gegebenenfalls das Kommando `MEM /C`, um im oberen Speicherbereich (UMB) Platz zu schaffen (`DOS=HIGH,UMB`).
* [ ] **Grafik-Kompatibilität:** Überprüfen Sie die Grafikkarte durch Aufruf des kleinen Testprogramms `VGACHECK.EXE`. Sollte der Bildschirm dunkel bleiben, ersetzen Sie die `EGAVGA.BGI` im Programmverzeichnis durch den Standardtreiber der Borland-Bibliothek.
* [ ] **Maus-Treiber:** Laden Sie den residenten Maustreiber (z.B. `MOUSE.COM`) vor dem Start der Simulationsumgebung, da andernfalls keine interaktive Steuerung der Phasenraum-Fadenkreuze möglich ist.

#### V.2 Didaktische Vorbereitung

* [ ] Stellen Sie sicher, dass auf den lokalen Festplatten das Verzeichnis `C:\SCHWING\DATA\` existiert und für den aktuellen Benutzer schreibbar ist, damit numerische Ergebnisse für die spätere Auswertung gesichert werden können.
* [ ] Drucken Sie die Protokollvorlagen (Anhang C und I) in ausreichender Stückzahl aus.

---

## Page 62

### Anhang W: Versionshistorie und Fehlerkorrekturen (Errata)

In diesem Abschnitt sind die wichtigsten Modifikationen und Fehlerbehebungen dokumentiert, die seit der ersten Veröffentlichung der Version 1.0 (Herbst 1994) in das Programmpaket eingepflegt wurden.

#### W.1 Version 1.1 (Frühjahr 1995)

* **Fehlerbehebung im RK4-Modul:** Ein Vorzeichenfehler bei der Berechnung des Terms der kubischen Rückstellkraft ($dx^3$) im Duffing-Modul wurde korrigiert. Dies führte in Version 1.0 bei extrem großen Amplituden zu einer fälschlichen Divergenz der Trajektorien ins Unendliche.
* **Erweiterung der Benutzeroberfläche:** Die Taste `F10` wurde global als "Masken-Bestätigung" implementiert, um den Workflow bei der Parameterstudie zu beschleunigen.

#### W.2 Version 2.0 (Herbst 1995)

* **Integration des Poincaré-Schnitts:** Das Modul zur Erzeugung stroboskopischer Abbildungen wurde vollständig neu geschrieben. Die Punkte werden nun nicht mehr als dicke Pixel, sondern als feine Einzelpunkte dargestellt, was die Auflösung fraktaler Strukturen (Filamente) erheblich verbessert.
* **Unterstützung für mathematische Koprozessoren:** Das Programm erkennt nun beim Bootvorgang automatisch, ob eine Intel 80387 FPU vorhanden ist, und schaltet dynamisch auf optimierten 32-Bit-Assemblercode um.

#### W.3 Aktuelle Version 2.1 (Januar 1996)

* Das van der Pol-System wurde als neues Standardmodell hinzugefügt (Dokumentation siehe Anhang T).
* Ein Speicherleck bei der fortlaufenden Generierung des Bifurkationsdiagramms (Überlauf des Grafikspeichers nach ca. 10.000 Iterationen) wurde vollständig behoben.

---

## Page 63

### Anhang X: Bestellschein für Zusatzmodule und Updates

Sollten Sie Interesse an einer Erweiterung Ihres Simulationspakets oder an weiterführenden Lehrmaterialien haben, schneiden Sie diesen Schein aus und senden Sie ihn frankiert an den Verlag:

**Soft-Physics Publishing GmbH** *Abteilung für Lehrsoftware* *Schönhauser Allee 124* *D-10437 Berlin* ---

#### Ich/Wir bestellen hiermit fest:

* [ ] **Zusatzmodul "Gekoppelte Oszillatoren" (Version 1.0):** Erweiterung des Programms auf zwei über eine lineare Feder verbundene Pendelsysteme. Ermöglicht das Studium von Schwebungen, Energieaustausch und hochdimensionalem Chaos (Phasenraum-Dimension = 4).
*Preis für Einzelplatzlizenz: DM 49,– / Schullizenz: DM 129,–*
* [ ] **Begleitendes Dia-Set "Geometrie des Chaos":** 24 hochwertige Farbdias für den Vorlesungseinsatz. Enthält hochaufgelöste Renderings seltsamer Attraktoren (Lorenz-Attraktor, Rössler-Attraktor, Hénon-Abbildung) sowie reale Laboraufnahmen.
*Preis pro Set: DM 78,–*
* [ ] **Update-Service auf Version 2.2 (Lieferung auf 3.5" Diskette):** Beinhaltet das neue Modul zur Berechnung des fraktalen Einzugsgebiets (Fractal Basin Boundaries).
*Nur gegen Einsendung der Originaldiskette der Version 1.x / 2.0. Servicegebühr: DM 15,–*

##### Rechnungsanschrift / Stempel der Institution:

Name: ________________________________________

Institution/Schule: _______________________________

Straße / Hausnummer: ______________________________

PLZ / Ort: _______________________________________

Datum: ______________ Unterschrift: ___________________

---

**Ende des Hefts.**
