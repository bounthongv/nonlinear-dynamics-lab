# Ordnung und Chaos bei nichtlinearen Schwingungen
*Complete transcription from scanned book*

## Page 1

### Vorwort

Nichtlinearität ist fundamental für das gesamte Naturgeschehen. Schon einfache Oszillatoren müssen durch nichtlineare Differentialgleichungen beschrieben werden, wenn die Auslenkung aus der Ruhelage nicht mehr klein genug ist. Durch Nutzung von Computern sind in den letzten Jahren beträchtliche Fortschritte im Verständnis der Dynamik nichtlinearer Systeme gemacht worden. Das dynamische Verhalten reicht von periodischen Schwingungen bis zu chaotischen Bewegungen.

Dieses Selbststudienprogramm "Nichtlineare Schwingungen" ermöglicht einen Zugang zu diesem Gebiet. Das Programm besteht aus zwei wesentlichen Teilen: **Lernteil** und **Simulationsteil** (im Programm **Experiment** genannt).

Im **Lernteil** werden Sie durch beispielhafte Untersuchung des getriebenen Pendels grundlegende Unterschiede zwischen linearen und nichtlinearen Schwingungen, charakteristische Phänomene der nichtlinearen Schwingungen sowie für deren Beschreibung geeignete Begriffe, Untersuchungs- und Darstellungsmethoden zur Beurteilung des Systemverhaltens kennenlernen.

Eine Zusammenfassung des Lernteils finden Sie in Kapitel I. Dieses Kapitel ergänzt außerdem den Lernteil mit vertieften theoretisch-mathematischen Betrachtungen.

Nach der Arbeit mit dem Lernteil sollten Sie die notwendigen Kenntnisse zu einer selbständigen Arbeit mit dem Experimentierteil besitzen. Sie können vier Systeme - das **getriebene Pendel**, den **getriebenen nichtlinearen Federschwinger**, das **Pohlsche Rad** und das **parametrisch getriebene Pendel** (jeweils mit Dämpfung) - untersuchen. Die Aufgabensammlung in Kapitel II kann als Ausgangspunkt dafür dienen.

Eine zusammengefaßte Form der theoretischen Grundlagen können Sie im online-Lexikon (im Programm) oder in diesem Heft, Kapitel III, nachschlagen.

Eine Benutzerdokumentation mit Installations- und Gebrauchshinweisen finden Sie in Kapitel IV.

---

## Page 2

### Kapitel I: Zur Physik der nichtlinearen Schwingungen

#### 1. Behandelte nichtlineare Systeme

##### 1.1 Das getriebene mathematische Pendel

Die Lage des (ebenen) Pendels läßt sich eindeutig durch den Winkel $\phi$ beschreiben. Durch die Schwerkraft erfährt das Pendel ein Drehmoment $M_s$, das über eine Sinusfunktion mit dem Auslenkwinkel verknüpft ist. Dieses Drehmoment versucht, das Pendel in seine Ruhelage zurückzutreiben. Eine äußere Anregung, z.B. durch einen Elektromotor (zum Versuchsaufbau siehe [1-5]), prägt dem Pendel ein zusätzliches zeitabhängiges Drehmoment $M_a$ auf, für das wir harmonische Zeitabhängigkeit annehmen werden.

![Figure 1.1: Schematic diagram of a mathematical pendulum with length l and mass m at an angle \phi from the vertical, experiencing gravitational force mg.]
Abb. 1.1: Das ebene mathematische Pendel

Die dynamische Grundgleichung für die Drehung um eine feste Achse lautet:

$$I \frac{d^2\phi}{dt^2} = M,$$

wobei $I$ das Trägheitsmoment des Körpers um diese Achse und $M$ das Gesamtdrehmoment bezüglich dieser Achse sind. Für unser Pendel ergibt sich dann

$$I \frac{d^2\phi}{dt^2} = M_a + M_s + M_r$$

mit

* $I = ml^2$ - Trägheitsmoment des Pendels (masselose Stange der Länge $l$, Punktmasse $m$ am Ende);
* $M_a = A \cos(\omega_A t)$ - harmonisches Anregungsmoment mit Amplitude $A$ und Kreisfrequenz $\omega_A$;
* $M_s = -mgl \sin\phi$ - Drehmoment der Schwerkraft (das Minuszeichen drückt die rücktreibende Wirkung dieses Moments aus);
* $M_r = -b \left|\frac{d\phi}{dt}\right|^r \text{sgn}\left(\frac{d\phi}{dt}\right)$ - Moment der Reibungskraft $^2$);
* $b$ - Dämpfungskoeffizient,
* $r$ - Dämpfungsexponent ($r=0$ oder $r \ge 1$)$^3$).

