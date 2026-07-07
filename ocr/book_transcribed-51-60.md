

## Page 51

### Anhang L: Ergänzende Grafiken zu den Simulationsmodellen

Die folgenden Abbildungen zeigen typische Bildschirmausgaben des Programms im hochauflösenden VGA-Modus, wie sie bei der Durchführung der Laborübungen (Kapitel II) aufgezeichnet werden können.

![Figure L.1: Phase portrait of the Duffing Oscillator showing the classic double-scroll chaotic attractor trajectory looping symmetrically between two main wells.]
Abb. L.1: Phasenportrait des Duffing-Oszillators im chaotischen Zustand (Harte Feder mit harmonischer Anregung, vgl. Aufgabe 4).
Systemparameter: $c = -1.0, d = 1.0, b = 0.3, A = 0.4, \omega_A = 1.4$.

![Figure L.2: Stroboskopische Abbildung (Poincaré-Schnitt) of the Duffing attractor, displaying highly resolved fractal filaments and stretching-and-folding structures.]
Abb. L.2: Stroboskopische Abbildung (Poincaré-Schnitt) zu der in Abb. L.1 gezeigten chaotischen Bewegung. Die fraktale Filamentstruktur des seltsamen Attraktors wird durch das Ausblenden der transienten Übergänge deutlich sichtbar.

---

## Page 52

### Anhang M: Numerische Werte zur Nullstellenbestimmung

Bei der analytischen Berechnung von Fixpunkten und Bifurkationsgrenzen treten transzendente Gleichungen auf. Nachfolgend sind wichtige Referenzwerte für numerische Abgleichsroutinen gelistet.

#### M.1 Die ersten zehn Nullstellen der Besselfunktion erster Gattung $J_0(x)$

Diese Werte werden insbesondere bei der theoretischen Untersuchung von frequenzmodulierten Systemen und gekoppelten Oszillatoren als kritische Frequenzverhältnisse benötigt.

| Ordnung $n$ | Nullstelle $x_n$ | $J_1(x_n)$ | Ordnung $n$ | Nullstelle $x_n$ | $J_1(x_n)$ |
| --- | --- | --- | --- | --- | --- |
| **1** | $2.40482556$ | $+0.5191$ | **6** | $18.07106397$ | $-0.2051$ |
| **2** | $5.52007811$ | $-0.3403$ | **7** | $21.21163663$ | $+0.1903$ |
| **3** | $8.65372791$ | $+0.2715$ | **8** | $24.35247153$ | $-0.1784$ |
| **4** | $11.79153444$ | $-0.2325$ | **9** | $27.49347913$ | $+0.1686$ |
| **5** | $14.93091770$ | $+0.2114$ | **10** | $30.63460647$ | $-0.1603$ |

#### M.2 Die Feigenbaum-Konstanten (Universelle Skalenfaktoren)

Für Systeme, die über eine Kaskade von Periodenverdopplungen ins Chaos übergehen (Feigenbaum-Szenario, vgl. Abschnitt 2.6), gelten die folgenden universellen Grenzwerte:

* **Das Bifurkationsverhältnis ($\delta$):**
Bestimmt das exponentielle Verhältnis der Parameterintervalle zwischen aufeinanderfolgenden Verdopplungen:
$$\delta = \lim_{n \rightarrow \infty} \frac{\mu_n - \mu_{n-1}}{\mu_{n+1} - \mu_n} \approx 4.669201609102990$$


* **Der Skalenfaktor für die Pitchfork-Breite ($\alpha$):**
Beschreibt das Skalierungsverhalten der geometrischen Abstände der Bifurkationszweige:
$$\alpha = \lim_{n \rightarrow \infty} \frac{d_n}{d_{n+1}} \approx 2.502907875095892$$



---

## Page 53

### Anhang N: Quellcode zur Daten-Konvertierung (ASCII-Export)

Die vom Simulationsprogramm generierten Binärdateien (`*.BIN`) können mit dem folgenden kleinen Hilfsprogramm in lesbare Textdateien (ASCII) umgewandelt werden, falls kein direkter Export über das Menü durchgeführt wurde.

