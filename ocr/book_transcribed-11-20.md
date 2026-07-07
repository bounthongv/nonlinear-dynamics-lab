
## Page 11

![Figure 2.5.2b: Left: Double-loop phase trajectory. Right: Stroboskopische Abbildung yielding exactly two distinct dots.]
Abb. 2.5.2b

Die Abbildungen 2.5.3 zeigen eine Schwingung mit der Periodizität vier. Bei weiterer Vergrößerung des Parameters $A$ verdoppelt sich die Periode weiter (Periode 8, 16 ...). Diese Folge von Periodenverdopplungen (Feigenbaum-Szenario, siehe auch 2.6) führt schließlich zu einer chaotischen Bewegung (Abb. 2.5.4).

![Figure 2.5.3a: Waveform plot of angle \phi and angular velocity \dot{\phi} vs. time showing period-4 oscillation with complex, repeating sub-peaks.]
Abb. 2.5.3a: Zeit-Funktionen (2.5.3a), Phasenbahn und stroboskopische Abbildung (2.5.3b) einer periodischen Bewegung mit der Periodizität vier.
Systemparameter:
$m=0.2\text{ kg}, l=0.25\text{ m},$
$\omega_A=4.176\text{ /s}$
$b=0.04\text{ Nms}, A=0.543\text{ Nm}$.

![Figure 2.5.3b: Left: Highly overlapping multi-loop phase trajectory. Right: Stroboskopische Abbildung yielding exactly four distinct dots arranged vertically.]
Abb. 2.5.3b

---

## Page 12

![Figure 2.5.4a: Multi-plot of angle \phi, angular velocity \dot{\phi}, and driving phase vs. time showing completely irregular, non-repeating chaotic waveforms.]
Abb. 2.5.4a: Zeit-Funktionen (2.5.4a), Phasenbahn und stroboskopische Abbildung (2.5.4b) einer chaotischen Bewegung.
Systemparameter:
$m=0.2\text{ kg}, l=0.25\text{ m},$
$\omega_A=4.176\text{ /s}$
$b=0.04\text{ Nms}, A=0.55\text{ Nm}$.

![Figure 2.5.4b: Left: Densely packed, non-repeating chaotic phase trajectory. Right: Stroboskopische Abbildung showing a structured, fractal cloud of points (strange attractor).]
Abb. 2.5.4b

Der Attraktor einer chaotischen Bewegung (Abb. 2.5.4b, rechts) wird **seltsamer Attraktor** (strange attractor) genannt. Er besitzt eine fraktale (nichtganzzahlige) Dimension (s. Kap. III).

##### 2.6 Wege ins Chaos

Der Übergang von einer regulären (periodischen) Bewegung zu einer chaotischen Bewegung bei kontinuierlicher Änderung eines Systemparameters (Kontrollparameters, z.B. der Erregeramplitude $A$) wird "Weg ins Chaos" genannt. Es gibt verschiedene universelle Wege ins Chaos.

Ein sehr anschauliches Bild über das Systemverhalten in Abhängigkeit von einem Parameter liefert das **Bifurkationsdiagramm** (auch Feigenbaum-Diagramm genannt). Zur Konstruktion eines Bifurkationsdiagramms trägt man für jeden Parameterwert (z.B. der Anregungsamplitude $A$) die stroboskopisch gemessenen Werte einer Zustandsvariablen (z.B. der Winkelgeschwindigkeit $\Omega$) auf.

---

## Page 13

Für eine Bewegung mit der Periodizität eins erhält man für einen Parameterwert einen Punkt, für Periode zwei zwei Punkte usw. (vgl. 2.5).

![Figure 2.6.1: Feigenbaum bifurcation diagram showing the cascade of period-doublings from a single line into 2, 4, then chaotic dense regions interspersed with periodic windows.]
Abb. 2.6.1: Bifurkationsdiagramm für das getriebene Pendel bei Variation der Anregungsamplitude $A$ im Bereich $0.5 \dots 0.57\text{ Nm}$.
Systemparameter: $m=0.2\text{ kg}, l=0.25\text{ m}, \omega_A=4.176\text{ 1/s}, b=0.04\text{ Nms}$.