---

$^1$) Das Drehmoment ist ein Vektor. Im vorliegenden Fall der Rotation um eine feste Achse liegt dieser Vektor stets parallel zur Drehachse; es genügt daher, nur die Komponente in Achsenrichtung zu betrachten.
$^2$) Die sgn-Funktion ist folgendermaßen definiert: $\text{sgn}(x) = \begin{cases} +1 & \text{falls } x > 0 \\ -1 & \text{falls } x < 0 \end{cases}$
$^3$) Bei $0 \le r < 1$ wird nach Cauchy-Lipschitz-Theoren (Existenz- und Eindeutigkeitssatz) die Eindeutigkeit der Lösung der Differentialgleichung (1.1.1) verletzt. Ein Ausweg für den Fall $r=0$ wird weiter unten beschrieben.

---

## Page 3

Der Ansatz für das Reibungsmoment garantiert, dass dieses stets der Bewegung entgegengerichtet ist. $r=1$ liefert eine lineare Reibung, wie sie z.B. beim Luftwiderstand für kleine Geschwindigkeiten oder bei der Wirbelstrombremse auftritt. Mit diesem Wert rechnen wir im Lernteil ausschließlich. Für den Experimentierteil kann auch $r > 1$ gewählt werden. $r=0$ bedeutet eine Gleitreibung; um aber nicht mit einer unstetigen Funktion rechnen zu müssen, modellieren wir die Gleitreibung durch $M_r = -b (2/\pi) \arctan(\dot{\phi}/\delta)$, wobei der Parameter $\delta$ ein Maß für die Breite des Übergangsbereiches (vom Wert $M_r = +b$ für $\dot{\phi} < 0$ zum Wert $M_r = -b$ für $\dot{\phi} > 0$) darstellt (siehe auch Anhang v).

Man erhält dann als Bewegungsgleichung eine nichtlineare Differentialgleichung zweiter Ordnung im Auslenkwinkel $\phi$ (im Folgenden ist in $M_r$ stets $r=1$ gesetzt):

$$I \frac{d^2\phi}{dt^2} + b \frac{d\phi}{dt} + mgl \sin\phi = A \cos(\omega_A t)$$

Die Lösungen dieser Differentialgleichung zweiter Ordnung sind bei Kenntnis zweier Anfangsbedingungen - z.B. für Winkel und Winkelgeschwindigkeit zum Zeitpunkt $t=0$ - eindeutig bestimmt. Der Zustand des Pendels zu einer bestimmten Zeit wird durch die Kenntnis von $\phi$ und $\dot{\phi}$ zu dieser Zeit beschrieben. Kennt man den Zustand zu einem Zeitpunkt (z.B. $t=0$), so ist er für alle anderen Zeitpunkte durch die Bewegungsgleichung (1.1.2) festgelegt. Die Variablen $\phi$ und $\dot{\phi}$ nennt man Zustandsvariable. Sie spannen den sog. Zustands- oder Phasenraum (2.1) auf.

##### 1.2 Sinusoidal erregter gedämpfter Federschwinger

Ein weiteres System, das Sie im Experimentierteil des Programms untersuchen können, ist der Federschwinger mit nichtlinearer Rückstellkraft und periodischer Anregung. Für die Rückstellkraft nehmen wir an: $F(x) = -cx - dx^3$. Die Konstanten $c, d$ hängen von Material und Form der Feder ab. (Für eine realistische Feder ist $c > 0$ und $d$ beliebig, allerdings sollte die Kraft für alle zugelassenen Auslenkungen rücktreibend sein). Für die Reibungskraft $F_r$ machen wir einen analogen Ansatz wie in 1.1, wobei lediglich $M_r \rightarrow F_r, \phi \rightarrow x, \dot{\phi} \rightarrow \dot{x}$ zu ersetzen ist. Die äußere anregende zeitabhängige Kraft sei $A \cos(\omega_A t)$. Aus dem zweiten Newtonschen Gesetz erhält man die Bewegungsgleichung, die im Falle linearer Reibung ($r=1$) Duffing-Differentialgleichung genannt wird,

$$m \frac{d^2x}{dt^2} + b \left|\frac{dx}{dt}\right|^r \text{sgn}\left(\frac{dx}{dt}\right) + cx + dx^3 = A \cos(\omega_A t),$$

---

## Page 4

wobei

* $m$ - Masse des Schwingers
* $b$ - Reibungskoeffizient $^1$)
* $r$ - Reibungsexponent ($r=0$ oder $r \ge 1$)
* $c, d$ - Konstanten der kubischen Rückstellkraft
* $A$ - Amplitude der anregenden Kraft $^1$)
* $\omega_A$ - Frequenz der Anregung

