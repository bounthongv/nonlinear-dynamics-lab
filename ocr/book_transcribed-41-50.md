Hier ist die exakte Transkription der nächsten zehn Seiten (Seiten 41 bis 50) Ihres Buches, fortlaufend im gleichen Format:

---

## Page 41

### Anhang F: Verzeichnis der verwendeten Formelzeichen

Im Folgenden sind die im Text und in den Simulationsmasken verwendeten physikalischen und mathematischen Symbole zusammenfassend aufgeführt.

| Symbol | Physikalische Bedeutung | Standard-Einheit (SI) |
| --- | --- | --- |
| $\phi$ | Auslenkwinkel (Pendel, Pohlsches Rad) | rad / grad |
| $\Omega, \dot{\phi}$ | Winkelgeschwindigkeit | rad/s / grad/s |
| $\ddot{\phi}$ | Winkelbeschleunigung | $\text{rad/s}^2$ |
| $x$ | Lineare Auslenkung (Federschwinger) | m |
| $\dot{x}$ | Lineare Schwingungsgeschwindigkeit | m/s |
| $m$ | Masse des Oszillators / der Unwucht | kg |
| $l$ | Pendellänge / Abstand der Zusatzmasse | m |
| $I$ | Trägheitsmoment des rotierenden Körpers | $\text{kg}\cdot\text{m}^2$ |
| $g$ | Schwerebeschleunigung ($9.81$) | $\text{m/s}^2$ |
| $b$ | Dämpfungs- bzw. Reibungskoeffizient | Nms / Ns/m |
| $r$ | Reibungsexponent | – |
| $A$ | Amplitude der erregenden Kraft / des Moments | Nm / N |
| $\omega_A$ | Kreisfrequenz der äußeren Anregung | 1/s |
| $T$ | Periodendauer der Schwingung | s |
| $c$ | Lineare Federkonstante | N/m |
| $d$ | Kubischer Koeffizient der Rückstellkraft | $\text{N/m}^3$ |
| $\lambda$ | Lyapunov-Exponent | 1/s |
| $\psi$ | Phasenwinkel der harmonischen Anregung | rad |

---

## Page 42

### Anhang G: Installationshinweise für Netzwerke und Windows 95

Obwohl das Simulationsprogramm als native MS-DOS-Anwendung konzipiert wurde, lässt es sich in modernen Systemumgebungen sowie in Novell-Netzwerken stabil betreiben, wenn bestimmte Konfigurationen eingehalten werden.

#### G.1 Betrieb unter Windows 95

Unter dem Betriebssystem Windows 95 kann das Programm entweder im MS-DOS-Modus oder in einer DOS-Box (DOS-Eingabeaufforderung) gestartet werden. Für eine flüssige Grafikausgabe ohne Ruckeln wird die Erstellung einer PIF-Datei empfohlen:

1. Klicken Sie mit der rechten Maustaste auf die Datei `SCHWING.EXE` und wählen Sie **Eigenschaften**.
2. Wechseln Sie zur Registerkarte **Programm** und klicken Sie auf **Erweitert**.
3. Aktivieren Sie das Kontrollkästchen **MS-DOS-Modus** sowie **Aktuelle MS-DOS-Konfiguration spezifizieren**.
4. Tragen Sie in der Registerkarte **Bildschirm** unter "Nutzung" den Wert **Vollbild** ein. Dadurch wird verhindert, dass Windows versucht, das VGA-Signal in einem skalierbaren Fenster zu emulieren.

#### G.2 Installation in Schulnetzwerken (z.B. Novell NetWare)

Beim Einsatz im Physikunterricht oder in Computerlaboren kann das Programm zentral auf einem Serverlaufwerk hinterlegt werden:

* Die ausführbare Datei benötigt nur Leserechte (`Read` und `File Scan`).
* **Wichtig:** Da das Programm temporäre Dateien für den Grafikexport und die Parameter-Konfiguration (`SETUP.DAT`) schreibt, muss das Arbeitsverzeichnis des jeweiligen lokalen Benutzers Schreibrechte (`Write`, `Create`, `Erase`) besitzen. Nutzen Sie hierzu das DOS-Kommando `SET` zur Umleitung temporärer Pfade, falls notwendig.

---

## Page 43

### Anhang H: Weiterführende theoretische Vertiefungen

#### H.1 Das Hamilton-Formalismus für nichtlineare Systeme

Für theoretisch interessierte Leser soll hier kurz der Übergang von den Newtonschen Bewegungsgleichungen zur Hamiltonschen Mechanik skizziert werden, die eine elegante geometrische Interpretation des Phasenraums ermöglicht.