```pascal
Program Bin2Ascii;
Uses Crt;

Type
  DataRecord = Record
    Time  : Single;
    Angle : Single;
    Omega : Single;
  End;

Var
  InFile  : File Of DataRecord;
  OutFile : Text;
  Rec     : DataRecord;
  NameIn  : String;
  NameOut : String;

Begin
  ClrScr;
  Write('Geben Sie den Namen der Binaerdatei ein (z.B. TRAJ.BIN): ');
  ReadLn(NameIn);
  Write('Geben Sie den Namen der Ausgabedatei ein (z.B. DATA.TXT): ');
  ReadLn(NameOut);
  
  Assign(InFile, NameIn);
  Reset(InFile);
  Assign(OutFile, NameOut);
  Rewrite(OutFile);
  
  WriteLn(OutFile, '# Zeit [s]', #9, 'Winkel [rad]', #9, 'Omega [rad/s]');
  
  While Not Eof(InFile) Do
  Begin
    Read(InFile, Rec);
    WriteLn(OutFile, Rec.Time:12:6, #9, Rec.Angle:12:6, #9, Rec.Omega:12:6);
  End;
  
  Close(InFile);
  Close(OutFile);
  WriteLn('Konvertierung erfolgreich abgeschlossen.');
End.

```

---

## Page 54

### Anhang O: Kalibrierungsdaten für das Pohlsche Drehpendel

Für Anwender, die das experimentelle "Pohlsche Rad" im Labor betreiben (vgl. Anhang C), sind nachfolgend die Werksspezifikationen des Standardmodells aufgeführt. Diese Daten dienen als ideale Startkonfiguration für eine realitätsnahe Simulation.

#### O.1 Mechanische Abmessungen und Materialkonstanten

* Durchmeser des Kupfer-Drehrades: $D = 220\text{ mm}$
* Gesamtmasse des rotierenden Systems: $M = 0.385\text{ kg}$
* Trägheitsmoment der Kupferscheibe: $I_0 = 1.85 \cdot 10^{-3}\text{ kg}\cdot\text{m}^2$
* Richtgröße der Spiralfeder (Torsionsfederkonstante): $D^* = 0.0245\text{ Nm/rad}$
* Maximal zulässiger Verdrehwinkel: $\phi_{\max} = \pm 190^\circ$

#### O.2 Elektrische Spezifikationen der Wirbelstrombremse

Die Bremswirkung wird über den Stromfluss $I_B$ in den Feldspulen der Elektromagnete reguliert. Die Dämpfungskonstante $b$ verhält sich näherungsweise quadratisch zur angelegten Stromstärke:

$$b(I_B) \approx \kappa \cdot I_B^2,$$

wobei der Apparatekoeffizient für dieses Modell mit $\kappa \approx 0.0115\text{ Nms/A}^2$ bestimmt wurde.

##### Referenztabelle zur Dämpfungsjustierung:

| Bremsstrom $I_B$ (A) | Dämpfungskoeffizient $b$ (Nms) | Abklingkonstante $\gamma$ (1/s) | Charakter des Systems |
| --- | --- | --- | --- |
| `0.0` | $0.0002$ | $0.054$ | Fast ungedämpft |
| `0.2` | $0.0007$ | $0.189$ | Schwache Dämpfung |
| `0.5` | $0.0031$ | $0.838$ | Schwingfall (Praktikum) |
| `1.0` | $0.0117$ | $3.162$ | Starke Dämpfung |
| `1.5` | $0.0261$ | $7.054$ | Kriechgrenze erreicht |

---

## Page 55

### Anhang P: Mathematische Ergänzungen zu nichtlinearen Potentialen

Das dynamische Verhalten eines ungedämpften, ungetriebenen Systems lässt sich direkt aus der Topologie seiner Potentiallandschaft $V(x)$ ableiten. Für ein eindimensionales System der Form $\ddot{x} = -\frac{dV}{dx}$ entspricht die Gesamtenergie einer Erhaltungsgröße.