![Figure 1.2: Schematic of a mass m on a horizontal surface connected to a spring and driven by a motor, showing displacement x.]
Abb. 1.2: Federschwinger

Die Duffing-Differentialgleichung ($r=1$) beschreibt viele reale physikalische Systeme (siehe [6-8]).

##### 1.3 Pohlsches Rad

Ein System, das man auch für Realexperimente schnell aufbauen kann, ist das Pohlsche Rad, ein Drehpendel. Durch Anbringen einer Unwucht läßt es sich leicht so verändern, daß Eigenschaften nichtlinearer Schwingungen demonstriert werden können.

Die Bewegungsgleichung des Pohlschen Rades mit Unwucht ergibt sich aus den Drehmomenten, die von der Zusatzmasse und der Feder auf das Rad ausgeübt werden, wobei letzteres noch durch die Anregung $A \cos(\omega_A t)$ harmonisch moduliert wird, das Reibungsmoment hänge wie in 1.1 von der Winkelgeschwindigkeit ab:

![Figure 1.3: Diagram of a Pohl's wheel showing a circular disk with an eccentric mass m, connected to a motor via a spring.]
Abb. 1.3: Pohlsches Rad

$$I \frac{d^2\phi}{dt^2} + b \left|\frac{d\phi}{dt}\right|^r \text{sgn}\left(\frac{d\phi}{dt}\right) + [d + \Phi - (A + A \cos(\omega_A t))] - mgl \sin\phi = 0,$$

wobei

* $I$ - Trägheitsmoment des Rades mit Unwucht der Masse $m$ ($I = I_0 + ml^2$; $I_0$ - Trägheitsmoment des Rades, $l$ - Distanz der Unwucht zum Zentrum des Rades)
* $b$ - Dämpfungskoeffizient, $r$ - Dämpfungsexponent ($r=0$ oder $r \ge 1$)
* $d$ - Rückstellkoeffizient der Spiralfeder
* $\alpha$ - Mittellage der Anregung, bzw. Ruhelage von $m$ bei $A=0, g=0$.

---

$^1$) Man beachte, daß $A$ und $b$ hier natürlich eine andere physikalische Dimension als für die übrigen Systeme haben.

---

## Page 5

##### 1.4 Parametrisch getriebenes Pendel

Ein parametrisch getriebenes Pendel ist, zum Beispiel, ein ebenes mathematisches Pendel wie in 1.1, dessen Aufhängungspunkt jedoch einer vertikalen periodischen Bewegung $s(t) = A \cos\omega_A t$ unterworfen wird (Abb. 1.4). Bei der Herleitung der Bewegungsgleichung beachten wir, daß der Winkel $\phi$ nun in einem mit dem Aufhängungspunkt mitbewegten Bezugssystem gemessen wird und wir demzufolge die Trägheitskraft $\vec{F}_T = -m\ddot{s}(t)\vec{e}_z$ zu berücksichtigen haben; diese übt das Drehmoment $M_T = m\ddot{s}(t)l \sin\phi$ auf das Pendel aus, was in (1.1.1) anstelle von $M_a$ zu berücksichtigen ist:

$$I\ddot{\phi} = M_T + M_s + M_r.$$

![Figure 1.4: Diagram of a parametrically driven pendulum with a vertically oscillating support point s(t).]
Abb. 1.4: Parametrisch erregtes Pendel

Bei diesem System wollen wir uns nun auf eine lineare Reibung ($r=1$ in 1.1) beschränken, die z.B. durch eine Wirbelstrombremse hervorgerufen wird (Lager- und insbesondere Luftreibung seien demgegenüber vernachlässigbar; zum Versuchsaufbau siehe [9,10]). Damit erhalten wir also für die Bewegungsgleichung des parametrisch erregten Pendels:

$$I\ddot{\phi} = -m l (g - \ddot{s}) \sin\phi - b\dot{\phi}.$$

Erfolgt die Anregung wieder harmonisch mit $s(t) = A \cos\omega_A t$, so gilt:

$$I\ddot{\phi} + b\dot{\phi} + ml(g + A\omega_A^2 \cos\omega_A t) \sin\phi = 0.$$

(alle Parameter sind analog zum System in 1.1)

#### 2. Nichtlineare Phänomene (am Beispiel des mathematischen Pendels)

##### 2.1 Bewegungsgleichung, Phasenraum

In der Theorie dynamischer Systeme schreibt man die Bewegungsgleichungen in Form eines Systems von $n$ Differentialgleichungen erster Ordnung für die $n$ Zustandsvariablen $q_i$:

$$\frac{dq_i}{dt} = \dot{q}_i = F_i(q_1, q_2, \dots, q_n, t), \quad i=1,2,\dots,n.$$

Je nachdem, ob die Funktionen $F_i$ explizit von der Zeit abhängen oder nicht, unterscheidet man zwischen nichtautonomen und autonomen Systemen.

In unserem Fall des mathematischen Pendels ist $n$ zunächst gleich zwei. Durch Einführen von $\Omega = \dot{\phi}$ als neue dynamische Variable kann die Differentialgleichung (1.1.2) in Form (2.1.1) umgeschrieben werden ($q_1 = \phi, q_2 = \Omega = \dot{\phi}$):

---

## Page 6

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi + \frac{A}{I}\cos(\omega_A t).
\end{aligned}$$

Das System ist also nichtautonom ($F_2$ enthält in $\cos\omega_A t$ die Zeit explizit!). Durch Einführen der neuen dynamischen Variablen $\psi = \omega_A t$ (die auf den Bereich $0..2\pi$ oder $-\pi..+\pi$ beschränkt werden kann) wird das System formal autonom gemacht:

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi + \frac{A}{I}\cos(\psi) \\
\frac{d\psi}{dt} &= \omega_A.
\end{aligned}$$

Die Anzahl der dynamischen (oder Zustands-) Variablen ist nun $n=3$ ($\phi, \Omega, \psi$).

###### Phasenraum

Üblicherweise wird die Entwicklung eines dynamischen Systems im Zustands- oder Phasenraum dargestellt, dessen Koordinatenrichtungen durch die Zustandsvariablen gebildet werden. Ein Punkt im Phasenraum repräsentiert also einen momentanen Systemzustand. Die im Zeitablauf (gemäß den Bewegungsgleichungen) durchlaufenen Punkte bilden die Phasenbahn oder Phasentrajektorie.

![Figure 2.1: 3D plot of a phase trajectory (black) of a periodic motion in a three-dimensional phase space, along with its 2D projection (gray) onto the (\phi, \Omega) plane.]
Abb. 2.1: Phasentrajektorie (schwarz) einer periodischen Bewegung im dreidimensionalen Phasenraum. Sie ist spiralförmig und kann sich nicht schneiden. Ihre Projektion (grau) auf die $\phi$-$\Omega$-Ebene kann Schnittpunkte enthalten.

Die Dimension des Phasenraums des getriebenen Pendels ist drei. Für eine anschaulichere 2-dimensionale Darstellung projiziert man die Zeitdimension heraus, indem man die Phasentrajektorien auf die $(\phi, \Omega)$ Ebene projiziert. Den zweidimensionalen Unterraum $(\phi, \Omega)$ bzw. $(\phi, \dot{\phi})$ nennt man Phasenebene oder auch Phasenraum. Da die Lösung des autonomen Systems (2.1.3) bei Vorgabe von Anfangswerten $q_i(t=0)$ eindeutig bestimmt ist, kann durch jeden Punkt des $n$-dimensionalen Phasenraumes nur eine Trajektorie gehen, d.h., die Trajektorien dürfen sich nicht schneiden - weder untereinander, noch sich selbst. Die in einen Unterraum projizierten Trajektorien können sich aber schneiden.

---

## Page 7

##### 2.2 Abhängigkeit der Schwingungsdauer des freien ungedämpften Pendels von der Schwingungsamplitude

Wir betrachten zuerst den einfachsten Fall, daß Reibung und äußere Anregung verschwinden ($b=0, A=0$):

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\frac{mgl}{I}\sin\phi.
\end{aligned}$$

Es handelt sich also um ein autonomes System mit den beiden Zustandsvariablen $(\phi, \Omega)$; der Phasenraum ist zweidimensional.

Wenn der Ausschlagwinkel $\phi$ klein ist, gilt $\sin\phi \approx \phi$, und wir erhalten ein System von linearen Differentialgleichungen

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\omega_0^2\phi
\end{aligned}$$

mit $\omega_0^2 = mgl/I$.

Diese linearen Gleichungen haben die periodische Lösung:

$$\phi = \phi_m \cos(\omega_0 t + \alpha),$$

wovon man sich einfach durch Einsetzen in die Gleichungen (2.2.2) überzeugen kann.

Die Schwingungsdauer $T$ ist nur durch den Systemparameter $\omega_0$ gegeben: $T = 2\pi/\omega_0$. Die in der Lösung (2.2.3) enthaltenen zwei Konstanten, Amplitude $\phi_m$ und Nullphasenwinkel $\alpha$, sind durch die Anfangswerte $\phi(t=0) = \phi_0$ und $\dot{\phi}(t=0) = \dot{\phi}_0$ bestimmt.