Abbildung 2.6.1 zeigt das Bifurkationsdiagramm für das getriebene Pendel bei Variation der Anregungsamplitude $A$. Man erkennt deutlich den Übergang zum Chaos über eine Kaskade von Periodenverdopplungen (**Feigenbaum-Szenario**, siehe auch [17-19]). Bei einem Parameterwert von ca. $0.545\text{ Nm}$ setzt das Chaos ein. Der chaotische Bereich (Bereich dichter Punkteverteilung) wird immer wieder von periodischen Fenstern (z.B. ein Periode-3-Fenster bei ca. $0.563\text{ Nm}$) unterbrochen, die bei weiterer Parametererhöhung ihrerseits wieder über Periodenverdopplung chaotisch werden.

Ein anderer universeller Weg ins Chaos ist die **Intermittenz** (Pomeau-Manneville-Szenario, siehe [20]). Hierbei wird eine periodische Bewegung in unregelmäßigen Zeitabständen durch chaotische "Bursts" unterbrochen. Mit der Änderung des Kontrollparameters werden die chaotischen Abschnitte immer länger, bis die Bewegung vollständig chaotisch ist.

Ein dritter Weg ist der Übergang über **Quasiperiodizität** (Ruelle-Takens-Newhouse-Szenario [21]). Eine quasiperiodische Bewegung ist eine Überlagerung von Schwingungen mit inkommensurablen Frequenzen (ihr Verhältnis ist eine irrationale Zahl). Die Phasenbahn schreibt sich auf einen Torus (Reifenoberfläche). Bei Parameteränderung verliert dieser Torus seine Stabilität und es entsteht ein seltsamer Attraktor.

---

## Page 14

##### 2.7 Empfindliche Abhängigkeit von den Anfangsbedingungen. Lyapunov-Exponent

Das wichtigste Charakteristikum einer chaotischen Bewegung ist ihre empfindliche Abhängigkeit von den Anfangsbedingungen (auch bekannt als "Schmetterlingseffekt"). Startet man zwei Trajektorien im Einzugsgebiet eines periodischen Attraktors sehr nahe beieinander, so nähern sie sich im Laufe der Zeit immer mehr an (Abb. 2.7.1a). Wenn der Attraktor jedoch chaotisch ist, so entfernen sich die beiden Trajektorien im Laufe der Zeit exponentiell voneinander (Abb. 2.7.1b), obwohl sie auf demselben Attraktor verbleiben!

![Figure 2.7.1a: Plot of \Delta\phi vs. time for a periodic attractor, showing the difference between two nearby trajectories decaying exponentially to zero.]
Abb. 2.7.1a: Zeitlicher Verlauf des Abstands $\Delta\phi$ zweier naher Trajektorien für einen periodischen Attraktor.

![Figure 2.7.1b: Plot of \Delta\phi vs. time for a chaotic attractor, showing the distance between two nearby trajectories growing exponentially on average until it saturates.]
Abb. 2.7.1b: Zeitlicher Verlauf des Abstands $\Delta\phi$ zweier naher Trajektorien für einen chaotischen Attraktor.

Ein quantitatives Maß für dieses Auseinanderlaufen ist der **Lyapunov-Exponent** $\lambda$ (siehe Kap. III). Für den Abstand $d(t)$ zweier benachbarter Trajektorien gilt im zeitlichen Mittel:

$$d(t) \sim d(0) \cdot e^{\lambda t}.$$

Ein positives $\lambda$ ($\lambda > 0$) ist das eindeutige Kriterium für das Vorliegen von deterministischem Chaos. Es bedeutet einen unumkehrbaren Verlust an Information über das System. Langzeitprognosen für das Systemverhalten sind unmöglich, da jede noch so kleine Ungenauigkeit in den Anfangsbedingungen (z.B. durch Messfehler) nach einer gewissen Zeit zu einer völlig anderen Bahn führt.

---

## Page 15

#### 3. Das parametrisch getriebene Pendel

Ein besonders reichhaltiges Verhalten zeigt das in Abschnitt 1.4 beschriebene parametrisch erregte Pendel. Die Bewegungsgleichung (1.4.3) unterscheidet sich vom direkt getriebenen Pendel dadurch, daß die Anregung als zeitabhängige Modulation des Koeffizienten des linearen Terms ($\sin\phi$) auftritt.