Für das ungedämpfte, freie mathematische Pendel (Abschnitt 2.2) lautet die Lagrange-Funktion $L = T - V$ (Kinetische Energie minus Potenzielle Energie):

$$L(\phi, \dot{\phi}) = \frac{1}{2} m l^2 \dot{\phi}^2 - mgl(1 - \cos\phi)$$

Der kanonisch konjugierte Impuls $p_\phi$ berechnet sich durch Differentiation nach der verallgemeinerten Geschwindigkeit:

$$p_\phi = \frac{\partial L}{\partial \dot{\phi}} = m l^2 \dot{\phi} = I \cdot \Omega$$

Die Hamilton-Funktion $H = T + V$, welche der Gesamtenergie des Systems entspricht, lautet somit:

$$H(\phi, p_\phi) = \frac{p_\phi^2}{2 I} + mgl(1 - \cos\phi)$$

Die Hamiltonschen Bewegungsgleichungen bilden ein System zweier gekoppelter Differentialgleichungen erster Ordnung:

$$\begin{aligned}
\dot{\phi} &= \frac{\partial H}{\partial p_\phi} = \frac{p_\phi}{I} \\
\dot{{p}_\phi} &= -\frac{\partial H}{\partial \phi} = -mgl \sin\phi
\end{aligned}$$

Dieses System ist exakt äquivalent zu den Gleichungen (2.2.1). Im Phasenraum $(\phi, p_\phi)$ entsprechen die Trajektorien den Höhenlinien der Funktion $H(\phi, p_\phi) = E = \text{const}$. Da die Energie erhalten bleibt, findet bei ungedämpften Systemen keine Phasenraumkontraktion statt; die Divergenz des Vektorfeldes ist identisch Null (Satz von Liouville für konservative Systeme).

---

## Page 44

#### H.2 Die Linearisierung in der Umgebung von Fixpunkten

Die qualitative Analyse nichtlinearer Systeme beginnt standardmäßig mit der Bestimmung der Fixpunkte (Gleichgewichtslagen) und deren Stabilitätsverhalten. Ein Fixpunkt $(\phi^*, \Omega^*)$ ist dadurch definiert, dass alle zeitlichen Ableitungen verschwinden.

Für das freie Pendel (Gleichung 2.3.1) bedeutet dies:

$$\begin{aligned}
\Omega^* &= 0 \\
-\frac{b}{I}\Omega^* - \frac{mgl}{I}\sin\phi^* &= 0 \implies \sin\phi^* = 0
\end{aligned}$$

Daraus ergeben sich im Intervall $[-\pi, +\pi]$ zwei physikalische Fixpunkte:

1. Der Fixpunkt $F_1 = (0, 0)$ – die untere Ruhelage.
2. Der Fixpunkt $F_2 = (\pi, 0)$ – die obere vertikale Ruhelage.

Um die Dynamik in der unmittelbaren Nähe eines Fixpunkts zu untersuchen, führt man eine Taylor-Entwicklung (Linearisierung) durch. Wir setzen $\phi = \phi^* + \xi$ und $\Omega = \Omega^* + \eta$, wobei $\xi, \eta \ll 1$ kleine Auslenkungen darstellen.

Die Jacobi-Matrix $J$ des Systems (2.3.1) lautet allgemein:

$$J(\phi, \Omega) = \begin{pmatrix} 
0 & 1 \\ 
-\frac{mgl}{I}\cos\phi & -\frac{b}{I} 
\end{pmatrix}$$

Aus den Eigenwerten $\mu$ der linearisierten Matrix, bestimmt aus der charakteristischen Gleichung $\det(J - \mu \cdot E) = 0$, lässt sich das Stabilitätsverhalten exakt klassifizieren.

---

## Page 45

##### Fall 1: Untersuchung der unteren Ruhelage $F_1 = (0, 0)$

Setzt man die Koordinaten des unteren Fixpunkts in die Jacobi-Matrix ein, erhält man wegen $\cos(0) = 1$:

$$J(0,0) = \begin{pmatrix} 
0 & 1 \\ 
-\frac{mgl}{I} & -\frac{b}{I} 
\end{pmatrix}$$

Die charakteristische Gleichung lautet:

$$\mu^2 + \frac{b}{I}\mu + \frac{mgl}{I} = 0$$

Die Eigenwerte ergeben sich zu:

$$\mu_{1,2} = -\frac{b}{2I} \pm \sqrt{\left(\frac{b}{2I}\right)^2 - \frac{mgl}{I}}$$

Für kleine Dämpfungen ($b < 2\sqrt{mglI}$) ist der Term unter der Wurzel negativ. Die Eigenwerte sind komplex konjugiert mit einem negativen Realteil:

$$\mu_{1,2} = -\gamma \pm i\omega_d$$

Dies entspricht mathematisch einem **stabilen Fokus** (Spirale im Phasenraum). Alle nahen Trajektorien spiralisieren im Laufe der Zeit in den Ursprung hinein, wie experimentell in Abb. 2.3.1b gezeigt.

##### Fall 2: Untersuchung der oberen Ruhelage $F_2 = (\pi, 0)$

Setzt man die Koordinaten des oberen Fixpunkts ein, erhält man wegen $\cos(\pi) = -1$:

$$J(\pi,0) = \begin{pmatrix} 
0 & 1 \\ 
+\frac{mgl}{I} & -\frac{b}{I} 
\end{pmatrix}$$

Die Eigenwerte berechnen sich hier zu:

$$\mu_{1,2} = -\frac{b}{2I} \pm \sqrt{\left(\frac{b}{2I}\right)^2 + \frac{mgl}{I}}$$

Da der Term unter der Wurzel stets größer als $(b/2I)^2$ ist, ist die Wurzel reell und größer als der Betrag des Vorfaktors. Wir erhalten zwei reelle Eigenwerte mit unterschiedlichen Vorzeichen: $\mu_1 > 0$ und $\mu_2 < 0$. Ein solcher Fixpunkt wird als **Sattelpunkt** bezeichnet. Er ist instabil, da Trajektorien entlang der Richtung des positiven Eigenwerts exponentiell weggedrückt werden.

---

## Page 46

#### H.3 Analytische Näherung für das Amplitudenverhalten bei großen Ausschlägen

Wie in Abschnitt 2.2 dargelegt, wächst die Periodendauer $T$ des ungedämpften freien Pendels mit zunehmender Amplitude $\phi_m$. Eine exakte analytische Berechnung führt auf ein elliptisches Integral erster Gattung, das sich nicht geschlossen auflösen lässt:

$$T = 4 \sqrt{\frac{l}{2g}} \int_0^{\phi_m} \frac{d\phi}{\sqrt{\cos\phi - \cos\phi_m}} = T_0 \cdot \frac{2}{\pi} K\left(\sin\frac{\phi_m}{2}\right)$$

wobei $T_0 = 2\pi\sqrt{l/g}$ die Schwingungsdauer für infinitesimale Amplituden ist. Mittels einer Taylor-Reihenentwicklung der Funktion $K$ lässt sich eine präzise Näherungsformel für die Praxis ableiten:

$$T \approx T_0 \left( 1 + \frac{1}{4}\sin^2\left(\frac{\phi_m}{2}\right) + \frac{9}{64}\sin^4\left(\frac{\phi_m}{2}\right) + \dots \right)$$

Für Winkel bis zu $\phi_m \approx 90^\circ$ reicht meist die erste Korrekturstufe aus, die oft auch vereinfacht als Borda-Formel geschrieben wird:

$$T \approx T_0 \left( 1 + \frac{\phi_m^2}{16} \right) \quad (\phi_m \text{ in Radiant})$$

##### Vergleichstabelle für die Laborpraxis (Aufgabe 1):

Die folgende Tabelle zeigt die Abweichungen zwischen der linearen Näherung und der exakten nichtlinearen Periodendauer, die Sie in Aufgabe 1 numerisch verifizieren können.

| Amplitude $\phi_m$ (grad) | Amplitude $\phi_m$ (rad) | Relativer Faktor $T/T_0$ | Abweichung zur harmonischen Schwingung |
| --- | --- | --- | --- |
| $5^\circ$ | $0.0873$ | $1.0005$ | $+0.05\%$ |
| $20^\circ$ | $0.3491$ | $1.0077$ | $+0.77\%$ |
| $45^\circ$ | $0.7854$ | $1.0400$ | $+4.00\%$ |
| $90^\circ$ | $1.5708$ | $1.1803$ | $+18.03\%$ |
| $150^\circ$ | $2.6180$ | $1.7112$ | $+71.12\%$ |
| $175^\circ$ | $3.0543$ | $3.1642$ | $+216.42\%$ |

---

## Page 47

### Anhang I: Komplementäre Aufgabensammlung (Fortgeschrittenen-Niveau)