Wenn man die nichtlinearen Differentialgleichungen (2.2.1) numerisch löst, sieht man, daß die Periodendauer $T$ der Funktion $\phi(t)$ bei kleinen Ausschlägen tatsächlich wie bei der Lösung (2.2.3) der Gleichungen (2.2.2) nicht von der Amplitude der Schwingung abhängt (Abb. 2.2.1a). Bei Anfangsbedingungen, die zu großen Schwingungsamplituden führen, hängen sowohl Lösungsform als auch Periodendauer von der Schwingungsweite und damit von den Anfangsbedingungen ab (Abb. 2.2.1b).

---

## Page 8

![Figure 2.2.1a: Plot of angle \phi (in degrees) vs. time t for small amplitudes, showing standard sinusoidal behavior.]
Abb. 2.2.1a: Winkel-Zeit-Funktion des freien ungedämpften Pendels bei kleinen Ausschlagwinkeln.

![Figure 2.2.1b: Plot of angle \phi (in degrees) vs. time t for larger amplitudes, where the period increases as the maximum angle increases.]
Abb. 2.2.1b: Winkel-Zeit-Funktion des freien ungedämpften Pendels bei großen Ausschlagwinkeln.

**Die Periodenlänge vergrößert sich mit Vergrößerung der Auslenkung.** Für die nichtlineare Schwingung hat der Begriff "Eigenfrequenz", im Sinn eines konstanten Werts, der nur von Systemparametern abhängt, seine physikalische Bedeutung verloren, die Schwingung ist nicht mehr harmonisch.

Nähert sich die Schwingungsamplitude dem Wert $\pi$, so hält sich das Pendel für immer längere Zeit in der Umgebung von $\phi = \pm\pi$ $^1$) auf. Der Punkt $\phi = \pi$ ist ein instabiler Gleichgewichtspunkt (instabiler Fixpunkt).

![Figure 2.2.2: Plots of angle \phi vs. time and angular velocity \dot{\phi} vs. time for an amplitude near 179.9 degrees, showing long plateaus near the peak.]
Abb. 2.2.2: Winkel-Zeit-Funktion des freien ungedämpften Pendels für eine Amplitude von $179.9^\circ$

---

$^1$) Die Punkte $\phi = +\pi$ und $\phi = -\pi$ sind miteinander zu identifizieren. Sie entsprechen derselben Lage des Pendels.

---

## Page 9

Bei weiterer Vergrößerung der Anfangsenergie durch Vergrößerung der Anfangsgeschwindigkeit wird das Pendel Rotationen ausführen. Der Mittelwert der Winkelgeschwindigkeit ist dann ungleich Null.

Für Schwingungen ohne Überschläge sind die Phasentrajektorien geschlossene Kurven (das System kommt immer wieder zu seinem Anfangszustand zurück). Für Rotationen liegen die Phasenraumtrajektorien in der oberen Halbebene (positive Geschwindigkeit) oder in der unteren Halbebene (negative Geschwindigkeit) der Phasenebene $^1$). Die Grenze zwischen den Bereichen der Phasenebene, in denen Rotationen und Schwingungen auftreten, wird Separatrix (Trennlinie) genannt (Kurve von $-\pi$ zu $+\pi$ und umgekehrt). (Zu diesem Begriff kommen wir nochmal in 2.4 zurück. In Kapitel II, Aufgabe 4, werden Sie diese Kurve berechnen).

Startet man die Bewegung von verschiedenen Gebieten der Phasenebene, die durch die Separatrix getrennt sind, so werden verschiedene Bewegungsformen - Schwingung oder Rotation - ausgeführt.

![Figure 2.2.3: Phase portrait (angular velocity \dot{\phi} vs. angle \phi) of the free undamped pendulum, showing closed loops for oscillations, open curves for rotations, and the separating separatrix lines.]
Abb. 2.2.3: Phasentrajektorien des freien ungedämpften Pendels für verschiedene Anfangsbedingungen.

---

$^1$) Sie sind geschlossen über die miteinander zu identifizierenden Punkte am rechten ($\phi = +\pi$) und linken ($\phi = -\pi$) Rand der Phasenebene.

---

## Page 10

##### 2.3 Dissipatives System. Attraktor

Nun wollen wir als nächstes eine (lineare) Reibung zulassen. Durch die Reibung wird dem System mechanische Energie entzogen. Ein solches System nennt man ein dissipatives System. Die Bewegungsgleichungen lauten nun:

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi.
\end{aligned}$$

