## Page 25

Für kleine Ausschläge ($\varphi \ll 1$, $k \ll 1$) ergibt sich eine Entwicklung bzgl. $k \sin x$:
$$K(k,x) = \int_{x_0}^{x} \frac{dx}{\sqrt{1-k^2 \sin^2 x}} = \int_{x_0}^{x} \left[1 + \frac{1}{2} k^2 \sin^2 x + \frac{3}{8} k^4 \sin^4 x + ...\right] dx$$
Beschränkung auf den ersten Term liefert:
$$t-t_0 = \pm \sqrt{\frac{I}{mgl}} \frac{\varphi}{2}$$
und damit für $\varphi(t)$
$$\sin \frac{\varphi}{2} = \sin \frac{\varphi_0}{2} \cos \left(\sqrt{\frac{mgl}{I}} (t-t_0)\right)$$
$$\varphi = \varphi_0 \cos \left(\sqrt{\frac{mgl}{I}} (t-t_0)\right)$$
Für das mathematische Pendel mit $I=ml^2$ ergibt sich $\omega = \sqrt{\frac{g}{l}}$.

---

$\dot{\varphi} = \frac{d\varphi}{dt}$
$$\frac{d\varphi}{dt} = \pm \sqrt{\frac{2mgl}{I} (\cos \varphi + 1)} = \pm \sqrt{\frac{2mgl}{I}} 2 \cos^2 \frac{\varphi}{2}$$
für $t=t_0$ liefert dies auch den Zusammenhang zwischen $\varphi(t_0)$ und $\dot{\varphi}(t_0)$.
„Trennen der Variablen“ und Substitution $\psi = \frac{\varphi}{2}$ liefern:
$$t-t_0 = \pm \sqrt{\frac{I}{mgl}} \int \frac{d\psi}{\cos \psi}$$
Zur Vereinfachung (aber ohne Beschränkung der Allgemeinheit) können wir $\dot{\varphi}(t_0)=0$ wählen.
Die Substitution $u = \tan \psi$, d.h. $\cos \psi = \frac{1}{\sqrt{1+u^2}}$, $d\psi = \frac{du}{1+u^2}$ führt auf:
$$\pm (t-t_0) = \sqrt{\frac{I}{mgl}} \int \frac{du}{\sqrt{1-u^2}}$$
Das Integral ergibt die Funktion $z = \text{Artanh } u$ 1) ("Areastangenshyperbolicus"), die Umkehrfunktion des hyperbolischen Tangens, also $u = \tanh z = \frac{e^z - e^{-z}}{e^z + e^{-z}} = \frac{e^{2z}-1}{e^{2z}+1}$. Diese Relation kann nach $z$ aufgelöst werden, was eine Darstellung von Artanh $u$ durch die Logarithmusfunktion liefert: $z = \text{Artanh } u = \frac{1}{2} \ln \frac{1+u}{1-u}$ somit
$$\pm (t-t_0) = \sqrt{\frac{I}{mgl}} \text{Artanh} \left(\tan \frac{\varphi}{2}\right) = \frac{1}{2} \sqrt{\frac{I}{mgl}} \ln \left(\frac{1+\tan \frac{\varphi}{2}}{1-\tan \frac{\varphi}{2}}\right) = \frac{1}{2} \sqrt{\frac{I}{mgl}} \ln \left(\tan \left(\frac{\pi}{4} + \frac{\varphi}{2}\right)\right)$$
(das letzte Gleichheitszeichen folgt aus dem entsprechenden Additionstheorem) und damit
$$\varphi(t) = 4 \arctan \left(e^{\pm \sqrt{\frac{mgl}{I}} (t-t_0)}\right) - \pi,$$
wobei $y = \text{arctan } x$ ("Arcustangens") die Umkehrfunktion des Tangens bedeutet, d.h. $x = \tan y$. Die beiden Vorzeichen entsprechen den beiden Ästen der Separatrix (positive und negative Winkelgeschwindigkeit). Das Besondere dieser Lösung besteht darin, daß die Punkte $\pm \pi$ bzw. $-\pi$ nur asymptotisch für $t \to \pm \infty$ erreicht werden können. Die Separatrix (im Phasenraum) repräsentiert somit - im Gegensatz zu den anderen Phasenbahnen - nicht eine, sondern drei Lösungen (Ruhe in instabiler Gleichgewichtslage $\varphi = \pi$, bzw. $\varphi = -\pi$ sowie eine ein- und eine auslaufende Lösung).

1) Beweis von $z = \int \frac{du}{1-u^2} = \text{Artanh } u$ bzw., nach Bildung des totalen Differentials, von $(1-u^2) dz = du$ mit $u = \tanh z$: Nun ist aber $du = d(\tanh z) = (1-\tanh^2 z) dz = (1-u^2) dz$.
63

---

3. $T$ ergibt sich als das Vierfache der Zeit, in der das Pendel den Winkelbereich von $\varphi_0$ bis 0 durchläuft. Aus (A2.a) und (A2.b) folgt:
$$T = 4 \sqrt{\frac{I}{mgl}} \int_0^{\varphi_0} \frac{d\varphi}{\sqrt{2(\cos \varphi - \cos \varphi_0)}} = 4 \sqrt{\frac{I}{mgl}} \int_0^{\varphi_0} \frac{d\varphi}{\sqrt{4(\sin^2 \frac{\varphi_0}{2} - \sin^2 \frac{\varphi}{2})}}$$
Entwicklung der Potenzen von $k$ bzgl. $\varphi_0$:
$$k = \sin \frac{\varphi_0}{2} = \frac{\varphi_0}{2} - \frac{\varphi_0^3}{48} + \frac{\varphi_0^5}{1920} - ...$$
$$k^2 = \frac{\varphi_0^2}{4} - \frac{\varphi_0^4}{24} + \frac{\varphi_0^6}{240} - ...$$
$$k^4 = \frac{\varphi_0^4}{16} - \frac{\