Die folgenden Zusatzaufgaben richten sich an Studierende höherer Semester und erfordern eine Kombination aus numerischer Simulation und analytischer Herleitung.

#### Aufgabe 7: Melnikov-Methode zur Chaos-Vorhersage

Für das getriebene Pendel lässt sich der Übergang von regulärer Dynamik zu chaotischem Verhalten näherungsweise analytisch eingrenzen. Die Melnikov-Methode untersucht das Schneiden der stabilen und instabilen Mannigfaltigkeiten (Separatrix-Splitting) unter dem Einfluss einer kleinen Störung (schwache Dämpfung $b$ und kleine Amplitude $A$).

1. Der kritische Zustand ist erreicht, wenn die Melnikov-Funktion $M(t_0)$ Nullstellen besitzt. Für das System (1.1.2) lautet die theoretische Bedingung für chaotische Ausreißer:
$$\frac{A}{b} \ge \frac{4g}{l \cdot \omega_A \cdot \cosh\left(\frac{\pi \omega_A}{2 \omega_0}\right)}$$


2. Überprüfen Sie diese analytische Grenze im Experimentierteil des Programms. Wählen Sie extrem kleine Werte für Dämpfung und Anregung und testen Sie, ob knapp unterhalb des kritischen Verhältnisses $A/b$ bereits chaotisches Verhalten detektiert werden kann.

#### Aufgabe 8: Untersuchung des fraktalen Einzugsgebiets

Koexistieren im System zwei Attraktoren (wie in Abschnitt 2.4, Abb. 2.4.3), entscheidet die Separatrix über das Schicksal der Trajektorie.

1. Nutzen Sie das Programm, um das Einzugsgebiet systematisch zu rastern. Variieren Sie dazu die Anfangsbedingungen $\phi_0$ im Bereich von $-180^\circ$ bis $+180^\circ$ und $\dot{\phi}_0$ im Bereich von $-5$ bis $+5$ in Schritten von $2^\circ$.
2. Markieren Sie manuell auf einem Millimeterpapier Punkte, die im kleinen Grenzzyklus enden, mit einem Kreuz und Punkte, die im großen Grenzzyklus enden, mit einem Kreis.
3. Analysieren Sie die Grenzlinie (Separatrix). Zeigt sie eine glatte Geometrie oder weist sie selbstähnliche, fraktale Strukturen auf? (Stichwort: *Fractal Basin Boundaries* [13]).

---

## Page 48

### Anhang J: Verzeichnis der numerischen Experimente und Systemparameter

Für eine schnelle Reproduktion der im Lernteil abgedruckten Grafiken sind nachfolgend alle exakten Parameterwerte und die zugehörigen Masken-Konfigurationen tabellarisch zusammengestellt.

#### J.1 Standard-Konfigurationen für das mathematische Pendel

In allen Beispielen des ersten Kapitels wurden, sofern nicht explizit anders angegeben, die folgenden mechanischen Grundparameter verwendet:

* Masse des Pendels $m = 0.2\text{ kg}$
* Länge der masselosen Stange $l = 0.25\text{ m}$
* Trägheitsmoment $I = m \cdot l^2 = 0.0125\text{ kg}\cdot\text{m}^2$
* Eigenkreisfrequenz der Linearnäherung $\omega_0 = \sqrt{g/l} \approx 6.264\text{ s}^{-1}$

##### Übersicht der Simulations-Datensätze:

| Abbildung im Text | Dämpfung $b$ (Nms) | Treiber $A$ (Nm) | Frequenz $\omega_A$ (1/s) | Anfangswerte $(\phi_0, \Omega_0)$ | Beobachtetes Phänomen |
| --- | --- | --- | --- | --- | --- |
| **Abb. 2.2.1a** | $0.0000$ | $0.0000$ | $0.0000$ | $(10^\circ, 0.0)$ | Harmonische Schwingung, Periode konstant |
| **Abb. 2.2.1b** | $0.0000$ | $0.0000$ | $0.0000$ | $(120^\circ, 0.0)$ | Nichtlineare Verzerrung, Periode vergrößert |
| **Abb. 2.2.2** | $0.0000$ | $0.0000$ | $0.0000$ | $(179.9^\circ, 0.0)$ | Extremes Plateau in der Nähe des Sattelpunkts |
| **Abb. 2.3.1b** | $0.0200$ | $0.0000$ | $0.0000$ | $(150^\circ, 2.0)$ | Phasenraumkontraktion auf Fixpunkt-Attraktor |
| **Abb. 2.4.1b** | $0.0200$ | $0.2900$ | $4.1760$ | $(0^\circ, 0.0)$ | Transienter Einschwingvorgang auf T1-Grenzzyklus |
| **Abb. 2.5.2b** | $0.0400$ | $0.5350$ | $4.1760$ | $(10^\circ, 0.0)$ | Periodenverdopplung (2 Punkte im Poincaré-Schnitt) |
| **Abb. 2.5.4b** | $0.0400$ | $0.5500$ | $4.1760$ | $(0^\circ, 0.0)$ | Deterministisches Chaos, Seltsamer Attraktor |