Beschränkt man zunächst sich wieder auf kleine Ausschläge ($\sin\phi \approx \phi$), so lautet die Lösung der dann aus (2.3.1) hervorgehenden linearen Gleichungen:

$$\phi = a e^{-\gamma t} \cos(\omega_d t + \alpha),$$

mit $\gamma = b/2I$ und $\omega_d^2 = \omega_0^2 - \gamma^2 > 0$ (wir wollen hier nur den Schwingfall betrachten). Die Integrationskonstanten $a$ und $\alpha$ sind wieder durch die Anfangswerte $\phi_0$ und $\dot{\phi}_0$ bestimmt. Von der Richtigkeit der Lösung (2.3.2) überzeugt man sich wieder durch Einsetzen in (2.3.1) bei $\sin\phi \approx \phi$.

Die Lösung (2.3.2) kann man als periodische Lösung mit der zeitabhängigen Amplitude

$$\phi = a e^{-\gamma t}$$

auffassen. Die Amplitude der Schwingung nimmt also mit der Zeit exponentiell ab. Sie nähert sich asymptotisch der Ruhelage.

Die numerische Lösung der nichtlinearen Gleichungen (2.3.1) bestätigt dieses Verhalten. Die Phasentrajektorien $\phi = \phi(\dot{\phi})$ schrumpfen auf den sog. **Fixpunkt - Attraktor** ($\phi_0 = 0, \dot{\phi}_0 = 0$) zusammen (Abb.2.3.1).

![Figure 2.3.1a: Damped oscillation curve showing the angle decaying over time toward zero.]
Abb. 2.3.1a: Winkel-Zeit-Funktion des freien gedämpften Pendels.

---

## Page 11

![Figure 2.3.1b: Phase space plot showing a trajectory spiraling inward toward the origin (0,0) due to damping.]
Abb. 2.3.1b: Phasentrajektorien des freien gedämpften Pendels.

Wenn man das dissipative System mit Anfangsbedingungen (Punkten) aus einem vorgegebenen Gebiet des Phasenraums startet, gelangen alle diese Trajektorien schließlich auf den Attraktor (hier Fixpunkt), d.h., alle Punkte bewegen sich (gemäß den Bewegungsgleichungen) so, daß das von ihnen eingenommene Gebiet ("Volumen") im Phasenraum "schrumpft" (hier bis auf einen Punkt; aus einer Fläche - Dimension 2 - wurde also ein Punkt - Dimension 0).

Dieses "Schrumpfen des Phasenraumvolumens" ist ein generelles Charakteristikum dissipativer Systeme. Die mathematische Formulierung dieser Eigenschaft finden Sie in Anhang iii.

##### 2.4 Grenzzyklus. Sprungphänomen. Bistabilität

Wir betrachten jetzt das getriebene Pendel (2.1.2) oder (2.1.3). Die Lösung der linearen Schwingungstheorie (für kleine Ausschlagwinkel, wo $\sin\phi \approx \phi$) lautet:

$$\phi = a e^{-\gamma t} \cos(\omega_d t + \alpha) + C \cos(\omega_A t + \psi)$$

wobei $\gamma, \omega_d$ die gleiche Bedeutung wie in (2.3.2) haben und $a$ und $\alpha$ durch die Anfangsbedingungen bestimmte Integrationskonstanten sind; die Amplitude $C$ und die Phasenverschiebung $\psi$ im zweiten Term ergeben sich nach Einsetzen in die Differentialgleichungen und Koeffizientenvergleich zu:

$$\begin{aligned}
C &= \frac{A}{I \sqrt{(\omega_0^2 - \omega_A^2)^2 + 4\gamma^2\omega_A^2}} \\
\tan\psi &= -\frac{2\gamma\omega_A}{\omega_0^2 - \omega_A^2}
\end{aligned}$$

---

## Page 12

Der erste Term in (2.4.1), die gedämpfte Eigenschwingung, klingt mit der Zeit ab (Einschwingvorgang). Nach dem Einschwingvorgang (transiente Bewegung) führt das Pendel eine periodische Bewegung mit der Frequenz $\omega_A$ der Erregerfunktion aus und zwar unabhängig von den Anfangsbedingungen. Die Amplitude $C$ ist nach (2.4.2) eine Funktion der Erregerfrequenz; sie ist unabhängig von den Anfangsbedingungen. $C(\omega_A)$ hat ein Maximum bei der Resonanzfrequenz $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$, die von der Anregungsamplitude $A$ unabhängig ist. Die Phasentrajektorie bildet dann (für große Zeiten) eine geschlossene Kurve. Diese Art eines Attraktors nennt man einen **Grenzzyklus**. Die numerische Lösung der nichtlinearen Gleichungen (2.1.2) bestätigt dieses Verhalten auch bei größeren Ausschlägen; nach einer Einschwingzeit (z.B. ca. 10 s in Abb.2.4.1) schwingt das System periodisch.

