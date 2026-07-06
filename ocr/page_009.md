## Page 31

Größenordnung $\Delta q_0 \sim 10^{-(n+1)}$. Nach der Zeit $\Delta t$ ist der Abstand auf die Größenordnung $10^{-n}$ angewachsen usw., und nach der Zeit $n\Delta t$ auf die Größenordnung $10^{-1}$.
Wir haben also
$$\Delta q(t=n\Delta t) \sim 10^{-n} = 10^{-(n+1)} e^{\lambda n\Delta t}$$
Die diese Abschätzung für beliebige $n=t/\Delta t$ gilt, kann man auch schreiben
$$\Delta q(t) \sim \Delta q_0 e^{\lambda t}$$
Daraus ergibt sich für das Verhältnis
$$\frac{\Delta q(t)}{\Delta q_0} \sim e^{\lambda t}$$
Wir haben also, wie behauptet, ein exponentielles Wachstum des Abstands zwischen ursprünglich benachbarten Trajektorien und damit eine äußerst empfindliche Abhängigkeit des Bahnverlaufs von den Anfangsbedingungen. Der Parameter $\lambda$ heißt Ljapunov-Exponent und ist ein positive Zahl. Er gibt die Geschwindigkeit an, mit der die im Anfangswert enthaltene Information abgegriffen und in die zeitliche Folge übertragen wird. ($\ln 10$ ist die in einer Dezimalstelle enthaltene Information).

Dieses Phänomen hat "katastrophale" Folgen für die Vorhersagbarkeit. Die Anfangswerte sind bei Messung oder Berechnung eines physikalischen Vorgangs niemals belie