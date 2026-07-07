
## Page 21

#### vi. Quantitative Charakterisierung fraktaler Strukturen (Kapap-Dimension)

Um die geometrische Struktur seltsamer Attraktoren zu quantifizieren, reicht der klassische Dimensionsbegriff nicht aus. Man nutzt stattdessen die Definition der Renyi-Dimensionen $D_q$. Die bekanntesten Spezialfälle sind:

1. **Kapazität- oder Box-Counting-Dimension ($D_0$):**
Überdeckt man das geometrische Objekt im Phasenraum mit Hyperwürfeln der Kantenlänge $\epsilon$ und ist $N(\epsilon)$ die Anzahl der Würfel, die mindestens einen Punkt des Attraktors enthalten, so gilt:
$$D_0 = \lim_{\epsilon \rightarrow 0} \frac{\ln N(\epsilon)}{\ln(1/\epsilon)}.$$


2. **Informationsdimension ($D_1$):**
Sie berücksichtigt zusätzlich die relative Häufigkeit (Wahrscheinlichkeit $p_i$) mit der die Trajektorie die einzelnen Würfel $i$ besucht:
$$D_1 = \lim_{\epsilon \rightarrow 0} \frac{\sum_{i=1}^{N(\epsilon)} p_i \ln p_i}{\ln \epsilon}.$$


3. **Korrelationsdimension ($D_2$):**
Diese läßt sich numerisch besonders effizient über das Korrelationsintegral $C(\epsilon)$ nach Grassberger und Procaccia bestimmen:
$$D_2 = \lim_{\epsilon \rightarrow 0} \frac{\ln C(\epsilon)}{\ln \epsilon},$$


wobei $C(\epsilon)$ die relative Anzahl der Punktpaare angibt, deren gegenseitiger Abstand kleiner als $\epsilon$ ist. Für alle seltsamen Attraktoren gilt die Ungleichungskette $D_2 \le D_1 \le D_0$ mit nicht-ganzzahligen Werten.

---

## Page 22

### Kapitel IV: Benutzerdokumentation und Programminstallation

#### 1. Systemvoraussetzungen

Das Simulationsprogramm "Nichtlineare Schwingungen" ist lauffähig auf IBM-PC-kompatiblen Rechnern unter MS-DOS (Version 5.0 oder höher).

Für eine einwandfreie Funktion wird folgende Hardwarekonfiguration empfohlen:

* Prozessor: Intel 80386 oder höher (ein mathematischer Koprozessor 80387 wird dringend empfohlen, um die Rechenzeiten für die numerische Integration zu minimieren).
* Arbeitsspeicher: Mindestens 640 KB konventioneller Speicher.
* Grafikkarte: VGA-Grafikkarte (640x480 Pixel, 16 Farben).
* Eingabegeräte: Tastatur; eine Microsoft-kompatible Maus wird unterstützt und erleichtert die interaktive Bedienung der Menüs erheblich.

#### 2. Installation des Programms

1. Legen Sie die mitgelieferte 3.5"-Diskette in das entsprechende Laufwerk (z.B. `A:`) ein.
2. Wechseln Sie auf dieses Laufwerk und erstellen Sie auf Ihrer Festplatte (`C:`) ein neues Verzeichnis:
```
MD C:\CHAOS

```


3. Kopieren Sie alle Dateien der Diskette in dieses Verzeichnis:
```
COPY A:\*.* C:\CHAOS /V

```


4. Starten Sie das Programm aus dem Verzeichnis `C:\CHAOS` heraus durch Eingabe von:
```
SCHWING

```



---

## Page 23

#### 3. Programmbedienung und Menüstruktur

##### 3.1 Das Hauptmenü

Nach dem Startbildschirm erscheint das Hauptmenü des Programms. Am oberen Bildschirmrand befindet sich die Menüleiste, die per Maus oder durch Drücken der `Alt`-Taste kombiniert mit dem rot hervorgehobenen Anfangsbuchstaben des jeweiligen Menüpunkts aktiviert werden kann.

Das Hauptmenü gliedert sich in folgende Bereiche:

* **System:** Auswahl des physikalischen Modells (Pendel, Federschwinger, Pohlsches Rad, Parametrisches Pendel).
* **Parameter:** Eingabe der physikalischen Systemkonstanten (Massen, Längen, Dämpfung, Anregungsamplitude und -frequenz).
* **Anfangswerte:** Festlegung der Startbedingungen im Phasenraum.
* **Rechnung:** Steuerung der numerischen Integration (Runge-Kutta-Verfahren), Wahl der Schrittweite und Integrationsdauer.
* **Darstellung:** Umschalten der Grafikmodi (Zeitverlauf, Phasenraum, Stroboskop-Schnitt, Bifurkationsdiagramm).

##### 3.2 Dateneingabe in Masken

Die numerischen Werte für Parameter und Anfangsbedingungen werden über Eingabemasken editiert. Innerhalb einer Maske können Sie sich mit den Pfeiltasten (`↑`, `↓`) oder der `Tab`-Taste vorwärtsbewegen. Ein eingegebener Wert wird mit `Enter` bestätigt. Durch Drücken von `F10` werden alle Werte der aktuellen Maske übernommen und die Berechnung vorbereitet. `Esc` bricht die Eingabe ab und stellt die alten Werte wieder her.

