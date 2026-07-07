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
