## Page 40
Anhang ii : Fourierspektrum
Nach dem Satz von Fourier läßt sich jede periodische Funktion $f(t)$ mit der Periodendauer $T=2\pi/\omega_0$ durch eine Summe von Sinus- und Cosinusfunktionen mit den Kreisfrequenzen $\omega_0, 2\omega_0, 3\omega_0, ...$ darstellen:
$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos n\omega_0 t + b_n \sin n\omega_0 t).$$ (ii.1)
Diese Summe heißt Fourier-Reihe. Sie kann kompakt in komplexer Schreibweise geschrieben werden:
$$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{in\omega_0 t}.$$ (ii.2)
Zwischen den Koeffizienten $a_n, b_n$ aus (ii.1) und $c_n$ aus (ii.2) besteht der Zusammenhang
$$c_n = \begin{cases} \frac{a_0}{2} & n=0 \\ \frac{1}{2}(a_n - ib_n) & n>0 \\ \frac{1}{2}(a_n + ib_n) & n<0 \end{cases} \quad \text{bzw.} \quad \begin{cases} a_n = c