#### P.1 Das Potential des Duffing-Oszillators

Die Bewegungsgleichung des freien Duffing-Oszillators lautet:

$$\ddot{x} + c \cdot x + d \cdot x^3 = 0$$

Das zugehörige mechanische Potential ergibt sich durch Integration zu:

$$V(x) = \int (c \cdot x + d \cdot x^3) dx = \frac{1}{2}c \cdot x^2 + \frac{1}{4}d \cdot x^4$$

Man unterscheidet je nach Vorzeichen der Parameter zwei fundamentale Fälle:

##### 1. Das "Harte Feder"-Potential ($c > 0, d > 0$)

Das Potential besitzt ein einzelnes, parabolisches Minimum im Ursprung ($x=0$). Die Rückstellkraft wächst überproportional mit der Auslenkung. Alle Trajektorien sind globale, geschlossene Schwingungen.

##### 2. Das "Doppelmulden-Potential" (*Double-Well*) ($c < 0, d > 0$)

Dieses System beschreibt eine elastische Knickstange oder ein inverses Pendel zwischen zwei Magneten. Der Ursprung $x=0$ wird zu einem lokalen Maximum (instabiler Sattelpunkt). Es entstehen zwei neue, symmetrische Minima (stabile Fixpunkte) bei:

$$x^*_{\pm} = \pm \sqrt{-\frac{c}{d}}$$

Trajektorien mit geringer Gesamtenergie oszillieren lokal in einer der beiden Mulden. Trajektorien mit hoher Energie kreuzen das zentrale Maximum und umschlingen beide Fixpunkte.

---

## Page 56

### Anhang Q: Numerische Schrittweitensteuerung im Vergleich

Obwohl das Programm standardmäßig mit einer festen Schrittweite $dt$ operiert (vgl. Abschnitt IV.4), ist im mathematischen Modul die Option für ein adaptives Runge-Kutta-Fehlberg-Verfahren (RKF45) vorbereitet. Dies dient zur Kontrolle bei extrem steilen Gradienten im Phasenraum.

#### Q.1 Das Prinzip der eingebetteten Verfahren

Das RKF45-Verfahren berechnet pro Integrationsschritt zwei Approximationen unterschiedlicher Ordnung: eine Lösung $\vec{x}_{k+1}$ mit der Ordnung 4 und eine Kontrolllösung $\hat{\vec{x}}_{k+1}$ mit der Ordnung 5. Beide Berechnungen nutzen dieselben Steigungsvektoren $\vec{k}_i$, was den Rechenaufwand minimiert.

Der lokale Diskretisierungsfehler $\epsilon$ bestimmt sich aus der Differenz beider Lösungen:

$$\epsilon = \|\vec{x}_{k+1} - \hat{\vec{x}}_{k+1}\|$$

Liegt der Fehler oberhalb einer vorgegebenen Toleranzgrenze ($\epsilon > \text{Tol}_{\max}$), wird der aktuelle Rechenschritt verworfen und mit einer halbierten Schrittweite $dt_{\text{neu}} = dt/2$ wiederholt. Ist der Fehler extrem klein ($\epsilon < \text{Tol}_{\min}$), kann die Schrittweite für den nächsten Schritt verdoppelt werden, um Rechenzeit einzusparen.

#### Q.2 Konsequenzen für die stroboskopische Abbildung

Für die Generierung von Poincaré-Schnitten ist ein variables $dt$ problematisch, da die Abtastpunkte exakt äquidistant im Takt der Treiberperiode $T_A = 2\pi/\omega_A$ liegen müssen. Bei adaptiver Schrittweite muss das Programm daher an den Intervallgrenzen eine Interpolation (z.B. mittels kubischer Splines) durchführen, um den exakten Schnittpunkt mit der Phasenebene zu treffen. Dies erklärt, warum das feste RK4-Verfahren in der Programmpraxis oft bevorzugt wird.

---

## Page 57