![Figure 2.4.1a: Waveform plot showing the transient behavior settling into a steady state oscillation.]
Abb. 2.4.1a: Winkel-Zeit-Funktion des erzwungenen gedämpften Pendels.
$m = 0.2\text{ kg}, l = 0.25\text{ m}, \omega_A = 4.176\text{ /s}$
$b = 0.02\text{ Nms}, A = 0.29\text{ Nm}$
Anfangsbedingungen: $\phi_0 = 0, \dot{\phi}_0 = 0$

![Figure 2.4.1b: Phase space plot showing a trajectory winding around and eventually settling onto a closed loop.]
Abb. 2.4.1b: Phasentrajektorie des erzwungenen gedämpften Pendels mit Einschwingvorgang und Grenzzyklus.

![Figure 2.4.1c: Clean closed-loop phase portrait representing the stable attractor (limit cycle).]
Abb. 2.4.1c: Grenzzyklus der Phasentrajektorie des erzwungenen gedämpften Pendels.

Trägt man man für das nichtlineare getriebene Pendel die Schwingungsamplitude (bei unveränderter Dämpfung) verschiebt sich das Maximum der Schwingungsamplitude zu kleineren Frequenzen (erinnern Sie sich daran, daß sich die Schwingungsdauer des freien Pendels mit Vergrößerung der Schwingungsamplitude vergrößert).

---

## Page 13

![Figure 2.4.2: Resonance curves for different excitation amplitudes, demonstrating the characteristic bending of the resonance peak to the left (softening spring behavior).]
Abb. 2.4.2: Resonanzkurven für verschiedene Anregungsamplituden.
Systemparameter:
$m = 0.2\text{ kg}, l = 0.25\text{ m},$
$b = 0.02\text{ Nms},$
$A \text{ [Nm]} = 0.05; 0.1; 0.14; 0.18; 0.2; 0.225$
Anfangsbedingungen: $(\phi_0 \text{ [grad]}, \dot{\phi}_0 \text{ [grad/s]}): (0,0), (150,0)$.

2. Bei relativ großer Anregungsamplitude (aber noch nicht so groß, daß Überschläge stattfinden) verändert sich bei einer bestimmten Erregerfrequenz die Pendelamplitude sprunghaft (**Sprungphänomen**, siehe auch [11,12]). Wenn man diese Resonanzkurve für verschiedene Anfangsbedingungen $^1$) berechnet, sieht man einen Frequenzbereich (überlappende Linien in Abb. 2.4.2), wo das System zwei stabile Schwingungen mit unterschiedlichen Amplituden ausführen kann (**Bistabilität**). Welche Schwingung realisiert wird, hängt von der Anfangsbedingung ab (Abb. 2.4.3). Bei nichtlinearen Systemen können also **mehrere Attraktoren koexistieren**. (Siehe auch [3-5,13-16]).

![Figure 2.4.3a: Closed loop phase portrait for one stable oscillation state under coexisting conditions.]
Abb. 2.4.3a

![Figure 2.4.3b: Another closed loop phase portrait showing a distinctly different shape/amplitude under identical system parameters but different initial conditions.]
Abb. 2.4.3b

Abb. 2.4.3: Bistabilität: Koexistenz zweier verschiedener Schwingungen bei denselben Systemparametern. Die Anfangsbedingungen entscheiden, welche Schwingung realisiert wird.
Abb.2.4.3a: Phasentrajektorien mit Einschwingvorgängen und Grenzzyklen.
Abb. 2.4.3b: Grenzzyklen.
Systemparameter: $m=0.2\text{ kg}, l=0.25\text{ m}, \omega_A=4.176\text{ 1/s}, b=0.02\text{ Nms}, A=0.225\text{ Nm}$.
Anfangsbedingungen: $(\phi_0\text{ [grad]}, \dot{\phi}_0\text{ [grad/s]}):$ kleiner Grenzzyklus - (0,0) und großer Grenzzyklus - (150,0).

---

$^1$) Im Experimentierteil haben Sie die Möglichkeit, den letzten Trajektorienpunkt des vorherigen Schrittes als Anfangsbedingung für die Rechnung mit dem nächsten Wert der Erregerfrequenz zu wählen (Option Zweig ON). Dabei entsteht nur ein Zweig der Resonanzkurve; beide Zweige erhält man, wenn man sowohl für zunehmende als auch für abnehmende Frequenz rechnet (s.a. IV.3.4.2).

