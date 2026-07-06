## Page 96
Ljapunoν-Dimension
Kennt man alle Ljapunov-Exponenten $\lambda_1 > \lambda_2 > ... > \lambda_n$ eines autonomen Systems (mit $n$ dynamischen Variablen), so kann man die sogenannte Ljapunov-Dimension $d_L$ des Attraktors definieren:
$$d_L = j + \frac{\lambda_1 + \lambda_2 + ... + \lambda_j}{|\lambda_{j+1}|}$$
(d.h. ein entsprechend gewähltes $j$ - dimensionales Volumenelement expandiert, während ein $(j+1)$-dimensionales schrumpft). Für unsere Systeme mit dreidimensionalem Phasenraum ($\lambda_1 > \lambda_2 > \lambda_3$) gilt also $d_L = 2 + \lambda_1 / |\lambda_3|$.
Der Zusammenhang mit der Kapazität $d_C$ des Attraktors wird in der Kaplan-Yorke-Vermutung (1979) $d_C = d_L$ ausgesprochen, welche für "typische" Attraktoren gültig ist (im allgemeinen sollte jedoch ein $\le$ Zeichen stehen).

Die Dimension des stroboskopierten Attraktors ist
$$d'_L = d_L - 1 = 1 + 2\lambda_1 / |\lambda_3|.$$
Verweis:
1. Dimension
2. Ljapunov-Exponent
3. Kapazität
Siehe auch Lernteil des Programms: Abschnitt 14 und Kapitel I dieses Heftes: Abschnitt 2.9.

---

Ljapunoν-Exponent
Ljapunoν-Exponenten (LE) $\lambda$ charakterisieren das exponentielle zeitliche Verhalten des Abstands $z$ eng (infinitesimal) benachbarter Trajektorien eines dynamischen Systems im zeitlichen Mittel ($z(t) = z_0 \exp(\lambda t)$). Sind alle LE negativ, so liegt exponentielle Konvergenz der Trajektorien vor. Ist auch nur ein LE positiv, so divergieren die Trajektorien exponentiell, d.h. die Bewegung ist empfindlich von den Anfangsbedingungen abhängig. Für ein dynamisches System gibt es so viele LE, wie dessen Zustandsraum Dimensionen hat. Die Summe der LE ist für ein dissipatives System immer negativ (da das Phasenraumvolumen schrumpfen muß) und wird durch die dissipativen Terme in den Bewegungsgleichungen festgelegt. Für die in diesem Programm behandelten Systeme gibt es jeweils drei Ljapunov-Exponenten; der zu der zur Trajektorie parallelen Richtung gehörende ist aber stets Null. Solange wir uns auf geschwindigkeitsproportionale Reibung beschränken, gilt für getriebenes Pendel, Pohlsches Rad und parametrisch getriebenes Pendel:
$\lambda_1 + \lambda_2 + \lambda_3 = -b/I$
und für den Federschwinger:
$\lambda_1 + \lambda_2 + \lambda_3 = -b/m$

---

## Page 97
Verweis:
1. Empfindliche Abhängigkeit von den Anfangsbedingungen
2. Dynamische Systeme
3. Phasenraum
4. Dimension
5. Ljapunov-Dimension
Siehe auch Lernteil des Programms: Abschnitt 14 und Kapitel I dieses Heftes: Abschnitt 2.9, Anhang iv.

---

Nichtautonomes System
Ein nichtautonomes System von Differentialgleichungen läßt sich in der Form:
$$\frac{dq_i}{dt} = F_i(q_1, q_2, ..., q_n, t); \quad i = 1, 2, ..., n;$$
schreiben, wobei die $F_i$ explizit von der Zeit $t$ abhängen.
Durch Einführen der Zeit (oder einer Funktion von ihr) als weitere dynamische Variable, z.B. $q_{n+1} = t$, mit $dq_{n+1}/dt = 1$ wird das ursprünglich nichtautonome System formal in ein autonomes System umgewandelt:
$$\frac{dq_i}{dt} = F_i(q_1, q_2, ..., q_n, q_{n+1}); \quad i = 1, 2, ..., n, n+1;$$
wobei sich dabei die Zahl der dynamischen Variablen und damit die Dimension des Phasenraumes um 1 erhöht hat.

Verweis:
1. Dynamische Systeme
2. Autonomes System
3. Phasenraum des getriebenen Pendels
Siehe auch Lernteil des Programms: Zusammenfassung I (Abschn. 9) und Kapitel I dieses Heftes: Abschnitt 2.1.

---

Nichtlineare Systeme
Systeme, die durch nichtlineare Differentialgleichungen modelliert werden, bezeichnet man als nichtlineare Systeme. Nichtlinearität ist fundamental für das gesamte Naturgeschehen. Viele nichtlineare Systeme aus Mechanik, Hydrodynamik, Elektrotechnik und anderen Wissenschaftsgebieten sind schon lange bekannt. Die mathematische Behandlung der Nichtlinearität erweist sich in den meisten Fällen als außerordentlich schwierig, deshalb versuchte man in der Vergangenheit, das wirkliche System zu "linearisieren". In den letzten Jahren sind beträchtliche Fortschritte im Verständnis der Dynamik nichtlinearer Systeme gemacht worden. Einen wesentlichen Beitrag zu diesem neuen Verständnis hat die moderne Rechentechnik geleistet.
Nichtlinearität ist notwendig, aber nicht hinreichend für das Auftreten von Chaos. Ob ein nichtlineares System chaotisches Verhalten zeigt, hängt auch von der Dimension seines Zustandsraumes ($>2$) und weitgehend von den Systemparametern und den Anfangsbedingungen ab.