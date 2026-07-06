## Page 32

Es ergibt sich also ein Schema folgenden Typs für den Informationsübertrag (Abb. 2.8.2)

```
       q₀  q₁  q₂  q₃  q₄  ... q_m
10⁰    |   |   |   |   |
       v   v   v   v   v
10¹    I₀  I₁  I₂  I₃  I₄  ... I_m
       |   |   |   |   |
       v   v   v   v   v
10²                                 q_int
       |   |   |   |   |
       v   v   v   v   v
10³                                 q_lok
       |   |   |   |   |
       v   v   v   v   v
10⁴                                 q_vor-k
```

Abb. 2.8.2 Informationsübertrag aus der Anfangsbedingung in den momentanen Systemzustand irregulären Regime.

Für beliebig große Zeiten geht der Informationszuwachs in der Symbolfolge gegen Null und die Vorhersagezeit dementsprechend gegen Unendlich. Für solche reguläre Bewegungen kann man also durch präzisere Kenntnis des Systemzustands eine bessere Vorhersagbarkeit ermöglichen.

Sei $\delta_{max}$ eine Abweichung in den Anfangsbedingungen und $\epsilon_{max}$ ein maximaler Fehler, der bei der Vorraussage nicht überschritten werden soll, so ist die Vorhersagezeit
$t_{vor} \sim \delta_{max} / \epsilon_{max}$.
Will man bei gleichem maximalen Fehler die Vorhersagezeit verlängern, so muß die Anfangstoleranz $\epsilon_{max}$ entsprechend linear verkleinert werden. Der Aufwand zur Erhöhung der Vorhersagezeit wächst linear.

Eine chaotische Bewegung kann also definiert werden durch eine (mindestens) konstante Geschwindigkeit des Informationsübertrags aus der Anfangsbedingung in die zeitliche Folge oder auch durch das im Zeitablauf exponentielle Auseinanderlaufen benachbarter Bewegungen im Endlichen. (Die Ergänzung der endlichen Bewegung ist wesentlich, da es lineare unbegrenzte Systeme gibt, die auch exponentielles Auseinanderlaufen aufweisen, z.B.: $\ddot{x} = x$).

---

## Page 33

(Lernteil, Abschn. 15)

### 2.9 Ljapunov-Exponent

Im vorherigen Abschnitt wurde chaotische Bewegung definiert durch eine zeitlich (mindestens) konstante Geschwindigkeit $\lambda$ des Informationsübertrags aus dem Anfangswert in die zeitliche Folge, was einem im Zeitablauf exponentiellen Auseinanderlaufen anfänglich benachbarter Trajektorien äquivalent ist. Die Geschwindigkeit $\lambda$ wird auch als Ljapunov-Exponent bezeichnet. Im Folgenden soll der Ljapunov-Exponent genauer definiert werden.

Zur Klarheit beginnen wir wieder mit dem eindimensionalen diskreten Fall. Die Bewegung wird durch die Abbildung (2.8.2) beschrieben:
$$q_m = f(q_{m-1}), \quad m=1,2,... \quad (2.9.1)$$
Bezeichnen wir mit $z_0$ eine infinitesimale Abweichung (Störung) vom Anfangspunkt $q_0$ und mit $z_m$ die sich durch die zeitliche Entwicklung ergebende Abweichung von $q_m$. Ein exponentielles Auseinanderlaufen benachbarter Trajektorien bedeutet im Mittel das folgende Verhalten des Streckungsfaktors $\alpha(m)$
$$|\alpha(m)| = \frac{|z_m|}{|z_0|} = A e^{\lambda(m)m}. \quad (2.9.2)$$
für $\lambda(m)$ erhalten wir also
$$\lambda(m) = \frac{1}{m} \ln \frac{|z_m|}{|z_0|} = \frac{1}{m} \ln |\alpha(m)|. \quad (2.9.3)$$
Dieses $\lambda(m)$ wird i.a. noch von $m$ abhängen. Als Ljapunov-Exponent definiert man nun den Grenzwert von $\lambda(m)$ für $m \to \infty$ als globale Kenngröße für die Trajektorie:
$$\lambda = \lim_{m \to \infty} \lambda(m) = \lim_{m \to \infty} \frac{1}{m} \ln \frac{|z_m|}{|z_0|} = \lim_{m \to \infty} \frac{1}{m} \ln |\alpha(m)|. \quad (2.9.4)$$
Der Ljapunov-Exponent charakterisiert also über die Bahn gemittelte (zeitliche) Veränderung einer kleinen Störung. $\lambda > 0$ bedeutet ein exponentielles Auseinanderlaufen (Divergenz), $\lambda = 0$ eine Neutralität und $\lambda < 0$ eine exponentielle Annäherung (Konvergenz) eng benachbarter Trajektorien.

Im kontinuierlichen $n$-dimensionalen Fall definiert man $n$ Ljapunov-Exponenten. Man beobachtet die zeitliche Entwicklung von Punkten im Phasenraum, die zur Zeit $t=0$ auf einer infinitesimalen $n$-dimensionalen Sphäre um den Startwert $q_0$ der Referenztrajektorie liegen [64,65]. Im Zeitablauf verformt sich die $n$-Sphäre, sie wird zu einem $n$-Ellipsoid, dessen Volumen wegen der vorhandenen Dissipation kleiner als das der Sphäre ist. Die Hauptachsen $z^{(i)}(t)$ dieses Ellipsoids werden zeitabhängig sein.