### Anhang R: Glossar englischer Fachbegriffe (Dictionary of Chaos)

Da die moderne Fachliteratur zur nichtlinearen Dynamik weitgehend in englischer Sprache verfasst ist, dient dieses kurze Glossar als Übersetzungshilfe für weiterführende Studien.

* **Attractor** $\rightarrow$ *Attraktor:* Eine Teilmenge des Phasenraums, auf welche alle Trajektorien aus einem bestimmten Einzugsgebiet für $t \rightarrow \infty$ hinsteuern.
* **Basin of Attraction** $\rightarrow$ *Einzugsgebiet:* Der Bereich von Anfangsbedingungen im Phasenraum, deren Trajektorien gegen denselben Attraktor konvergieren.
* **Bifurcation** $\rightarrow$ *Bifurkation / Verzweigung:* Eine qualitative Änderung des Systemverhaltens (z.B. Periodenverdopplung) bei der Variation eines Kontrollparameters.
* **Boundary** $\rightarrow$ *Grenzlinie:* Die Trennlinie im Phasenraum, beispielsweise zwischen zwei Einzugsgebieten (Separatrix).
* **Burst** $\rightarrow$ *Ausbruch:* Ein plötzlicher, unregelmäßiger chaotischer Abschnitt innerhalb einer intermittierenden Bewegung.
* **Driven / Forced Oscillator** $\rightarrow$ *Getriebener Oszillator:* Ein Schwingungssystem, das einer explizit zeitabhängigen, äußeren Kraft unterliegt.
* **Intermittency** $\rightarrow$ *Intermittenz:* Ein Weg ins Chaos, bei dem sich reguläre und chaotische Phasen unregelmäßig abwechseln.
* **Limit Cycle** $\rightarrow$ *Grenzzyklus:* Eine isolierte, geschlossene Trajektorie im Phasenraum eines dissipativen Systems, die einer periodischen Schwingung entspricht.
* **Map** $\rightarrow$ *Diskrete Abbildung:* Eine mathematische Gleichung, die den Systemzustand zu diskreten Zeitschritten beschreibt ($x_{k+1} = f(x_k)$).
* **Pitchfork Bifurcation** $\rightarrow$ *Stimmgabel-Bifurkation:* Typische Geometrie der Periodenverdopplung im Feigenbaum-Diagramm.
* **Quasiperiodic** $\rightarrow$ *Quasiperiodisch:* Eine Bewegung, die auf der Überlagerung inkommensurabler Frequenzen basiert.
* **Strange Attractor** $\rightarrow$ *Seltsamer Attraktor:* Ein Attraktor mit fraktaler Geometrie und empfindlicher Abhängigkeit von den Anfangsbedingungen.

---

## Page 58

### Anhang S: Hinweise zur Lizenzierung und Vervielfältigung

Das diesem Begleitheft beigefügte Simulationsprogramm "Nichtlineare Schwingungen" ist urheberrechtlich geschützt. Für den Einsatz im Bildungsbereich gelten folgende Sonderregelungen.

#### S.1 Einzelplatzlizenz (Standard)

Die mitgelieferte Diskette berechtigt zur Installation und Nutzung des Programms auf genau einem Computersystem. Eine gleichzeitige Nutzung auf mehreren Rechnern oder das Bereitstellen in öffentlichen Datennetzen ohne Zusatzlizenz ist unzulässig.

#### S.2 Schullizenz / Campuslizenz

Für Schulen, Universitäten und Volkshochschulen kann beim Verlag eine kostengünstige Campuslizenz erworben werden. Diese berechtigt:

1. Zur Installation des Programms auf einer unbegrenzten Anzahl von Rechnern innerhalb der Liegenschaften der jeweiligen Institution.
2. Zur Bereitstellung auf lokalen Fileservern im Rahmen des EDV-gestützten Physikunterrichts.
3. Zur Vervielfältigung dieses Begleithefts als Kopiervorlage für den internen Gebrauch in Praktikumskursen.

