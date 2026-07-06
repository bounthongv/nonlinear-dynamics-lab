## Page 36

Abb. 2.9.1: Ljapunov-Exponenten
einer periodischen Bewegung
des getriebenen Pendels.

Systemparameter:
$m=0.2$ kg, $l=0.25$ m,
$\omega_A=4.176$/s
$b=0.04$ Nms, $A=0.535$ Nm.

Abb. 2.9.2: Ljapunov-Exponenten
einer chaotischen Bewegung des
getriebenen Pendels.

Systemparameter:
$m=0.2$ kg, $l=0.25$ m,
$\omega_A=4.176$/s
$b=0.04$ Nms, $A=0.58$ Nm.

Abb. 2.9.3: Ljapunov-Exponenten
in Abhängigkeit von der
Anregungsamplitude.

Systemparameter:
$m=0.2$ kg, $l=0.25$ m,
$\omega_A=4.176$/s
$b=0.04$ Nms.

---

Der Zusammenhang mit der Kapazität $d_C$ des Attraktors wird in der Kaplan-Yorke-Vermutung $d_C = d_L$ ausgesprochen. Damit wäre ein Zusammenhang zwischen der Kapazität und den Ljapunov-Exponenten hergestellt. Allerdings konnte die Hypothese bisher nicht bewiesen werden, sondern nur die Ungleichung $d_C \le d_L$ [9]. In [23] wurden die beiden Dimensionen für mehrere Systeme berechnet. Dadurch ließ sich zeigen, daß die Kaplan-Yorke-Vermutung eine gute Approximation liefert, insbesondere für "typische" Attraktoren, bei denen die Punkte gleichmäßig verteilt sind (siehe auch [22]).

$$d_L = j + \frac{\lambda_j}{\vert \lambda_{j+1} \vert}$$

Im 2-dimensionalen Unterraum $(\varphi, \dot{\varphi})$ des getriebenen Pendels ist die Dimension des stroboskopierten Attraktors

$$d_L = d_L = 1 + \frac{\lambda_1}{\vert \lambda_2 \vert} \quad \text{(2.9.9)}$$

Nach der Definition der Ljapunov-Exponenten ist die Berechnung der durchschnittlichen Rate der Divergenz oder Konvergenz für ein unendliches Zeitintervall erforderlich. In der Praxis muß man aber die Iteration bei endlichen Zeiten abbrechen.

In diesem Programm werden für die Berechnung der Ljapunov-Exponenten zwei Varianten verwendet:
1.  Berechnung der LE für einen bestimmten Parametersatz und gleichzeitig Darstellung der Ergebnisse. Die Berechnungszeit ist also gleich der jeweils aktuellen Zeit. Auf diese Weise kann man auch das Einschwingverhalten verfolgen. Die am Anfang auseinanderlaufenden Trajektorien (kein LE $> 0$) können nach dem Einschwingen konvergieren (kein LE $< 0$) und umgekehrt. (Bsp. in Abb. 2.9.1,2.9.2).
2.  Die Ljapunov-Exponenten werden als Funktionen des Kontrollparameters (Anregungsamplitude, Dämpfungskoeffizient oder Erregerfrequenz) berechnet. Für jeden Parametersatz werden sie über eine einstellbare Zeitspanne ermittelt ${}^1)$. Dadurch gewinnt man eine Übersicht über die Entwicklung des Systems in Abhängigkeit von der äußeren Anregung. Wo die periodischen Bewegungen stattfinden, sind beide LE $< 0$, und wo die chaotischen Bewegungen auftreten, ist $\lambda_1 > 0$. An den Stellen, wo $\lambda_1 = 0$ ist, treten Bifurkationen auf. (Bsp. in Abb. 2.9.3).

${}^1)$ Bezüglich der Anfangsbedingungen siehe Fußnote in 2.6.

36