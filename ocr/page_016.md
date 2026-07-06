## Page 44
Gilt global (d.h. $\forall q_i \in R^n$)
$$\frac{1}{\delta V} \frac{d \delta V}{dt} = \sum_{i=1}^n \frac{\partial F_i}{\partial q_i} < 0,$$
schrumpft also das Phasenvolumen stets, so heißt das System dissipativ. Wenn dagegen
$$\frac{1}{\delta V} \frac{d \delta V}{dt} = \sum_{i=1}^n \frac{\partial F_i}{\partial q_i} = 0$$
gilt, bleibt das Phasenvolumen also konstant, dann heißt das System konservativ oder auch Hamiltonsches System.

Wir berechnen, als Beispiel, diese relative Volumenänderung für unser getriebenes gedämpftes Pendel: die Zustandsvariablen sind $q_1 = \Omega, q_2 = \phi, q_3 = \omega_A$ und die Funktionen $F_i$ lauten:
$$F_1 = \Omega$$
$$F_2 = -\frac{b}{I} \Omega - \frac{mgl}{I} \sin \phi + \frac{A}{I} \cos(\phi)$$
$$F_3 = \omega_A$$
$$\frac{1}{\delta V} \frac{d \delta V}{dt} = \text{div} F = \frac{\partial F_1}{\partial \Omega