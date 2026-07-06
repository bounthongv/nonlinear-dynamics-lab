## Page 34
Der $i$-te Ljapunov-Exponent ist nun durch die mittlere Geschwindigkeit der Langzeitentwicklung der $i$-ten Hauptachse des Ellipsoids definiert:
$$
\lambda_i = \lim_{t \to \infty} \frac{1}{t} \ln \frac{|z^{(i)}(t)|}{|z^{(i)}(0)|},
$$ (2.9.5)
wobei $z^{(i)}(0)$ die $i$-te Achse des Ellipsoids zum Zeitpunkt $t=0$ ist.

Die Zeitentwicklung einer kleinen Störung erhalten wir aus (2.8.1) nach Taylorentwicklung bis zum linearen Glied (hier wird der Index $i$ weggelassen).
$$
\dot{q}(t) + \dot{z}(t) = F(q(t)+z(t)) = F(q) + \left(\frac{\partial}{\partial q} F(q)\right) \cdot z + \mathcal{O}(z^2)
$$
also
$$
\dot{z}(t) = \left(\frac{\partial}{\partial q} F(q)\right) \cdot z(t) \quad \text{bzw.} \quad \dot{z}_k(t) = \sum_{l=1}^n \frac{\partial F_k(q)}{\partial q_l} z_l(t), \quad i=1,...,n,
$$ (2.9.6)
oder in Matrixform
$$
\begin{pmatrix}
\dot{z}_1(t) \\
\dot{z}_2(t) \\
\vdots \\
\dot{z}_n(t)
\end{pmatrix}
=
\begin{pmatrix}
\frac{\partial F_1}{\partial q_1} & \frac{\partial F_1}{\partial q_2} & \dots & \frac{\partial F_1}{\partial q_n} \\
\frac{\partial F_2}{\partial q_1} & \frac{\partial F_2}{\partial q_2} & \dots & \frac{\partial F_2}{\partial q_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial F_n}{\partial q_1} & \frac{\partial F_n}{\partial q_2} & \dots & \frac{\partial F_n}{\partial q_n}
\end{pmatrix}
\begin{pmatrix}
z_1(t) \\
z_2(t) \\
\vdots \\
z_n(t)
\end{pmatrix}
$$ (2.9.7)
(Die Matrix wird auf oft mit $DF$ bezeichnet.)

Für jeden Störungsvektor muß man $n$ Differentialgleichungen erster Ordnung lösen. Im $n$-dimensionalen System sind das $n^2$ Gleichungen. Für die Referenztrajektorie hat man noch $n$ Ljapunov-Exponenten erfordert also insgesamt die simultane Lösung von $n^2+n$ gekoppelten Differentialgleichungen, wobei die Richtungen der Hauptachsen nicht bekannt sind und sich mit der Zeit ändern, da die Matrix in (2.9.7) zeitabhängig ist. Die praktische Berechnungsmethode für die Ljapunov-Exponenten finden Sie im Anhang V.
---
## Page 35
Gewöhnlich ordnet man die Ljapunov-Exponenten $\lambda_i$, $i=1,2,...n$ nach der Größe:
$$
\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n.
$$
Positive Ljapunov-Exponenten repräsentieren ein exponentielles Auseinanderlaufen der Trajektorien in bestimmten Richtungen, während negative Ljapunov-Exponenten dementsprechend eine exponentielle Annäherung in anderen Richtungen beschreiben. Die Existenz von zumindest einem positiven Ljapunov-Exponent bedeutet ein exponentielles Auseinanderlaufen von Nachbartrajektorien und damit sensible Abhängigkeit von den Anfangsbedingungen. Für die Entscheidung, ob chaotisches Verhalten vorliegt, genügt die Kenntnis des größten Ljapunov-Exponenten. Wir kommen somit zu der Definition
$$
\text{Chaos} \Leftrightarrow \lambda_1 > 0.
$$
D.h., um festzustellen, ob chaotisches oder periodisches Verhalten vorliegt, muß man die Ljapunov-Exponenten (LE) bestimmen. Sind alle LE negativ, so liegt periodisches oder quasiperiodisches Verhalten vor. Ist nur ein LE positiv, so handelt es sich um chaotisches Verhalten mit den in 2.8. diskutierten Eigenschaften.

Die Summe der LE ist für ein dissipatives System wegen des "Schrumpfens" des Phasenraumvolumens (siehe auch 2.3 und Anhang III) immer negativ und wird durch die dissipativen Terme in den Bewegungsgleichungen festgelegt (siehe Anhang IV). Für das in diesem Programm behandelte getriebene Pendel mit geschwindigkeitsproportionaler Reibung (2.1.3) gilt:
$$
\lambda_1 + \lambda_2 + \lambda_3 = -b/I,
$$ (2.9.7)
mit $b$ - Dämpfungskoeffizient, $I$ - Trägheitsmoment, wobei der zu der zur Trajektorie parallelen Richtung gehörende Ljapunov-Exponent stets verschwindet (siehe Anhang V).

Kennt man alle Ljapunov-Exponenten $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n$ eines autonomen Systems (mit $n$ dynamischen Variablen), so kann man die sogenannte Ljapunov-Dimension $d_L$ des Attraktors definieren:
$$
d_L = j + \frac{\sum_{i=1}^j \lambda_i}{|\lambda_{j+1}|} \quad \text{mit } j \text{ gemäß } \sum_{i=1}^j \lambda_i \ge 0 \text{ aber } \sum_{i=1}^{j+1} \lambda_i < 0,
$$ (2.9.8)
d.h. ein entsprechend gewähltes $j$ - dimensionales Volumenelement expandiert, während ein $(j+1)$-dimensionales schrumpft [9,14,23,25].

In unserem Fall ($\lambda_1 > \lambda_2 = 0 > \lambda_3$) ist also: $d_L = 2 + \frac{\lambda_1}{|\lambda_3|}$.

35