Für kleine Amplituden ($\sin\phi \approx \phi$) führt dies auf die Mathieusche Differentialgleichung:

$$\ddot{\phi} + 2\gamma\dot{\phi} + (\omega_0^2 + \frac{A\omega_A^2}{l} \cos\omega_A t)\phi = 0.$$

Ein bekanntes Phänomen dieses Systems ist die **parametrische Resonanz**. Sie tritt am stärksten auf, wenn die Erregerfrequenz ungefähr das Doppelte der Eigenfrequenz beträgt ($\omega_A \approx 2\omega_0$). In diesem Fall kann die Ruhelage $\phi=0$ instabil werden, und das Pendel beginnt aus kleinsten Störungen heraus aufzuschwingen (Kinder auf einer Schaukel nutzen diesen Effekt durch periodische Schwerpunktverlagerung).

Bei großen Amplituden zeigt das System neben harmonischen und subharmonischen Schwingungen auch Rotationen sowie den Übergang zu chaotischen Bewegungen. Eine Besonderheit des parametrischen Pendels ist die Möglichkeit der **Stabilisierung der instabilen oberen Ruhelage** ($\phi = \pi$). Bei hinreichend großer Erregerfrequenz und -amplitude kann das Pendel stabil senkrecht nach oben stehen und um diese Lage oszillieren (Kapistza-Pendel, siehe [22]).

---

## Page 16

### Kapitel II: Aufgaben und Experimente

Die folgenden Aufgaben sind so konzipiert, daß sie mit Hilfe des Simulationsteils ("Experiment") des Programms bearbeitet werden können. Sie dienen der Vertiefung des Stoffs aus Kapitel I.

#### Aufgabe 1: Das freie ungedämpfte Pendel (Amplitudenabhängigkeit der Periode)

Untersuchen Sie das freie ungedämpfte mathematische Pendel ($b=0, A=0$) gemäß Abschnitt 2.2.

1. Bestimmen Sie numerisch die Schwingungsdauer $T$ für verschiedene Anfangsauslenkungen $\phi_0$ im Bereich von $5^\circ$ bis $175^\circ$ (Wählen Sie jeweils $\dot{\phi}_0 = 0$).
2. Vergleichen Sie Ihre Meßergebnisse mit der harmonischen Näherung $T_0 = 2\pi\sqrt{l/g}$.
3. Plotten Sie die relative Periodendauer $T/T_0$ als Funktion der Amplitude $\phi_0$.

#### Aufgabe 2: Phasenportraits und Separatrix

Stellen Sie das Phasenportrait des freien ungedämpften Pendels dar.

1. Suchen Sie gezielt nach den Trajektorien, die den Übergang von der Schwingungs- zur Rotationsbewegung markieren (Separatrix).
2. Welche Anfangsgeschwindigkeit $\dot{\phi}_0$ ist bei einer Anfangsauslenkung von $\phi_0 = 0$ nötig, damit das Pendel exakt die obere Ruhelage ($\phi = 180^\circ$) erreicht? Nutzen Sie den Energiesatz zur theoretischen Berechnung und überprüfen Sie das Ergebnis im Experiment.

#### Aufgabe 3: Der Fixpunkt-Attraktor beim gedämpften Pendel

Untersuchen Sie das freie gedämpfte Pendel ($b > 0, A = 0$).

1. Wählen Sie eine feste Dämpfung $b=0.05\text{ Nms}$ und starten Sie das Pendel bei verschiedenen Anfangsbedingungen. Beobachten Sie das Schrumpfen des Phasenraumvolumens im Laufe der Zeit.
2. Unterscheiden Sie experimentell zwischen dem Schwingfall (Spirale im Phasenraum) und dem Kriechfall (direktes Einlaufen in den Fixpunkt) durch Erhöhung des Dämpfungskoeffizienten $b$.

---

## Page 17

#### Aufgabe 4: Resonanzkurve und Sprungphänomen beim Duffing-Oszillator

Untersuchen Sie den sinusförmig erregten nichtlinearen Federschwinger (Duffing-Oszillator) nach Gleichung (1.2.1) mit einer harten Feder ($c > 0, d > 0$).

