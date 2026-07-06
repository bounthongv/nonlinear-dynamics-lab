## Page 46
Anhang V:
---
**Zur numerischen Bestimmung der Ljapunov-Exponenten**

Die Bewegungsgleichung der Störung $z^{(1)}(t)$ (2.9.6) oder (2.9.7) kann folgendermaßen geschrieben werden:
$$ \frac{dz^{(1)}}{dt} = DF(q)z^{(1)} $$
(v.1)
Für unser getriebenes Pendel mit linearer Reibung, z.B., gilt für den Störungsvektor $z^{(1)}$ das mit der i.a. zeitabhängigen Koeffizientenmatrix $DF(q)$:
$$ DF(\varphi, \dot{\varphi}) = \begin{pmatrix} 0 & 1 \\ -\frac{mgl}{I}\cos\varphi - \frac{b}{I} & 0 \end{pmatrix} $$
(v.2)
Löst man das gekoppelte System aus (2.8.1) und (v.1) zur Anfangsbedingung $(x_0, z_0^{(1)})$ so erhält man $z^{(1)}(t)$ für die Berechnung der Ljapunov-Exponenten. Für jeden der Störungsvektoren $z^{(1)}(t)$ (i=1,2,3) muß man also ein System von 3 Differentialgleichungen lösen. Für die Berechnung der 3 Ljapunov-Exponenten müssen demzufolge 9 Differentialgleichungen für die Referenztrajektorie, insgesamt also 12 gekoppelte Differentialgleichungen, simultan integriert werden. In der dritten Zeile von (v.2) sind alle Elemente Null. Das bedeutet, daß Störungen in der Zeitrichtung konstant bleiben. Dieser Richtung entspricht damit ein verschwindender Ljapunov-Exponenten. Daher muß die obige Prozedur nur noch für den zur Zeitrichtung orthogonalen zweidimensionalen Unterraum durchgeführt werden; wozu nur noch mit zwei zweikomponentigen Störungsvektoren zu rechnen ist, d.h. es verbleiben nur noch 4 Differentialgleichungen. Zur praktischen Berechnung der Referenztrajektorie wird auf die nichtautonome Formulierung (2.1.2) zurückgegriffen. Es sind also 6 gekoppelte Differentialgleichungen simultan zu lösen.

Die direkte numerische Auswertung der Ljapunov-Exponenten nach (2.9.5) ist nicht möglich. Es treten folgende Probleme auf:
1. Wegen der exponentiellen Entwicklung des Abstandes zwischen benachbarten Trajektorien führen positive Ljapunov-Exponenten zum Überschreiten des Zahlenbereiches (Overflow) und negative Ljapunov-Exponenten zum Unterschreiten des Zahlenbereiches (Underflow) des Computers.
2. Bei freier Wahl eines Startvektors $z_0$, stellt sich das entstehende $z^{(1)}(t)$ in die zum größten Ljapunov-Exponenten gehörende Richtung ein. Aufgrund dieser Eigenschaft konnte zunächst

46

---

## Page 47
nur ein numerisches Verfahren zur Bestimmung des größten LE angegeben werden. Eine Bestimmung der weiteren LE wird verhindert.

Zur Lösung dieser Probleme gehen wir folgendermaßen vor: Zunächst bestimmen wir eine Referenztrajektorie aus (2.8.1). Dann wählen wir $n$ paarweise orthonormale Anfangsstörungen $z_0^{(i)}$ (i=1,2,...,n).
$$ (z_0^{(i)}, z_0^{(j)}) = \begin{cases} 1, & \text{falls } i=j \\ 0, & \text{sonst} \end{cases} $$
$((.,.))$ bezeichnet das Skalarprodukt, d.h., $(a,b) = \sum_{k=1}^n a_k b_k$.

Die zeitliche Entwicklung dieser Störungsvektoren um die Referenztrajektorie errechnen wir aus dem System von Differentialgleichungen (v.1). Aus den $z_0^{(i)}$ entstehen zu einer späteren Zeit die $z^{(i)}$. Die beiden oben genannten Probleme können durch wiederholte Anwendung des Schmidtschen Orthonormalisierungsverfahrens überwunden werden, welches aus den (i.a. nicht mehr zueinander orthogonalen) $z^{(i)}$ den folgenden orthonormalen Satz $\tilde{z}^{(i)}$ erzeugt:
$$ \tilde{z}^{(1)} = \frac{z^{(1)}}{\alpha^{(1)}} \quad \text{mit } \alpha^{(1)} = |z^{(1)}| $$
$$ \tilde{z}^{(2)} = \frac{z^{(2)} - (z^{(2)}, \tilde{z}^{(1)})\tilde{z}^{(1)}}{\alpha^{(2)}} \quad \text{mit } \alpha^{(2)} = |z^{(2)} - (z^{(2)}, \tilde{z}^{(1)})\tilde{z}^{(1)}| $$
$$ \tilde{z}^{(3)} = \frac{z^{(3)} - (z^{(3)}, \tilde{z}^{(1)})\tilde{z}^{(1)} - (z^{(3)}, \tilde{z}^{(2)})\tilde{z}^{(2)}}{\alpha^{(3)}} \quad \text{mit } \alpha^{(3)} = |z^{(3)} - (z^{(3)}, \tilde{z}^{(1)})\tilde{z}^{(1)} - (z^{(3)}, \tilde{z}^{(2)})\tilde{z}^{(2)}| $$
$$ \dots $$
$$ \tilde{z}^{(l)} = \frac{z^{(l)} - \sum_{i=1}^{l-1} (z^{(l)}, \tilde{z}^{(i)})\tilde{z}^{(i)}}{\alpha^{(l)}} \quad \text{mit } \alpha^{(l)} = \left|z^{(l)} - \sum_{i=1}^{l-1} (z^{(l)}, \tilde{z}^{(i)})\tilde{z}^{(i)}\right| $$
(v.3)
$\alpha^{(l)}$, $l=1,2,...,n$ sind also die Streckungsfaktoren der Störungsvektoren in einem einzelnen Schritt der Reorthonormierung (lokale Streckungsfaktoren). Die Wahl der Zeitschritte $\Delta t$, nach denen diese Reorthonormierung durchgeführt wird, ist nicht kritisch, solange weder die Betrags- noch Orientierungsdivergenzen die durch den Rechner gesetzten Grenzen nicht überschreiten. Als Richtwert für $\Delta t$ kann die Anregungsperiode oder der Integrationsschritt dienen.

Das Orthonormalisierungsverfahren beeinflußt die Richtung des ersten Vektors nicht, so daß sich dieser in die Richtung größter Streckung einstellen wird und $\alpha_1$ den zugehörigen lokalen Streckungsfaktor darstellt. Der zweite Vektor wurde um seine Komponente in Richtung des ersten reduziert und dann normiert; $z^{(2)}$ kann sich also nicht mehr in Richtung größter Streckung ausrichten, sondern er wird (nach hinreichend vielen Schritten) in Richtung der

47