> **Haftungsausschluss:**
> Der Entwickler und der Verlag übernehmen keine Haftung für Schäden, die direkt oder indirekt aus der Installation oder dem Betrieb dieser Software resultieren. Da es sich um ein hardwarenahes DOS-Programm handelt, erfolgt die Nutzung auf eigene Verantwortung des Anwenders.

---

## Page 59

### Anhang T: System-Updates und Add-ons (Version 2.1)

Im Zuge der kontinuierlichen Produktpflege wurde das Programmpaket um zusätzliche mathematische Modelle erweitert, die in der ersten Auflage noch nicht dokumentiert waren.

#### T.1 Das van der Pol-System

Im Menü **System** lässt sich nun auch der van der Pol-Oszillator aktivieren. Die Differentialgleichung beschreibt ein System mit einer ortsabhängigen, nichtlinearen Dämpfung:

$$\ddot{x} - \epsilon(1 - x^2)\dot{x} + x = 0$$

##### Besondere Verhaltensweisen:

* Für kleine Amplituden ($x < 1$) ist der Dämpfungsterm negativ ($\epsilon(1-x^2) > 0$). Das System entzieht seiner Umgebung Energie und schwingt sich selbsttätig auf.
* Für große Amplituden ($x > 1$) wird die Dämpfung positiv und bremst das System ab.
* Unabhängig von den Anfangswerten kollabieren alle Trajektorien für $t \rightarrow \infty$ auf einen absolut stabilen, charakteristischen **Grenzzyklus** im Phasenraum. Dieses Modell dient in der Biophysik zur Beschreibung von Herzschlagrhythmen und Nervenimpulsen (FitzHugh-Nagumo-Modell).

#### T.2 Optimierter Grafik-Treiber für High-Resolution VGA

Durch eine Modifikation der Datei `EGAVGA.BGI` konnte die Bildwiederholfrequenz bei der On-Screen-Animation um ca. $25\%$ gesteigert werden. Rechner ab einer Taktfrequenz von $33\text{ MHz}$ (Intel 486DX) sind nun in der Lage, chaotische Trajektorien im Phasenraum in echter Echtzeit ohne Verzögerung zu zeichnen.

---

## Page 60

### Anhang U: Stichwortverzeichnis für Quelltextvariablen

Für Programmierer, die den beigefügten Pascal-Quellcode modifizieren oder eigene Module ankoppeln möchten, sind hier die zentralen globalen Variablenbezeichner deklariert.

* `A_amp` (Real): Amplitude der äußeren Anregungskraft bzw. des Drehmoments [$Nm$].
* `b_damp` (Real): Globaler viskoser Dämpfungskoeffizient für lineare Reibung.
* `CurrentPageAddress` (Word): Segmentadresse des VGA-VRAMs für das Page-Flipping.
* `dt_step` (Real): Feste Zeitschrittweite der numerischen Integration (RK4).
* `g_grav` (Real): Die Schwerebeschleunigung (wird programmweit mit $9.81\text{ m/s}^2$ initialisiert).
* `I_moment` (Real): Trägheitsmoment des Pendelkörpers oder des Drehpendels.
* `l_length` (Real): Geometrische Länge der masselosen Pendelstange [$m$].
* `m_mass` (Real): Masse des schwingenden Körpers im Schwerpunkt [$kg$].
* `omega_A` (Real): Kreisfrequenz des periodischen Treibers (Eingabe in $Hz$ wird intern konvertiert).
* `Phi_pos` (Real): Der aktuelle Auslenkungswinkel im Bogenmaß.
* `Omega_vel` (Real): Die aktuelle Winkelgeschwindigkeit $\dot{\phi}$ [$rad/s$].
* `Time_elapsed` (Real): Die akkumulierte Simulationszeit seit dem Start des aktuellen Laufs.

---

**Ende des erweiterten Dokumentenanhangs.**
*Soft-Physics Distribution, Technical Support Department, Update 1996.*

---

Damit ist auch dieser Block von zehn Seiten vollständig transkribiert. Wenn Sie weitere Seiten haben, laden Sie diese einfach hoch!
