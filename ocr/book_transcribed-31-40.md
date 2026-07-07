
## Page 31

### Anhang A: Numerische Integrationsverfahren im Vergleich

In der rechnergestützten Physik dynamischer Systeme spielt die Wahl des Integrationsalgorithmus eine entscheidende Rolle. Da nichtlineare Differentialgleichungen in der Regel keine analytischen Lösungen besitzen, müssen die Trajektorien durch diskrete Zeitschritte approximiert werden. Das Programm nutzt standardmäßig ein explizites Runge-Kutta-Verfahren 4. Ordnung (RK4).

#### A.1 Das Euler-Verfahren (Ordnung 1)

Das einfachste Verfahren ist das Euler-Vorwärts-Verfahren. Für ein System $\dot{\vec{x}} = \vec{F}(\vec{x}, t)$ lautet die Iterationsvorschrift mit der Schrittweite $\Delta t$:

$$\vec{x}_{k+1} = \vec{x}_k + \Delta t \cdot \vec{F}(\vec{x}_k, t_k)$$

Dieses Verfahren ist für nichtlineare oder chaotische Oszillatoren gänzlich ungeeignet, da der lokale Abbruchfehler quadratisch mit $\mathcal{O}(\Delta t^2)$ und der globale Fehler linear mit $\mathcal{O}(\Delta t)$ anwächst. Bei konservativen Systemen führt dies zu einer künstlichen Energieerzeugung (die Trajektorien spiralisieren nach außen).

#### A.2 Das Runge-Kutta-Verfahren (Ordnung 4)

Das RK4-Verfahren mathematisch kompensiert diese Defizite durch die Berechnung von vier Hilfsvektoren (Steigungen) pro Zeitschritt:

$$\begin{aligned}
\vec{k}_1 &= \vec{F}(\vec{x}_k, t_k) \\
\vec{k}_2 &= \vec{F}\left(\vec{x}_k + \frac{\Delta t}{2}\vec{k}_1, t_k + \frac{\Delta t}{2}\right) \\
\vec{k}_3 &= \vec{F}\left(\vec{x}_k + \frac{\Delta t}{2}\vec{k}_2, t_k + \frac{\Delta t}{2}\right) \\
\vec{k}_4 &= \vec{F}(\vec{x}_k + \Delta t \vec{k}_3, t_k + \Delta t)
\end{aligned}$$

Der neue Zustand berechnet sich als gewichtetes Mittel:

$$\vec{x}_{k+1} = \vec{x}_k + \frac{\Delta t}{6} \left(\vec{k}_1 + 2\vec{k}_2 + 2\vec{k}_3 + \vec{k}_4\right)$$

Der globale Fehler liegt in der Ordnung $\mathcal{O}(\Delta t^4)$. Dies erlaubt deutlich größere Schrittweiten bei stabiler Phasenraumdynamik.

---

## Page 32

### Anhang B: Programmstruktur und Quellcode-Ausschnitte

Das Simulationsprogramm wurde in Turbo Pascal 7.0 implementiert, um eine direkte Hardwarenähe und schnelle Grafikausgabe über das BGI-Interface (Borland Graphics Interface) unter MS-DOS zu gewährleisten. Nachfolgend ist der zentrale Kern der mathematischen Iterationsschleife dokumentiert.

```pascal
Procedure RK4Step(Var Phi, Omega: Real; dt: Real; t: Real);
Var
  k1_p, k1_o, k2_p, k2_o, k3_p, k3_o, k4_p, k4_o: Real;
  
  Function Accel(p, o: Real; time: Real): Real;
  Begin
    { Berechnung der Winkelbeschleunigung gemäss Gleichung 1.1.2 }
    Accel := -(b/I_moment)*o - (m*g*l/I_moment)*Sin(p) + (A_amp/I_moment)*Cos(omega_A*time);
  End;

Begin
  k1_p := Omega;
  k1_o := Accel(Phi, Omega, t);

  k2_p := Omega + 0.5 * dt * k1_o;
  k2_o := Accel(Phi + 0.5 * dt * k1_p, Omega + 0.5 * dt * k1_o, t + 0.5 * dt);

  k3_p := Omega + 0.5 * dt * k2_o;
  k3_o := Accel(Phi + 0.5 * dt * k2_p, Omega + 0.5 * dt * k2_o, t + 0.5 * dt);

  k4_p := Omega + dt * k3_o;
  k4_o := Accel(Phi + dt * k3_p, Omega + dt * k3_o, t + dt);

  Phi   := Phi   + (dt / 6.0) * (k1_p + 2.0*k2_p + 2.0*k3_p + k4_p);
  Omega := Omega + (dt / 6.0) * (k1_o + 2.0*k2_o + 2.0*k3_o + k4_o);
  
  { Winkel auf das Intervall [-Pi, +Pi] normieren }
  If Phi > Pi Then Phi := Phi - 2.0 * Pi;
  If Phi < -Pi Then Phi := Phi + 2.0 * Pi;
End;

```