---

## Page 24

##### 3.3 Durchführung von numerischen Experimenten

Nachdem ein System ausgewählt und die gewünschten Parameter gesetzt wurden, startet der Menüpunkt **Rechnung -> Start** die Simulation. Am unteren Bildschirmrand erscheint ein Statusbalken, der den Fortschritt der Integration anzeigt.

Während einer laufenden Berechnung kann die grafische Ausgabe durch Drücken der `Leertaste` jederzeit unterbrochen werden. Es öffnet sich ein interaktives Untermenü, das folgende Optionen bietet:

* **Abbruch:** Beendet die aktuelle Integration und kehrt zum Menü zurück.
* **Weiter:** Setzt die Berechnung an der Unterbrechungsstelle fort.
* **Parameter ändern:** Erlaubt eine Modifikation der Anregungsamplitude im laufenden Betrieb, um transiente Übergänge direkt visuell zu verfolgen.

##### 3.4 Spezielle Darstellungsmodi

###### 3.4.1 Der Stroboskop-Modus

Um die stroboskopische Abbildung (Poincaré-Schnitt) zu aktivieren, wählen Sie im Menü **Darstellung -> Stroboskop**. Das Programm fordert Sie zur Eingabe der Phase $\psi_0$ auf (Standardwert ist `0.0`). Während der Integration wird die kontinuierliche Trajektorie ausgeblendet, und es werden nur noch die diskreten Punkte im Takt der Erregerperiode gezeichnet.

###### 3.4.2 Die Option "Zweig ON"

Für die Aufnahme von Hysteresekurven und Resonanzdiagrammen (wie in Abschnitt 2.4 beschrieben) besitzt das Programm die Option **Zweig**. Ist diese Option auf **ON** gesetzt, so werden bei einer Parameteränderung (z.B. Erhöhung der Erregerfrequenz $\omega_A$) die Endwerte der letzten Berechnung automatisch als Anfangswerte für den neuen Simulationslauf übernommen. Dies verhindert das Abklingen neuer transienter Vorgänge aus der Ruhelage heraus.

---

## Page 25

#### 4. Fehlermeldungen und deren Behebung

* **Error 102: Math Co-Processor not found.**
Das Programm versucht, auf die Fließkomma-Hardware zuzugreifen. Falls Ihr System keinen mathematischen Koprozessor besitzt, starten Sie das Programm stattdessen mit dem Parameter `/E` (`SCHWING /E`), um die Software-Emulation der Fließkomma-Arithmetik zu erzwingen. Die Rechenzeit erhöht sich dadurch signifikant.
* **Error 204: Division by zero / Floating point overflow.**
Dieser Fehler tritt auf, wenn die Integrationsschrittweise $dt$ im Menü **Rechnung** zu groß gewählt wurde und das numerische Verfahren divergiert (insbesondere im chaotischen Regime oder in der Nähe der Separatrix). Reduzieren Sie in diesem Fall den Wert für $dt$ um den Faktor 10 (z.B. von `0.01` auf `0.001`) und starten Sie die Berechnung erneut.

---

## Page 26

### Kapitel V: Literaturverzeichnis und Referenzen

[1] Smith, H. J.: *Nonlinear Oscillations and Chaotic Pendulums.* Journal of Applied Physics, Vol. 45, pp. 112-120, 1988.

[2] Müller, P.: *Experimentelle Mechanik und nichtlineare Dynamik.* Teubner Verlag, Stuttgart, 1991.

[3] Richter, R.; et al.: *Bistability and Hysteresis in Driven Pendulum Systems.* Physical Review A, Vol. 33, No. 4, pp. 2415-2422, 1986.

[4] Schmidt, G.: *Schwingungen nichtlinearer Systeme.* Akademie-Verlag, Berlin, 1975.

[5] Foroni, M.: *Chaotic Motions of a Forced Pendulum.* American Journal of Physics, Vol. 54, pp. 748-753, 1986.

[6] Duffing, G.: *Erzwungene Schwingungen bei veränderlicher Eigenfrequenz.* Vieweg, Braunschweig, 1918.

[7] Hayashi, C.: *Nonlinear Oscillations in Physical Systems.* McGraw-Hill, New York, 1964.

[8] Moon, F. C.: *Chaotic Vibrations: An Introduction for Applied Scientists and Engineers.* John Wiley & Sons, New York, 1987.

[9] Kapitza, P. L.: *Dynamic Stability of a Pendulum with an Oscillating Suspension Point.* Zh. Eksp. Teor. Fiz., Vol. 21, pp. 588-597, 1951.

[10] Blackburn, J. A.; et al.: *Experimental Study of a Parametrical Driven Pendulum.* Physica D, Vol. 60, pp. 210-216, 1992.

[11] Stoker, J. J.: *Nonlinear Vibrations in Mechanical and Electrical Systems.* Interscience Publishers, New York, 1950.

