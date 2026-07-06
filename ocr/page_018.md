## Page 49
Wir umgehen dieses Problem, indem wir die Funktion $y = \text{sgn}(\Omega)$ durch
$$
y = \frac{2}{\pi} \arctan(\Omega/\delta)
$$
(Abb. rechts), wobei der Parameter $\delta$ ein Maß für die Breite des Übergangsbereiches ( vom Wert $y=-1$ für $\Omega<0$ zum Wert $y=+1$ für $\Omega>0$) darstellt.

Diesen Parameter können Sie selbst einstellen (siehe Kapitel IV, Abschnitt 3.1.3).
---
zweitgrößten Streckung weisen und $\alpha_2$ wird gleich dem zweitgrößten lokalen Streckungsfaktor (für einen Zeitschritt $\Delta t$) definiert. So lassen sich also alle lokalen Streckungsfaktoren (für einen Zeitschritt $\Delta t$) als die Tendenz der $z_i^{(0)}$, sich in Richtung der größten Streckung zu orientieren, und der Eigenschaften der Reorthonormierung – die Numerierung der Start-Vektoren $z_i$ willkürlich gewählt werden kann.

Analog zu (2.9.2) ist $\alpha_i(\Delta t)$ der Streckungsfaktor über $m$ Zeitschritte $\Delta t$, den wir globalen Streckungsfaktor nennen. Er ist nichts anderes als das Produkt der in (V.3) angegebenen lokalen Streckungsfaktoren $\alpha_i^{(1)}$ aus allen $m$ Zeitschriften:
$$
\alpha_i(m) = \prod_{k=1}^{m} \alpha_i^{(1)}(k)
$$
wobei $\alpha_i^{(1)}(k)$ den $i$-ten Streckungsfaktor im Zeitschritt $(k-1)\Delta t \to k\Delta t$ bedeutet, der jeweils aus (V.3) bestimmt wird.

Der Ljapunov-Exponent $\lambda_i$ ermittelt sich also mit (2.9.5) zu
$$
\lambda_i = \lim_{m \to \infty} \lambda_i(m) = \lim_{m \to \infty} \frac{1}{m\Delta t} \sum_{k=1}^{m} \ln(\alpha_i^{(1)}(k)), \quad i=1,2,...,n
$$
(V.4)

Bei praktischen Rechnungen wird $m$ natürlich immer endlich sein, sollte aber sehr groß gewählt werden, um gute Konvergenz zu sichern (praktisch: mehrere hundert Anregungsperioden).

Bei der praktischen Berechnung der Ljapunov-Exponenten für unsere Systeme trifft man jedoch (außer im Fall linearer Reibung) auf einige weitere Probleme.

Wir betrachten zuerst den Fall, bei dem die Reibung eine Konstante ist. Die Bewegungsgleichungen lautet:
$$
\frac{d\phi}{dt} = \Omega
$$
$$
\frac{d\Omega}{dt} = -\frac{b}{I} \text{sgn}(\Omega) - \frac{mgL}{I} \sin\phi + \frac{A}{I} \cos(\omega_f t)
$$
(V.5)

Zur Berechnung der Ljapunov-Exponenten muß (V.5) simultan mit der Differentialgleichung der Störungen (V.1) gelöst werden. Die Ableitung des Terms $-b/I \cdot \text{sgn}(\Omega)$ ist bei $\Omega=0$ unstetig. Wir können also das System (V.1) nicht mit einer solchen Form der Reibung schreiben.