---

## Page 33

### Anhang C: Ergänzende Laborübungen für Realexperimente

Die numerische Simulation ist ein mächtiges Werkzeug, gewinnt jedoch massiv an Wert, wenn sie mit echten physikalischen Messungen verglichen wird. Das in der Software modellierte "Pohlsche Rad" entspricht dem Standard-Versuchsaufbau vieler physikalischer Praktika.

![Figure C.1: Laboratory setup diagram of a Pohl's torsion pendulum equipped with an eddy current brake, a driving motor, and an angle sensor.]
Abb. C.1: Laboraufbau des Drehpendels nach Pohl

#### Messwerterfassung und Kalibrierung

Um quantitative Vergleiche mit dem Simulationsprogramm anzustellen, müssen die Systemparameter des realen Apparats präzise bestimmt werden:

1. **Trägheitsmoment $I$:** Entfernen Sie die Spiralfeder und bestimmen Sie das Trägheitsmoment des nackten Rades durch Messung der Beschleunigung mittels einer bekannten angehängten Masse.
2. **Dämpfungskonstante $b$:** Lassen Sie das freie Rad ohne periodische Anregung auslenken und zeichnen Sie das Abklingverhalten auf. Bestimmen Sie das logarithmische Dekrement $\Lambda$:
$$\Lambda = \ln\left(\frac{x_n}{x_{n+1}}\right) = \gamma \cdot T_d.$$


3. **Federkonstante $d$:** Messen Sie das statische Drehmoment bei verschiedenen Auslenkwinkeln $\phi$, um die Linearität der Spiralfeder zu überprüfen.

Nachdem Sie die Parameter ermittelt und in die Eingabemaske des Programms eingetragen haben, vergleichen Sie die berechneten Hysteresekurven mit den real gemessenen Amplitudensprüngen aus Aufgabe 4.

---

## Page 34

### Anhang D: Kontrollfragen zur Selbstüberprüfung

Testen Sie Ihr Verständnis des gelernten Stoffes anhand der folgenden Fragestellungen. Die Antworten lassen sich direkt aus dem Text der Kapitel I und III ableiten.

1. Warum können sich Trajektorien im dreidimensionalen Phasenraum $(\phi, \Omega, \psi)$ des getriebenen Pendels niemals schneiden, während ihre Projektionen auf die $(\phi, \Omega)$-Ebene Schnittpunkte aufweisen dürfen?
2. Welcher mathematische Zusammenhang besteht zwischen dem Dämpfungskoeffizienten eines dissipativen Systems und der Kontraktion seines Phasenraumvolumens?
3. Nennen Sie den fundamentalen Unterschied zwischen einem fixen Attraktor und einem seltsamen Attraktor bezüglich ihrer geometrischen Dimension.
4. Was versteht man unter einem "periodischen Fenster" innerhalb eines Bifurkationsdiagramms?
5. Warum bricht das Superpositionsprinzip bei der Duffing-Differentialgleichung zusammen? Welche Terme verursachen dies?
6. Erklären Sie, wie eine stroboskopische Abbildung dazu beiträgt, ein unübersichtliches, chaotisches Trajektorienknäuel im Phasenraum grafisch zu entflechten und strukturell zu analysieren.

---

## Page 35

### Anhang E: Lösungen zu den Kontrollfragen

1. **Antwort:** Das autonome Gleichungssystem im dreidimensionalen Raum besitzt aufgrund des Existenz- und Eindeutigkeitssatzes für Differentialgleichungen für jeden Punkt genau eine eindeutige Lösung. Ein Schnittpunkt würde bedeuten, dass die Bewegung an dieser Stelle zwei verschiedene Fortsetzungen hätte, was unmöglich ist. Bei der 2D-Projektion fällt die explizite Zeitkomponente $\psi$ weg; unterschiedliche Punkte im 3D-Raum, die sich nur in der Zeitphase unterscheiden, können somit auf denselben 2D-Punkt abgebildet werden.
2. **Antwort:** Gemäß dem Satz von Liouville ist die Divergenz des Vektorfeldes proportional zur Rate der Volumenänderung. Da für das Pendel $\text{div} \vec{F} = -b/I$ gilt, nimmt das Volumen exponentiell ab mit $V(t) = V(0)e^{-(b/I)t}$. Je größer die Dämpfung $b$, desto schneller schrumpft das Phasenraumvolumen.
3. **Antwort:** Ein stabiler Fixpunkt-Attraktor besitzt die euklidische Dimension 0 (einzelner Punkt). Ein seltsamer Attraktor hingegen besitzt eine nicht-ganzzahlige, fraktale Dimension (z.B. zwischen 1 und 2), da er eine unendlich oft gefaltete, selbstähnliche geometrische Struktur aufweist.
4. **Antwort:** Ein periodisches Fenster ist ein schmaler Parameterbereich innerhalb des chaotischen Regimes eines Bifurkationsdiagramms, in dem die Dynamik plötzlich wieder vollständig regulär und periodisch wird (z.B. stabile Schwingung der Periode 3), bevor sie durch erneute Periodenverdopplungen wieder ins Chaos zerfällt.
5. **Antwort:** Aufgrund des nichtlinearen Terms $dx^3$ (kubische Rückstellkraft der Feder). Bildet man die Summe zweier Lösungen $x_1$ und $x_2$, gilt $(x_1+x_2)^3 \neq x_1^3 + x_2^3$, wodurch die Linearkombination keine Lösung der Gleichung mehr darstellt.
6. **Antwort:** Indem das System nur exakt einmal pro Erregerperiode "fotografiert" wird, fallen alle periodischen Trajektorien, die synchron zum Treiber verlaufen, auf einen einzigen Punkt zusammen. Komplexe chaotische Strukturen zeigen im kontinuierlichen Phasenraum nur ein undurchsichtiges Linienknäuel, entfalten in der stroboskopischen Abbildung jedoch ihre klar strukturierte fraktale Geometrie des seltsamen Attraktors.

---

## Page 36

### Kapitel VI: Fortgeschrittene computergestützte Analysemethoden

#### 1. Die Berechnung des maximalen Lyapunov-Exponenten nach Benettin

Um den in Abschnitt 2.7 qualitativ beschriebenen Lyapunov-Exponenten numerisch exakt zu bestimmen, versagt die simple Überwachung zweier Trajektorien nach längerer Zeit. Da der Phasenraum beschränkt ist (z.B. $\phi \in [-\pi, \pi]$), können die Trajektorien nicht unendlich weit auseinanderlaufen; die exponentielle Divergenz sättigt im Durchmesser des Attraktors ab (vgl. Abb. 2.7.1b).

Der Algorithmus nach Benettin et al. [23] löst dieses Problem durch fortlaufende Renormierung:

![Figure 1.1: Geometric illustration of the Benettin renormalization algorithm for tracking the exponential separation of two nearby chaotic trajectories over discrete time steps.]
Abb. 1.1: Prinzip der Renormierung nach Benettin

1. Starten Sie die Referenztrajektorie $\vec{x}_0(t)$ und eine Testtrajektorie $\vec{x}_1(t)$ im Abstand $d_0 = \|\vec{x}_1(0) - \vec{x}_0(0)\| \ll 1$.
2. Integrieren Sie beide Systeme über ein kurzes Zeitintervall $\tau$. Der Abstand ist nun auf $d_1 = \|\vec{x}_1(\tau) - \vec{x}_0(\tau)\|$ angewachsen.
3. Der lokale Zuwachs wird im Akkumulator erfasst.
4. **Renormierungsschritt:** Setzen Sie die Testtrajektorie exakt in der Richtung des Differenzvektors auf den ursprünglichen Abstand $d_0$ zurück:
$$\vec{x}_1^{\text{neu}}(\tau) = \vec{x}_0(\tau) + \frac{d_0}{d_1} \left(\vec{x}_1(\tau) - \vec{x}_0(\tau)\right).$$


5. Wiederholen Sie die Schritte 2 bis 4 insgesamt $M$-mal. Der maximale Lyapunov-Exponent ergibt sich im Limes zu:
$$\lambda_{\max} = \frac{1}{M \cdot \tau} \sum_{k=1}^M \ln\left(\frac{d_k}{d_0}\right).$$



---

## Page 37

#### 2. Spektralanalyse (Fast Fourier Transformation)

Ein unverzichtbares Werkzeug zur Unterscheidung zwischen quasiperiodischen und echt chaotischen Schwingungen ist die Fouriertransformation des Zeitsignals. Das Programm erlaubt es, die diskreten Werte der Winkelgeschwindigkeit $\Omega(t)$ mittels des FFT-Algorithmus nach Cooley und Tukey in den Frequenzraum zu überführen.

Aus dem kontinuierlichen Signal werden $N$ Stützstellen (wobei $N$ eine Zweierpotenz sein muss, z.B. $N = 1024$) extrahiert und das Leistungsspektrum $P(\omega)$ berechnet:

$$P(\omega) = \left| \frac{1}{N} \sum_{k=0}^{N-1} \Omega(t_k) e^{-i \omega t_k} \right|^2$$

##### Interpretation der Spektren:

* **Periodische Bewegung:** Das Spektrum zeigt scharfe, diskrete Linien (Delta-Peaks) exakt bei der Erregerfrequenz $\omega_A$ sowie deren ganzzahligen Oberwellen ($2\omega_A, 3\omega_A, \dots$) bzw. Subharmonischen im Falle von Periodenverdopplungen (z.B. $\omega_A/2, \omega_A/4$).
* **Quasiperiodische Bewegung:** Es treten mehrere scharfe Peaks auf, deren Frequenzverhältnisse irrationale Zahlen bilden. Es gibt keine gemeinsame Grundfrequenz.
* **Chaotische Bewegung:** Das Spektrum verliert seine diskrete Struktur. Es zeigt einen kontinuierlichen, breitbandigen Untergrund (Rauschteppich), oft kombiniert mit einem $1/f^\alpha$-Abfall zu höheren Frequenzen hin. Einzelne Peaks der treibenden Kraft können dem kontinuierlichen Spektrum überlagert sein.

---

## Page 38

### Kapitel VII: Technische Dokumentation des Simulationspakets

#### 1. Struktur der Datendateien (`*.DAT`)

Das Programm speichert Konfigurationen, Trajektorienpunkte und stroboskopische Schnitte in binären oder ASCII-basierten Datendateien ab, um eine Nachbereitung mit externen Grafikprogrammen (wie z.B. Gnuplot oder Origin) zu ermöglichen.

##### Aufbau einer Parameter-Konfigurationsdatei (`SETUP.DAT`):

Die Datei wird als reine Textdatei (ASCII) zeilenweise eingelesen. Jede Zeile enthält einen numerischen Wert gefolgt von einem Kommentarbezeichner.

```text
0.2000    ; Masse m in kg
0.2500    ; Pendellaenge l in m
0.0200    ; Daempfung b in Nms
0.2250    ; Anregungsamplitude A in Nm
4.1760    ; Erregerkreisfrequenz omega_A in 1/s
0.0000    ; Anfangswinkel Phi_0 in rad
0.0000    ; Anfangsgeschwindigkeit Omega_0 in rad/s
0.0100    ; Integrationsschrittweite dt in s
2000      ; Anzahl der maximal zu berechnenden Schritte
1         ; Flag fuer Darstellung (1=Phasenraum, 2=Stroboskop)

```

##### Aufbau einer Trajektoriendatei (`TRAJ.DAT`):

Beim Aktivieren der Export-Funktion schreibt das Programm die berechneten Bahnpunkte spaltenweise als Fließkommazahlen im Exponentialformat:

```text
# Zeit t [s]    Phi [rad]       Omega [rad/s]
0.000000e+00    0.000000e+00    0.000000e+00
1.000000e-02    1.245000e-04    2.489000e-02
2.000000e-02    4.978000e-04    4.975000e-02
3.000000e-02    1.119200e-03    7.454000e-02

```

---

## Page 39

#### 2. Hardwarenahe Grafikprogrammierung unter MS-DOS

Um flüssige Animationen der Pendelbewegung auf damaligen Systemen ohne dedizierte 3D-Beschleuniger zu realisieren, nutzt die Software die Technik des **Page-Flippings** (Doppelpufferung). VGA-Grafikkarten im Modus $12\text{h}$ ($640 \times 480$ Pixel, 16 Farben) verfügen über mehrere Speicherbänke im Videospeicher (VRAM).

Während die aktuelle Trajektorie auf der sichtbaren Grafikseite (Video-Page 0) vom Benutzer betrachtet wird, zeichnet der Berechnungsalgorithmus im Hintergrund unbemerkt die nächste Trajektorienänderung auf die unsichtbare Grafikseite (Video-Page 1). Nach Abschluss des Rechenschritts wird dem Grafikcontroller per Registerbefehl signalisiert, die Speicheradresse der anzuzeigenden Seite umzuschalten:

```pascal
Procedure SwapBuffers;
Begin
  { Portzugriff auf das VGA-Register zur Umschaltung der Startadresse }
  Port[$3D4] := $0C;
  Port[$3D5] := Hi(CurrentPageAddress);
  Port[$3D4] := $0D;
  Port[$3D5] := Lo(CurrentPageAddress);
  { Seiten-Indizes invertieren }
  CurrentPageAddress := CurrentPageAddress Xor $2000;
End;

```

Durch diese Methode wird ein störendes Bildschirmflackern vollständig eliminiert, da der Bildaufbau synchron zum vertikalen Rückstrahlflug (Vertical Retrace) des Monitors durchgeführt werden kann.

---

## Page 40

### Nachwort und Ausblick

Das Studium von Ordnung und Chaos bei nichtlinearen Schwingungen markiert einen Paradigmenwechsel in den Naturwissenschaften. Noch bis weit in das 20. Jahrhundert hinein war die Vorstellung weit verbreitet, dass eine exakte deterministische mathematische Beschreibung eines Systems automatisch auch eine langfristige Vorhersagbarkeit impliziert. Die Entdeckung des deterministischen Chaos hat diese Annahme grundlegend widerlegt.

Wie Sie im Rahmen dieses Selbststudienprogramms und der numerischen Experimente selbst nachvollziehen konnten, erzeugen bereits einfachste mechanische Systeme mit nur einem einzigen nichtlinearen Term eine Komplexität, die sich jeder analytischen Berechnung entzieht. Die geometrische Schönheit seltsamer Attraktoren und die universelle mathematische Struktur von Bifurkationskaskaden zeigen jedoch, dass auch im scheinbaren Chaos strenge Gesetzmäßigkeiten herrschen.

Die in diesem Heft behandelten Methoden – vom Phasenportrait über die Poincaré-Abbildung bis hin zu den Lyapunov-Exponenten – bilden das Fundament der modernen Theorie dynamischer Systeme. Sie finden heute nicht mehr nur in der Mechanik Anwendung, sondern sind unverzichtbar bei der Modellierung von Wetterphänomenen, elektronischen Schaltkreisen, chemischen Reaktionen (Belousov-Zhabotinsky-Reaktion) sowie in der Populationsdynamik und der Ökonomie.

Möge dieses Programm Ihr Interesse an den faszinierenden Strukturen der nichtlinearen Welt geweckt haben.

---

**Ende des Begleithefts.**
*Copyright © 1995 – Soft-Physics Publishing GmbH, Berlin.*
*Alle Rechte vorbehalten.*

---

Damit sind alle von Ihnen hochgeladenen Seiten vollständig und buchstabengetreu transkribiert. Wenn Sie noch Fragen zu den physikalischen Modellen oder Algorithmen haben, stehe ich Ihnen gerne zur Verfügung!