[12] Nayfeh, A. H.; Mook, D. T.: *Nonlinear Oscillations.* Wiley-Interscience, New York, 1979.

---

## Page 27

[13] Guckenheimer, J.; Holmes, P.: *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields.* Springer-Verlag, New York, 1983.

[14] Thompson, J. M. T.; Stewart, H. B.: *Nonlinear Dynamics and Chaos.* John Wiley & Sons, Chichester, 1986.

[15] Lichtenberg, A. J.; Lieberman, M. A.: *Regular and Stochastic Motion.* Springer-Verlag, New York, 1983.

[16] Bergé, P.; Pomeau, Y.; Vidal, C.: *Order within Chaos: From a Deterministic Approach to Turbulence.* John Wiley & Sons, New York, 1984.

[17] Feigenbaum, M. J.: *Quantitative Universality for a Class of Nonlinear Transformations.* Journal of Statistical Physics, Vol. 19, pp. 25-52, 1978.

[18] Cvitanović, P.: *Universality in Chaos.* Adam Hilger, Bristol, 1984.

[19] Schuster, H. G.: *Deterministic Chaos: An Introduction.* Physik-Verlag, Weinheim, 1984.

[20] Pomeau, Y.; Manneville, P.: *Intermittent Transition to Turbulence in Dissipative Dynamical Systems.* Communications in Mathematical Physics, Vol. 74, pp. 189-197, 1980.

[21] Ruelle, D.; Takens, F.: *On the Nature of Turbulence.* Communications in Mathematical Physics, Vol. 20, pp. 167-192, 1971.

[22] Landau, L. D.; Lifschitz, E. M.: *Lehrbuch der Theoretischen Physik, Band I: Mechanik.* Akademie-Verlag, Berlin, 1990.

---

## Page 28

### Sachwortverzeichnis

A

* Anfangsbedingungen 3, 6, 7, 11, 12, 13, 14, 16, 17, 24
* Anregungsamplitude 5, 12, 13, 14, 22, 24
* Anregungsfrequenz 2, 4, 12, 22
* Attraktor 10, 11, 12, 13, 14, 16, 17, 19
* Autonomes System 5, 6, 7, 18

B

* Bifurkationsdiagramm 12, 13, 23
* Bistabilität 11, 13, 17
* Box-Counting-Dimension 21

C

* Chaos, deterministisches 12, 13, 14, 25

D

* Dämpfung 1, 2, 4, 10, 11, 12, 16, 22
* Dämpfungskoeffizient 2, 4, 16
* Differentialgleichung 1, 2, 3, 4, 5, 7, 10, 11, 15, 18
* Dissipatives System 10, 11, 19
* Divergenz 19
* Duffing-Oszillator 3, 4, 17

E

* Einzugsgebiet 14
* Erregerfrequenz 12, 13, 14, 15, 17, 24

F

* Federschwinger 1, 3, 4, 17, 23
* Feigenbaum-Szenario 12, 13, 17
* Fixpunkt 8, 10, 11, 16
* Fraktale Dimension 12, 21

---

## Page 29

G

* Gleichgewichtspunkt 8
* Gleitreibung 3, 20
* Grenzzyklus 11, 12, 13, 20

I

* Informationsdimension 21
* Intermittenz 13

K

* Kapitza-Pendel 15
* Korrelationsdimension 21

L

* Linearität 1, 3, 5, 7, 10, 11, 15, 18
* Liouville, Satz von 19
* Lyapunov-Exponent 14, 17

M

* Mathieusche Gleichung 15

N

* Nichtautonomes System 5, 6, 18

P

* Parametrische Resonanz 15
* Pendel, mathematisches 1, 2, 5, 6, 7, 8, 11, 12, 13, 15, 16, 17
* Phasenbahn 6, 13, 14
* Phasenebene 6, 7, 9, 14
* Phasenraum 3, 6, 7, 9, 11, 16, 18, 19, 21
* Pohlsches Rad 1, 4, 23
* Poincaré-Abbildung 19, 20, 24

Q

* Quasiperiodizität 13, 20

---

## Page 30

R

* Reibungskraft 2, 3, 7, 10
* Resonanzkurve 12, 13, 14, 17, 24
* Rotation 2, 9, 14, 15, 16
* Runge-Kutta-Verfahren 23

S

* Schmetterlingseffekt 14
* Schwingungsdauer 7, 14, 16
* Seltsamer Attraktor 12, 13, 20, 21
* Separatrix 9, 14, 16, 25
* Sprungphänomen 11, 13, 17
* Stroboskopische Abbildung 14, 15, 17, 20, 24
* Superpositionsprinzip 18

T

* Torus 13, 18, 20
* Trajektorie 6, 7, 9, 11, 12, 13, 14, 16, 19, 24
* Transiente Bewegung 12, 24

U

* Unwucht 4

V

* Volumenkontraktion 11, 19

W

* Weg ins Chaos 12, 13, 17
* Wirbelstrombremse 3, 5

Z

* Zustandsvariable 3, 5, 6, 7, 12
* Zweig-Option 13, 17, 24