1. Nehmen Sie die Resonanzkurve Amplitude als Funktion der Erregerfrequenz $\omega_A$ auf. Gehen Sie dabei schrittweise vor: Erhöhen Sie die Frequenz langsam in kleinen Schritten (Nutzen Sie die Option "Zweig ON", siehe IV.3.4.2) und notieren Sie die stationäre Schwingungsamplitude.
2. Wiederholen Sie das Experiment, indem Sie von einer hohen Frequenz ausgehend die Frequenz schrittweise verringern.
3. Zeichnen Sie beide Kurven in ein Diagramm. Identifizieren Sie den bistabilen Bereich und das Sprungphänomen.

#### Aufgabe 5: Die Feigenbaum-Kaskade (Periodenverdopplung)

Verfolgen Sie den Weg ins Chaos über Periodenverdopplung beim getriebenen Pendel bei Erhöhung der Anregungsamplitude $A$.

1. Stellen Sie die Parameter entsprechend Abb. 2.6.1 ein.
2. Suchen Sie die genauen Werte von $A$, bei denen der Übergang von Periode 1 zu Periode 2, und von Periode 2 zu Periode 4 stattfindet (Bifurkationspunkte).
3. Nutzen Sie die stroboskopische Abbildung, um die Anzahl der Punkte auf dem Attraktor eindeutig zu bestimmen.

#### Aufgabe 6: Bestimmung des Lyapunov-Exponenten

Weisen Sie die empfindliche Abhängigkeit von den Anfangsbedingungen im chaotischen Regime nach.

1. Wählen Sie Parameter, die zu einer chaotischen Bewegung führen (z.B. wie in Abb. 2.5.4).
2. Starten Sie eine Trajektorie bei $(\phi_0, \dot{\phi}_0)$. Starten Sie eine zweite Trajektorie mit einem winzigen Abstand dazu, z.B. $(\phi_0 + 0.001^\circ, \dot{\phi}_0)$.
3. Verfolgen Sie den zeitlichen Abstand $\Delta\phi(t)$ beider Bahnen. Schätzen Sie aus dem linearen Anstieg im halblogarithmischen Plot ($\ln|\Delta\phi|$ gegen $t$) den größten Lyapunov-Exponenten ab.

---

## Page 18

### Kapitel III: Theoretische Grundlagen und Mathematischer Anhang

#### i. Lineare vs. Nichtlineare Differentialgleichungen

Ein System von Differentialgleichungen heißt **linear**, wenn die gesuchten Funktionen und deren Ableitungen nur in der ersten Potenz und nicht in Form von Produkten miteinander verknüpft auftreten. Für lineare Systeme gilt das **Superpositionsprinzip**: Sind $y_1(t)$ und $y_2(t)$ Lösungen der homogenen linearen Gleichung, so ist auch jede Linearkombination

$$y(t) = c_1 y_1(t) + c_2 y_2(t)$$

eine Lösung. Bei nichtlinearen Systemen (wie z.B. durch das Auftreten von $\sin\phi$ in (1.1.2) oder $x^3$ in (1.2.1)) bricht dieses Prinzip völlig zusammen. Das Verhalten des Gesamtsystems ist nicht mehr die Summe seiner Teile.

#### ii. Autonomisierung nichtautonomer Systeme

Ein nichtautonomes System $n$-ter Ordnung der Form

$$\dot{\vec{x}} = \vec{F}(\vec{x}, t) \quad \text{mit } \vec{x} \in \mathbb{R}^n$$

läßt sich stets durch Einführen einer zusätzlichen Variablen $x_{n+1} = t$ in ein autonomes System $(n+1)$-ter Ordnung überführen:

$$\begin{aligned}
\dot{\vec{x}} &= \vec{F}(\vec{x}, x_{n+1}) \\
\dot{x}_{n+1} &= 1.
\end{aligned}$$

Handelt es sich um eine periodische Anregung mit der Frequenz $\omega_A$, so wählt man zweckmäßigerweise die Phasenvariable $\psi = \omega_A t \pmod{2\pi}$ als neue Koordinate. Der Phasenraum wird dadurch kompakt in dieser Dimension (Zylinder- oder Torusgeometrie).

---

## Page 19

