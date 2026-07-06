## Page 56
Kapitel II: Aufgaben

Mathematisches Pendel
1. Leiten Sie aus der Bewegungsgleichung des freien ungedämpften Pendels den Energiesatz
$W_{kin}(\dot{\varphi}(t)) + W_{pot}(\varphi(t)) = E = \text{const}$
ab, indem Sie die Bewegungsgleichung mit $\dot{\varphi}$ multiplizieren und geeignet umformen.

2. Bei Gültigkeit des Energiesatzes kann die Lösung eines eindimensionalen
Bewegungsproblems auf eine Integration zurückgeführt werden, indem man den Energiesatz
zunächst nach $\dot{\varphi}$ auflöst: $d\varphi/dt = R(\varphi)$ und ein "Trennen der Variablen" durchführt, gemäß
$$t - t_0 = \int_{\varphi(t_0)}^{\varphi(t)} \frac{d\varphi}{R(\varphi)}$$
Wie lautet $R(\varphi)$ für das Pendel? Lösen Sie das Integral für kleine Ausschläge ($\sin \varphi \approx \varphi$). Für
das nichtlineare Pendel ergeben sich sog. elliptische Integrale, die nicht elementar integrierbar
sind.
Hinweis: Wählen Sie die Anfangsbedingung $\dot{\varphi}(t_0) = 0$. Drücken Sie die Gesamtenergie $E$
durch den maximalen Ausschlag $\varphi_{max}$ aus und verwenden Sie das Additionstheorem $\cos \varphi = 1 - 2\sin^2(\varphi/2)$.
Substituieren Sie im Integral $\sin \varphi/2 = \sin x$. Machen Sie nun erst die Näherung $\varphi_0 \ll 1$.

3. Berechnen Sie, ausgehend vom Resultat der vorherigen Aufgabe, die Schwingungsdauer
$T = T(\varphi_0)$ in Abhängigkeit von der Amplitude $\varphi_0$. Für beliebige Ausschläge erhalten Sie ein
elliptisches Integral. Bestimmen Sie $T(\varphi_0)$ zunächst für nicht zu große $\varphi_0$, indem Sie den
Integranden bzgl. $\varphi_0$ in eine Taylorreihe (bis $\varphi_0^2$) entwickeln.

4. Für das Pendel erhält man die Separatrix, die Schwingungslösungen ($E < W_{pot,max}$) von
Rotationslösungen ($E > W_{pot,max}$) trennt, falls die Gesamtenergie gleich dem Maximalwert der potentiellen Energie ist. Wie lauten dann $R(\varphi)$
und die Lösung des Integrals aus Aufgabe 2? Was ist das Besondere an dieser Lösung?
Welcher Zusammenhang muß zwischen Anfangswinkel $\varphi_0$ und Anfangswinkel-
geschwindigkeit $\dot{\varphi}_0$ bestehen, damit die Separatrix realisiert wird? Prüfen Sie die Lösung
numerisch im Experimentierteil nach.

5. Nach welcher Zeit ist die Amplitude des freien linear gedämpften Pendels bei kleinen
Ausschlägen ($\sin \varphi \approx \varphi$) auf den $e$-ten Teil ihres Anfangswertes gesunken? Prüfen Sie Ihr

---
## Page 57
Ergebnis durch numerische Berechnungen im Experimentierteil für verschiedene
Parameterwerte.

6. a. Wie lautet der Zusammenhang zwischen den Integrationskonstanten in der Lösung (2.4.2)
und den Anfangsbedingungen beim getriebenen Pendel mit linearer Reibung bei kleinen
Ausschlägen ($\sin \varphi \approx \varphi$)?
b. Charakterisieren Sie die Bewegung bei verschwindender Reibung (aber stets $\omega_A \neq \omega_0$),
insbesondere im Falle $\omega_A = \omega_0(1+\epsilon)$ ($\epsilon \ll 1$).
c. Führen Sie den Grenzübergang $\omega_A \rightarrow \omega_0$ aus, wie verhält sich die Lösung in diesem
Resonanzfall? Studieren Sie im Experimentierteil numerisch dieses Verhalten.

7. Wieviel unabhängige Parameter bestimmen das Lösungsverhalten des getriebenen Pendels
mit linearer Dämpfung?
Hinweis: Schreiben Sie die Bewegungsgleichung in geeigneten dimensionslosen Variablen.

8. Betrachten wir die Resonanzkurve des getriebenen Pendels in der Abbildung 2.4.2 (oder im
Lernteil des Programms, Abschn. 5), so sehen wir, daß es für bestimmte Werte der
Anregungsamplitude einen Frequenzbereich gibt, wo zwei verschiedene Schwingungen
möglich sind, d.h., zwei Attraktoren koexistieren. Bestimmen Sie mit Hilfe des
Bifurkationsdiagramms bei konstanter Anregungsfrequenz den Koexistenzbereich der beiden
Attraktoren bezüglich der Anregungsamplitude.
Parametersatz: $m=0.2$ kg, $l=0.25$ m, $b=0.02$ Nms, $\omega_A=4.176/s=2\omega_0/3$;
Anfangsbedingung: $\varphi_0=0$; $\dot{\varphi}_0=0$ und $\varphi_0=150^\circ$.
Hinweis: Um große Schrittweiten bei der Berechnung eines Bifurkationsdiagramms zu erreichen, wählen Sie
einen großen maximalen Amplitudenwert und brechen die Berechnung rechtzeitig ab. Studieren Sie das
Systemverhalten an den kritischen Punkten (Anfang und Ende des Koexistenzbereiches) genauer.

9. Benutzen Sie das Bifurkationsdiagramm des getriebenen Pendels, um die Feigenbaumzahl zu
bestimmen. Um die Bifurkationen bis zu höheren Periodizitäten auflösen zu können, berechnen
Sie das Bifurkationsdiagramm für feinere Schrittweiten des Parameters $A$.
Parametersatz: $m=0.2$ kg, $l=0.25$ m, $b=0.04$ Nms, $\omega_A=4.176/s$;
Empfohlene Anregungsamplitude $A = 0.540$ Nm $\pm$ $0.541$ Nm;
Berechnungszeiten $t_{min}=900$ s; $t_{max}=1200$ s;
Anfangsbedingung $\varphi_0=135^\circ$; $\dot{\varphi}_0=0$.

10. Untersuchen Sie das getriebene Pendel für die Systemparameter
$m=0.2$ kg, $l=0.25$ m, $b=0.0033$ Nms, $\omega_A=4.6/s$, $A=0.1795$ Nm. Anfangsbed.: $\varphi_0=0$, $\dot{\varphi}_0=0$.
Welche Bewegung (periodisch oder chaotisch) führt das Pendel aus? Falls die Bewegung
periodisch ist, welche Periodizität hat sie?