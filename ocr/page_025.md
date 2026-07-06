## Page 62
Für kleine Ausschläge ($\varphi \ll 1$, $k \ll 1$) ergibt sich eine Entwicklung bzgl. $k \sin x$:
$$K(k,x) = \int_{x_0}^{x} \frac{dx}{\sqrt{1-k^2 \sin^2 x}} = \int_{x_0}^{x} \left[1 + \frac{1}{2} k^2 \sin^2 x + \frac{3}{8} k^4 \sin^4 x + ... \right] dx$$
Beschränkung auf den ersten Term liefert:
$$t-t_0 = \pm \sqrt{\frac{I}{mgl}} \frac{\varphi}{2}$$
und damit für $\varphi(t)$
$$\sin \frac{\varphi}{2} = \sin \frac{\varphi_0}{2} \cos \left( \sqrt{\frac{mgl}{I}} (t-t_0) \right)$$
$$\varphi = \varphi_0 \cos \left( \omega (t-t_0) \right) \text{ mit } \omega = \sqrt{\frac{mgl}{I}}$$
Für das mathematische Pendel mit $I=ml^2$ ergibt sich $\omega = \sqrt{\frac{g}{l}}$.

3. $T$ ergibt sich als das Vierfache der Zeit, in der das Pendel den Winkelbereich von $\varphi_0$ bis 0 durchläuft. Aus (A2.a) und (A2.b) folgt:
$$T = 4 \sqrt{\frac{I}{mgl}} \int_0^{\varphi_0} \frac{d\varphi}{\sqrt{\cos \varphi - \cos \varphi_0}} = 4 \sqrt{\frac{I}{mgl}} \int_0^{\pi/2} \frac{dx}{\sqrt{1-k^2 \sin^2 x}} = 4 \sqrt{\frac{I}{mgl}} K(k,\pi/2)$$
Entwicklung der Potenzen von $k$ bis $\varphi_0$ ergibt:
$$k = \sin \frac{\varphi_0}{2} = \frac{\varphi_0}{2} \left( 1 - \frac{\varphi_0^2}{24} + ... \right), \quad k^2 = \frac{\varphi_0^2}{4} \left( 1 - \frac{\varphi_0^2}{12} + \frac{\varphi_0^4}{384} + ... \right), \quad k^4 = \frac{\varphi_0^4}{16} \left( 1 - \frac{\varphi_0^2}{6} + ... \right)$$
$$K(k,\pi/2) = \frac{\pi}{2} \left( 1 + \frac{1}{4} k^2 + \frac{9}{64} k^4 + ... \right)$$
und damit
$$T = 2\pi \sqrt{\frac{I}{mgl}} \left( 1 + \frac{1}{16} \varphi_0^2 + \frac{11}{3072} \varphi_0^4 + ... \right)$$
Die Periodendauer hängt also von der Amplitude und damit von den Anfangsbedingungen ab; sie erhöht sich mit wachsender Amplitude.
Beschränkung auf den ersten Term (kleine Ausschläge) liefert
$$T = 2\pi \sqrt{\frac{I}{mgl}}$$
für das mathematische Pendel also $T = 2\pi \sqrt{\frac{l}{g}}$.

4. Der maximal mögliche Wert des Ausschlagwinkels ist $\pi$, bei höherer Energie wird ein freies ungedämpftes Pendel eine Rotationsbewegung ausführen. Der Energieerhaltungssatz ergibt für $E = W_{pot,max} = mgl$:
$$\frac{1}{2} I \dot{\varphi}^2 - mgl \cos \varphi = mgl.$$
damit lautet die Differentialgleichung für die Separatrix:
62
---
## Page 63
$\dot{\varphi}$
$\frac{d\varphi}{dt}$
$$\frac{d\varphi}{dt} = \pm \sqrt{\frac{2mgl}{I} (\cos \varphi + 1)} = \pm 2 \sqrt{\frac{mgl}{I}} \cos \frac{\varphi}{2}$$
für $t=t_0$ liefert dies auch den Zusammenhang zwischen $\dot{\varphi}(t_0)$ und $\varphi(t_0)$.
„Trennen der Variablen“ und Substitution $\psi = \frac{\varphi}{2}$ liefern:
$$t-t_0 = \pm \sqrt{\frac{I}{mgl}} \int \frac{d\psi}{\cos \psi}$$
Zur Vereinfachung (aber ohne Beschränkung der Allgemeinheit) können wir $\dot{\varphi}(t_0)=0$ wählen.
Die Substitution $u = \tan \psi$, d.h. $\cos \psi = \frac{1-u^2}{1+u^2}$, $d\psi = \frac{2}{1+u^2} du$, führt auf:
$$\pm (t-t_0) = \sqrt{\frac{I}{mgl}} \int \frac{2}{1-u^2} du$$
Das Integral ergibt die Funktion $z = \text{Artanh } u$ $^{1)}$ („Areatangenshyperbolicus“), die Umkehrfunktion des hyperbolischen Tangens, also $u = \tanh z = \frac{e^z - e^{-z}}{e^z + e^{-z}} = \frac{e^{2z}-1}{e^{2z}+1}$. Diese Relation kann nach $z$ aufgelöst werden, was eine Darstellung von Artanh $u$ durch die Logarithmusfunktion liefert: $z = \text{Artanh } u = \frac{1}{2} \ln \frac{1+u}{1-u}$, somit
$$\pm (t-t_0) = 2 \sqrt{\frac{I}{mgl}} \text{Artanh} \left( \tan \frac{\varphi}{4} \right) = \sqrt{\frac{I}{mgl}} \ln \left( \frac{1+\tan \frac{\varphi}{4}}{1-\tan \frac{\varphi}{4}} \right) = \sqrt{\frac{I}{mgl}} \ln \left( \tan \left( \frac{\pi}{4} + \frac{\varphi}{4} \right) \right)$$
(das letzte Gleichheitszeichen folgt aus dem entsprechenden Additionstheorem) und damit
$$\varphi(t) = 4 \arctan \left( e^{\pm \sqrt{\frac{mgl}{I}} (t-t_0)} \right) - \pi,$$
wobei $y = \text{arctan } x$ („Arcustangens“) die Umkehrfunktion des Tangens bedeutet, d.h. $x = \tan y$. Die beiden Vorzeichen entsprechen den beiden Ästen der Separatrix (positive und negative Winkelgeschwindigkeit). Das Besondere dieser Lösung besteht darin, daß die Punkte $\pm \pi$ bzw. $-\pi$ nur asymptotisch für $t \to \pm \infty$ erreicht werden können. Die Separatrix (im Phasenraum) repräsentiert somit – im Gegensatz zu den anderen Phasenbahnen – nicht eine, sondern drei Lösungen (Ruhe in instabiler Gleichgewichtslage $\varphi = \pi$, bzw. $\varphi = -\pi$ sowie eine ein- und eine auslaufende Lösung).

$^{1)}$ Beweis von $z = \int \frac{du}{1-u^2}$: Nun ist aber $du = d(\tanh z) = (1-\tanh^2 z) dz = (1-u^2) dz$.
63