#### iii. Kontraktion des Phasenraumvolumens (Dissipative Systeme)

Die zeitliche Änderung eines infinitesimalen Phasenraumvolumens $V(t)$ wird durch die Divergenz des Vektorfeldes der Bewegungsgleichungen bestimmt (Satz von Liouville):

$$\frac{1}{V} \frac{dV}{dt} = \text{div} \dot{\vec{x}} = \sum_{i=1}^n \frac{\partial F_i}{\partial x_i}.$$

Für das gedämpfte erzwungene Pendel (Gleichung 2.1.2) ergibt sich mit den Variablen $(\phi, \Omega)$:

$$\begin{aligned}
F_1(\phi, \Omega) &= \Omega \\
F_2(\phi, \Omega) &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi + \frac{A}{I}\cos(\omega_A t).
\end{aligned}$$

Die Divergenz lautet hierfür:

$$\text{div} \vec{F} = \frac{\partial F_1}{\partial \phi} + \frac{\partial F_2}{\partial \Omega} = 0 - \frac{b}{I} = -\frac{b}{I}.$$

Da $b > 0$ und $I > 0$ sind, ist die Divergenz konstant und negativ:

$$\frac{1}{V} \frac{dV}{dt} = -\frac{b}{I} \implies V(t) = V(0) \cdot e^{-\frac{b}{I} t}.$$

Das Phasenraumvolumen schrumpft also für $t \rightarrow \infty$ exponentiell gegen Null. Alle Trajektorien werden somit auf eine Teilmenge des Phasenraums gezwungen, die ein Volumen von Null besitzt (den Attraktor).

#### iv. Poincaré-Abbildung und stroboskopische Abbildung

Die Poincaré-Abbildung ist eine fundamentale Methode zur Reduktion der Dimensionalität eines kontinuierlichen dynamischen Systems. Statt der kontinuierlichen Trajektorie $\vec{x}(t)$ betrachtet man nur die Schnittpunkte dieser Trajektorie mit einer hyperdimensionalen Fläche $\Sigma$ (Poincaré-Schnittfläche) im Phasenraum.

---

## Page 20

Für periodisch getriebene Systeme wählt man als Schnittfläche am einfachsten feste Phasen der äußeren Anregung (stroboskopische Abbildung):

$$\Sigma = \{(\vec{x}, \psi) \mid \psi = \psi_0 \in [0, 2\pi)\}.$$

Die kontinuierliche Dynamik wird dadurch in eine diskrete Abbildung (Map) überführt:

$$\vec{x}_{k+1} = \vec{P}(\vec{x}_k),$$

wobei $\vec{x}_k = \vec{x}(t_k)$ mit $t_k = \frac{\psi_0}{\omega_A} + k \frac{2\pi}{\omega_A}$ ist.

| Bewegungstyp | Topologie im Phasenraum | Struktur in der Poincaré-Abbildung |
| --- | --- | --- |
| **Periodisch (Periode 1)** | Geschlossene Kurve (Grenzzyklus) | 1 isolierter Punkt |
| **Subharmonisch (Periode m)** | Verschlungener Grenzzyklus | $m$ isolierte Punkte |
| **Quasiperiodisch** | Torusoberfläche | Geschlossene Kurve (Invarianter Kreis) |
| **Chaotisch** | Seltsamer Attraktor | Fraktale Punktwolke |

#### v. Mathematische Modellierung der Gleitreibung ($r=0$)

Um numerische Instabilitäten an der Unstetigkeitsstelle der idealen Gleitreibung ($M_r = -b \cdot \text{sgn}(\dot{\phi})$ bei $\dot{\phi}=0$) zu vermeiden, nutzt man im Programm eine glatte Approximation mittels der Arkustangens-Funktion:

$$M_r(\dot{\phi}) = -b \cdot \frac{2}{\pi} \arctan\left(\frac{\dot{\phi}}{\delta}\right),$$

wobei $\delta \ll 1$ ein kleiner Regularisierungsparameter ist, der die Steilheit des Übergangs beim Nulldurchgang der Geschwindigkeit bestimmt. Im Limes $\delta \rightarrow 0$ nähert sich diese Funktion der exakten Coulombschen Gleitreibung an.
