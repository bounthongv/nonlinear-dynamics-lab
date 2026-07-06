## Page 42
Einsetzen von $c(\omega)$ und Vertauschen der Integrationsreihenfolge liefern
$$
f(t) = \lim_{\epsilon \to 0} \frac{1}{2\pi} \int_{-\infty}^{\infty} \left[ \int_{-\infty}^{\infty} e^{-i\omega(t-\tau)} e^{-\epsilon(\omega-\omega_0)^2} d\omega \right] f(\tau) d\tau
$$
Das Integral in der geschweiften Klammer kann berechnet werden (Auftrennen in ein Integral über die negativen $\omega$ und in eines über die positiven $\omega$) und ergibt:
$$
\frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-i\omega(t-\tau)} e^{-\epsilon(\omega-\omega_0)^2} d\omega = \frac{1}{2\pi} \sqrt{\frac{\pi}{\epsilon}} e^{-\frac{(t-\tau)^2}{4\epsilon}} e^{-i\omega_0(t-\tau)}
$$
also eine symmetrische Funktion der Höhe $1/\epsilon$ und der Breite $\sqrt{\epsilon}$ um den Punkt $t=\tau$, deren Integral über $t$ gleich eins ist (in der Grenze $\epsilon \to 0$ wird diese Funktion als Diracsche Deltafunktion bezeichnet). Also erhalten wir die gewünschte Intensität
$$
f(t) = \lim_{\epsilon \to 0} \int_{-\infty}^{\infty} \delta_\epsilon(t-\tau) f(\tau) d\tau = f(t)
$$
da zu dem $\tau$-Integral nur eine Umgebung der Breite $\epsilon$ um den Punkt $t=\tau$ beiträgt, ist $f(\tau)$ hinreichend klein, so kann $f(\tau)$ in diesem Bereich als konstant betrachtet und als $f(t)$ vor das Integral gezogen werden und es verbleibt das Integral über $\delta_\epsilon(t-\tau)$, was eins liefert.

Die Spektralfunktion $c(\omega)$ wird als die Fouriertransformierte der Zeitfunktion $f(t)$ bezeichnet. Die Fouriertransformierte $c(\omega)$ ist im allgemeinen eine komplexe Funktion $^2)$. Man definiert eine reelle Funktion $s(\omega) = |c(\omega)|^2$, die sogenannte spektrale Leistungsdichte oder kurz das Leistungsspektrum von $f(t)$, welches in unserem Simulationsprogramm berechnet wird. Einen schnellen Algorithmus (Fast-Fourier-Transformation: FFT) und Beispielprogramme zur Berechnung der diskreten Fourier-Transformation findet man in [67,68].

---
$^2$) Für eine reelle Funktion $f^*(t) = f(t)$ folgt $c(-\omega) = c^*(\omega)$.
Beweis: $c^*(\omega) = \frac{1}{2\pi} \int_{-\infty}^{\infty} f(t) e^{i\omega t} dt = c(-\omega)$.
42

## Page 43
Anhang iii:
Veränderung des Phasenraumvolumens
Es seien $q_i$ ($i=1,2,...,n$) die Zustandsvariablen eines dynamischen Systems. Die Bewegungsgleichungen des Systems sind:
$$
\dot{q}_i = F_i(q_1, q_2, ..., q_n, t) \quad \text{(iii.1)}
$$
Wir betrachten die zeitliche Entwicklung eines infinitesimalen Phasenraumvolumens
$$
\delta V = \delta q_1 \delta q_2 ... \delta q_n = \prod_{i=1}^n \delta q_i
$$
In der Zeit $dt$ ändert sich dieses Volumen um:
$$
d\delta V = \delta V'(t+dt) - \delta V(t) = \prod_{i=1}^n \delta q_i(t+dt) - \prod_{i=1}^n \delta q_i(t) \quad \text{(iii.2)}
$$
Taylorentwicklung von $\delta q_i(t+dt)$ um $t$ bis zum ersten Glied ergibt:
$$
\delta q_i(t+dt) = \delta q_i(t) + \dot{\delta q_i}(t) dt
$$
Mit den Bewegungsgleichungen (iii.1) folgt:
$$
\dot{\delta q_i}(t) = F_i(q_1,...,q_i+\delta q_i,...,q_n) - F_i(q_1,...,q_n) = \frac{\partial F_i}{\partial q_i} \delta q_i
$$
und damit
$$
\delta q_i(t+dt) = \left[1 + \frac{\partial F_i}{\partial q_i} dt\right] \delta q_i
$$
Die Volumenänderung wird nun
$$
d\delta V = \prod_{i=1}^n \left[1 + \frac{\partial F_i}{\partial q_i} dt\right] \delta q_i - \prod_{i=1}^n \delta q_i
$$
Beschränkt man sich im ersten Produkt auf Terme erster Ordnung in $dt$, so erhält man:
$$
d\delta V = \sum_{i=1}^n \frac{\partial F_i}{\partial q_i} dt \delta V
$$
Damit kann die relative Volumenänderung pro Zeit geschrieben werden als:
$$
\frac{1}{\delta V} \frac{d\delta V}{dt} = \sum_{i=1}^n \frac{\partial F_i}{\partial q_i} \quad \text{(iii.3)}
$$
---
$^1$) Faßt man die Gesamtheit der $F_i$ als Vektor $F = (F_1, F_2, ..., F_n)$ auf, so nennt man den Ausdruck auf der rechten Seite die Divergenz von $F$:
$$
\sum_{i=1}^n \frac{\partial F_i}{\partial q_i} = \text{div } F
$$
43