---

## Page 14

Das Gebiet oder die Menge der Anfangsbedingungen, deren zugehörige Trajektorien in einen bestimmten Attraktor hineinlaufen, nennt man Einzugsgebiet dieses Attraktors. Die Grenze zwischen den Einzugsgebieten verschiedener Attraktoren wird Separatrix genannt. Wenn das System in der Nähe der Separatrix gestartet wird, kann eine kleine Abweichung in den Anfangsbedingungen zu sehr unterschiedlichen Bewegungen führen. So ergeben die "nahe" beieinander liegenden Anfangsbedingungen in Abb 2.4.4 Bewegungen auf den unterschiedlichen Attraktoren.

![Figure 2.4.4: Phase portrait illustrating two phase trajectories starting very close to each other but separating and converging to different coexisting attractors.]
Abb. 2.4.4: Zwei verschiedene Schwingungen, die von zwei nahe beieinander liegenden Anfangsbedingungen gestarteten werden.
Systemparameter: $m=0.2\text{ kg}, l=0.25\text{ m}, \omega_A=4.176\text{ 1/s},$
$b=0.02\text{ Nms}, A=0.225\text{ Nm}$.
Anfangsbedingungen: $(\phi_0\text{ [grad]}, \dot{\phi}_0\text{ [grad/s]}):$ kleiner Grenzzyklus - (163,0) und großer Grenzzyklus - (162,0).

##### 2.5 Stroboskopische Abbildung. Seltsamer Attraktor

Mit der Erhöhung der Anregungsamplitude werden wir immer komplexere Bewegungen beobachten. So kann das Pendel Überschläge ausführen. Die Bewegung wird im allgemeinen eine Kombination von Rotation und Schwingung sein. Die Resonanzkurve ist unbrauchbar für die Untersuchung solcher Bewegungen, da bei Überschlägen die Amplitude der Schwingung immer $180^\circ$ beträgt. Wenn sich (wie beobachtet) die Periode der Schwingungen vergrößert, wird die Phasenbahn unübersichtlich; sie erscheint für die Untersuchung des Bewegungsverhaltens als wenig geeignet.

In der stroboskopischen Abbildung reduziert man die Information in der Phasenseite, ohne Wesentliches zu verlieren, indem man die Phasenbahn periodisch nach einer Periode der Erregung "beleuchtet". Eine Bewegung, die die gleiche Periode wie die Anregungsfunktion hat, produziert dann einen Punkt, eine Bewegung, deren Schwingungsdauer gleich der doppelten Schwingungsdauer des Erregers ist, produziert zwei Punkte in der Phasenebene usw..

Bei periodischen Bewegungen hat man in der stroboskopischen Abbildung also eine endliche Anzahl von Punkten (, falls die Frequenz der Bewegung gleich einem rationalen Vielfachen der Erregerfrequenz ist). Bei quasiperiodischen und chaotischen Bewegungen, wo das System niemals zu demselben Zustand zurückläuft, werden in der stroboskopischen Abbildung stets neue Punkte auf dem Attraktor produziert. Die Abbildungen 2.5.1-4 stellen die Winkel-

---

## Page 15

geschwindigkeit-Zeit-Funktion, Phasenbahn und stroboskopische Abbildung periodischer Bewegungen verschiedener Periodizität und chaotischer Bewegung dar.

![Figure 2.5.1a: Waveform plot of angle \phi and angular velocity \dot{\phi} vs. time showing period-1 oscillation.]
Abb. 2.5.1a: Zeit-Funktionen (2.5.1a), Phasenbahn und stroboskopische Abbildung (2.5.1b) einer periodischen Bewegung mit der Periodizität eins.
Systemparameter:
$m=0.2\text{ kg}, l=0.25\text{ m},$
$\omega_A=4.176\text{ /s}$
$b=0.04\text{ Nms}, A=0.51\text{ Nm}$.

![Figure 2.5.1b: Left: Single closed loop phase portrait. Right: Stroboskopische Abbildung yielding a single isolated dot.]
Abb. 2.5.1b

![Figure 2.5.2a: Waveform plot of angle \phi and angular velocity \dot{\phi} vs. time showing period-2 oscillation (alternating peak heights).]
Abb. 2.5.2a: Zeit-Funktionen (2.5.2a), Phasenbahn und stroboskopische Abbildung (2.5.2b) einer periodischen Bewegung mit der Periodizität zwei.
Systemparameter:
$m=0.2\text{ kg}, l=0.25\text{ m},$
$\omega_A=4.176\text{ /s}$
$b=0.04\text{ Nms}, A=0.535\text{ Nm}$.



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