---

## Page 49

### Anhang K: Hinweise zur numerischen Präzision und Hardware-Einflüssen

Bei der Durchführung langandauernder chaotischer Simulationen (wie z.B. bei der Generierung des dichten Bifurkationsdiagramms in Abb. 2.6.1) kann es zu feinen Abweichungen zwischen den Ergebnissen verschiedener Computer kommen. Diese Eigenschaft ist im Wesentlichen keine Fehlfunktion der Software, sondern eine direkte Konsequenz der mathematischen Natur des Chaos.

#### K.1 Rundungsfehler-Verstärkung

Da im chaotischen Regime der Lyapunov-Exponent positiv ist ($\lambda > 0$), wird der Abstand zweier Trajektorien pro Zeiteinheit um den Faktor $e^{\lambda t}$ vergrößert. Dies gilt nicht nur für Abweichungen in den physikalischen Anfangsbedingungen (wie in Aufgabe 6), sondern auch für rein numerische Fehler.

Ein typischer PC berechnet Fließkommazahlen nach dem IEEE-754-Standard mit einer Genauigkeit von 64 Bit (Double Precision), was ca. 15-17 signifikanten Dezimalstellen entspricht. Der unvermeidbare Rundungsfehler beim kleinsten Integrationsschritt wird somit im chaotischen Bereich unaufhaltsam verstärkt. Nach einer charakteristischen Zeitdauer – der sogenannten **Lyapunov-Zeit** $t_L \approx 1/\lambda$ – ist der Fehler auf die Makroebene angewachsen. Ab diesem Moment beschreibt die berechnete Kurve nicht mehr die exakte physikalische Bahn des realen Systems, sondern eine sogenannte "Pseudotrajektorie".

> **Wichtiger Hinweis für die Lehre:**
> Dank des *Shadowing-Theorems* (Beschattungssatz) der Topologie ist das qualitative Ergebnis im Phasenraum (die fraktale Geometrie des seltsamen Attraktors und die statistischen Kennwerte) trotz der Rundungsfehler mathematisch absolut verlässlich. Es existiert für jede numerische Pseudotrajektorie eine echte, exakte Trajektorie zu leicht veränderten Anfangsbedingungen, die exakt denselben Pfad beschreibt.

---

## Page 50

#### K.2 Einfluss des mathematischen Koprozessors (FPU)

Sollten Sie Berechnungen auf Systemen ohne Koprozessor unter Verwendung des Emulationsparameters `/E` (siehe Abschnitt IV.4) durchführen, nutzt die Software interne 32-Bit-Routinen zur Nachbildung der mathematischen Operationen.

Dies führt dazu, dass der Punkt des Umschlagens in eine chaotische Phase im Bifurkationsdiagramm im Vergleich zu Berechnungen mit einer echten Hardware-FPU (Intel 80387) minimal verschoben sein kann. Für quantitative Vergleiche in Versuchsprotokollen wird daher dringend empfohlen, alle Messreihen innerhalb einer Arbeitsgruppe auf baugleichen Rechnerarchitekturen durchzuführen.

---

### Verzeichnis der im Text erwähnten Programmdateien

* `SCHWING.EXE` – Das ausführbare Hauptprogramm (Simulationsumgebung).
* `SCHWING.OVR` – Overlay-Datei für die Speicherverwaltung unter MS-DOS.
* `EGAVGA.BGI` – Grafiktreiber für EGA- und VGA-Bildschirme.
* `LERN.TXT` – Online-Hilfe und Begleittext für den Lernteil.
* `SETUP.DAT` – Standard-Parameterdatei (wird automatisch generiert).
* `READ.ME` – Aktuelle Last-Minute-Hinweise zur Hardwarekompatibilität.

---

**Ende des technischen Anhangs.**
*Dieses Begleitmaterial ist integraler Bestandteil des Softwarepakets "Nichtlineare Dynamik".*
*Printed in Germany 1995.*
