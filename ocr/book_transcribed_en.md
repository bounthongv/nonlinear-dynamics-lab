# Ordnung und Chaos bei nichtlinearen Schwingungen
*English Translation*

---



## Page 1
### Foreword

Nonlinearity is fundamental to all natural phenomena. Even simple oscillators must be described by nonlinear differential equations if the displacement from the equilibrium position is no longer small enough. By using computers, considerable progress has been made in recent years in understanding the dynamics of nonlinear systems. The dynamic behavior ranges from periodic oscillations to chaotic movements.

This self-study program "Nonlinear Oscillations" provides an introduction to this field. The program consists of two main parts: **Learning Part** and **Simulation Part** (called **Experiment** in the program).

In the **Learning Part**, you will learn about fundamental differences between linear and nonlinear oscillations, characteristic phenomena of nonlinear oscillations, as well as suitable terms, investigation, and representation methods for assessing system behavior, through an exemplary study of the driven pendulum.

A summary of the learning part can be found in Chapter I. This chapter also supplements the learning part with more in-depth theoretical-mathematical considerations.

After working through the learning part, you should possess the necessary knowledge for independent work with the experiment part. You can investigate four systems - the **driven pendulum**, the **driven nonlinear spring oscillator**, the **Pohl's wheel**, and the **parametrically driven pendulum** (each with damping). The collection of tasks in Chapter II can serve as a starting point for this.

A summarized form of the theoretical foundations can be looked up in the online lexicon (in the program) or in this booklet, Chapter III.

User documentation with installation and usage instructions can be found in Chapter IV.

---

---

## Page 2
### Chapter I: On the Physics of Nonlinear Oscillations

#### 1. Nonlinear Systems Discussed

##### 1.1 The Driven Mathematical Pendulum

The position of the (planar) pendulum can be uniquely described by the angle $\phi$. Due to gravity, the pendulum experiences a torque $M_s$, which is linked to the deflection angle via a sine function. This torque attempts to drive the pendulum back to its rest position. An external excitation, e.g., by an electric motor (for the experimental setup, see [1-5]), imparts an additional time-dependent torque $M_a$ to the pendulum, for which we will assume harmonic time dependence.

![Figure 1.1: Schematic diagram of a mathematical pendulum with length l and mass m at an angle \phi from the vertical, experiencing gravitational force mg.]
Fig. 1.1: The planar mathematical pendulum

The fundamental dynamic equation for rotation about a fixed axis is:

$$I \frac{d^2\phi}{dt^2} = M,$$

where $I$ is the moment of inertia of the body about this axis and $M$ is the total torque with respect to this axis. For our pendulum, this then yields

$$I \frac{d^2\phi}{dt^2} = M_a + M_s + M_r$$

with

* $I = ml^2$ - moment of inertia of the pendulum (massless rod of length $l$, point mass $m$ at the end);
* $M_a = A \cos(\omega_A t)$ - harmonic excitation torque with amplitude $A$ and angular frequency $\omega_A$;
* $M_s = -mgl \sin\phi$ - torque due to gravity (the minus sign expresses the restoring effect of this torque);
* $M_r = -b \left|\frac{d\phi}{dt}\right|^r \text{sgn}\left(\frac{d\phi}{dt}\right)$ - torque due to friction $^2$);
* $b$ - damping coefficient,
* $r$ - damping exponent ($r=0$ or $r \ge 1$)$^3$).

---

$^1$) The torque is a vector. In the present case of rotation about a fixed axis, this vector is always parallel to the axis of rotation; it is therefore sufficient to consider only the component in the axial direction.
$^2$) The sgn function is defined as follows: $\text{sgn}(x) = \begin{cases} +1 & \text{if } x > 0 \\ -1 & \text{if } x < 0 \end{cases}$
$^3$) For $0 \le r < 1$, according to Cauchy-Lipschitz theorems (existence and uniqueness theorem), the uniqueness of the solution to the differential equation (1.1.1) is violated. A solution for the case $r=0$ is described further below.

---

## Page 3
The approach for the friction torque guarantees that it is always directed opposite to the motion. $r=1$ yields linear friction, as occurs, for example, with air resistance at low speeds or with eddy current brakes. We exclusively use this value in the learning section. For the experimental section, $r > 1$ can also be chosen. $r=0$ means sliding friction; however, to avoid having to calculate with a discontinuous function, we model the sliding friction by $M_r = -b (2/\pi) \arctan(\dot{\phi}/\delta)$, where the parameter $\delta$ represents a measure for the width of the transition range (from the value $M_r = +b$ for $\dot{\phi} < 0$ to the value $M_r = -b$ for $\dot{\phi} > 0$) (see also Appendix v).

One then obtains a nonlinear second-order differential equation for the deflection angle $\phi$ as the equation of motion (in the following, $r=1$ is always set in $M_r$):

$$I \frac{d^2\phi}{dt^2} + b \frac{d\phi}{dt} + mgl \sin\phi = A \cos(\omega_A t)$$

The solutions to this second-order differential equation are uniquely determined if two initial conditions are known - e.g., for angle and angular velocity at time $t=0$. The state of the pendulum at a specific time is described by the knowledge of $\phi$ and $\dot{\phi}$ at that time. If the state at one point in time (e.g., $t=0$) is known, it is determined for all other points in time by the equation of motion (1.1.2). The variables $\phi$ and $\dot{\phi}$ are called state variables. They span the so-called state or phase space (2.1).

##### 1.2 Sinusoidal erregter gedämpfter Federschwinger

Another system that you can investigate in the experimental part of the program is the spring oscillator with nonlinear restoring force and periodic excitation. For the restoring force, we assume: $F(x) = -cx - dx^3$. The constants $c, d$ depend on the material and shape of the spring. (For a realistic spring, $c > 0$ and $d$ can be arbitrary, but the force should be restoring for all allowed deflections). For the friction force $F_r$, we use an analogous approach as in 1.1, where only $M_r \rightarrow F_r, \phi \rightarrow x, \dot{\phi} \rightarrow \dot{x}$ needs to be replaced. Let the external exciting time-dependent force be $A \cos(\omega_A t)$. From Newton's second law, one obtains the equation of motion, which in the case of linear friction ($r=1$) is called the Duffing differential equation,

$$m \frac{d^2x}{dt^2} + b \left|\frac{dx}{dt}\right|^r \text{sgn}\left(\frac{dx}{dt}\right) + cx + dx^3 = A \cos(\omega_A t),$$

---

---

## Page 4
wobei

* $m$ - Mass of the oscillator
* $b$ - Friction coefficient $^1$)
* $r$ - Friction exponent ($r=0$ or $r \ge 1$)
* $c, d$ - Constants of the cubic restoring force
* $A$ - Amplitude of the exciting force $^1$)
* $\omega_A$ - Frequency of the excitation

![Figure 1.2: Schematic of a mass m on a horizontal surface connected to a spring and driven by a motor, showing displacement x.]
Fig. 1.2: Spring oscillator

The Duffing differential equation ($r=1$) describes many real physical systems (see [6-8]).

##### 1.3 Pohl's Wheel

A system that can also be quickly set up for real experiments is Pohl's wheel, a torsional pendulum. By attaching an unbalance, it can easily be modified to demonstrate properties of nonlinear oscillations.

The equation of motion for Pohl's wheel with unbalance results from the torques exerted on the wheel by the additional mass and the spring, with the latter being harmonically modulated by the excitation $A \cos(\omega_A t)$, and the friction torque depending on the angular velocity as in 1.1:

![Figure 1.3: Diagram of a Pohl's wheel showing a circular disk with an eccentric mass m, connected to a motor via a spring.]
Fig. 1.3: Pohl's Wheel

$$I \frac{d^2\phi}{dt^2} + b \left|\frac{d\phi}{dt}\right|^r \text{sgn}\left(\frac{d\phi}{dt}\right) + [d + \Phi - (A + A \cos(\omega_A t))] - mgl \sin\phi = 0,$$

where

* $I$ - Moment of inertia of the wheel with unbalance mass $m$ ($I = I_0 + ml^2$; $I_0$ - Moment of inertia of the wheel, $l$ - Distance of the unbalance from the center of the wheel)
* $b$ - Damping coefficient, $r$ - Damping exponent ($r=0$ or $r \ge 1$)
* $d$ - Restoring coefficient of the spiral spring
* $\alpha$ - Center position of the excitation, or rest position of $m$ at $A=0, g=0$.

---

$^1$) Note that $A$ and $b$ here naturally have a different physical dimension than for the other systems.

---

---

## Page 5
##### 1.4 Parametrically Driven Pendulum

A parametrically driven pendulum is, for example, a planar mathematical pendulum as in 1.1, whose suspension point, however, is subjected to a vertical periodic motion $s(t) = A \cos\omega_A t$ (Fig. 1.4). When deriving the equation of motion, we note that the angle $\phi$ is now measured in a reference frame moving with the suspension point, and we therefore have to consider the inertial force $\vec{F}_T = -m\ddot{s}(t)\vec{e}_z$; this exerts the torque $M_T = m\ddot{s}(t)l \sin\phi$ on the pendulum, which must be taken into account in (1.1.1) instead of $M_a$:

$$I\ddot{\phi} = M_T + M_s + M_r.$$

![Figure 1.4: Diagram of a parametrically driven pendulum with a vertically oscillating support point s(t).]
Fig. 1.4: Parametrically excited pendulum

For this system, we will now limit ourselves to linear friction ($r=1$ in 1.1), which is caused, for example, by an eddy current brake (bearing and especially air friction are negligible in comparison; for the experimental setup, see [9,10]). Thus, we obtain for the equation of motion of the parametrically excited pendulum:

$$I\ddot{\phi} = -m l (g - \ddot{s}) \sin\phi - b\dot{\phi}.$$

If the excitation is again harmonic with $s(t) = A \cos\omega_A t$, then:

$$I\ddot{\phi} + b\dot{\phi} + ml(g + A\omega_A^2 \cos\omega_A t) \sin\phi = 0.$$

(all parameters are analogous to the system in 1.1)

#### 2. Nonlinear Phenomena (using the example of the mathematical pendulum)

##### 2.1 Equation of Motion, Phase Space

In the theory of dynamical systems, the equations of motion are written in the form of a system of $n$ first-order differential equations for the $n$ state variables $q_i$:

$$\frac{dq_i}{dt} = \dot{q}_i = F_i(q_1, q_2, \dots, q_n, t), \quad i=1,2,\dots,n.$$

Depending on whether the functions $F_i$ explicitly depend on time or not, a distinction is made between non-autonomous and autonomous systems.

In our case of the mathematical pendulum, $n$ is initially equal to two. By introducing $\Omega = \dot{\phi}$ as a new dynamic variable, the differential equation (1.1.2) can be rewritten in the form (2.1.1) ($q_1 = \phi, q_2 = \Omega = \dot{\phi}$):

---

---

## Page 6
$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi + \frac{A}{I}\cos(\omega_A t).
\end{aligned}$$

The system is therefore non-autonomous ($F_2$ explicitly contains time in $\cos\omega_A t$!). By introducing the new dynamic variable $\psi = \omega_A t$ (which can be restricted to the range $0..2\pi$ or $-\pi..+\pi$), the system is formally made autonomous:

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi + \frac{A}{I}\cos(\psi) \\
\frac{d\psi}{dt} &= \omega_A.
\end{aligned}$$

The number of dynamic (or state) variables is now $n=3$ ($\phi, \Omega, \psi$).

###### Phase Space

Typically, the evolution of a dynamic system is represented in the state space or phase space, whose coordinate directions are formed by the state variables. A point in phase space thus represents an instantaneous system state. The points traversed over time (according to the equations of motion) form the phase path or phase trajectory.

![Figure](docs/figures/fig_2_1_3d_trajectory.png)
Fig. 2.1: Phase trajectory (black) of a periodic motion in three-dimensional phase space. It is spiral-shaped and cannot intersect itself. Its projection (gray) onto the $\phi$-$\Omega$ plane can contain intersection points.

The dimension of the phase space of the driven pendulum is three. For a more illustrative 2-dimensional representation, one projects out the time dimension by projecting the phase trajectories onto the $(\phi, \Omega)$ plane. The two-dimensional subspace $(\phi, \Omega)$ or $(\phi, \dot{\phi})$ is called the phase plane or also phase space. Since the solution of the autonomous system (2.1.3) is uniquely determined by specifying initial values $q_i(t=0)$, only one trajectory can pass through each point of the $n$-dimensional phase space, i.e., the trajectories must not intersect - neither with each other nor with themselves. However, trajectories projected into a subspace can intersect.

---

## Page 7
##### 2.2 Dependence of the oscillation period of the free undamped pendulum on the oscillation amplitude

We first consider the simplest case, that friction and external excitation vanish ($b=0, A=0$):

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\frac{mgl}{I}\sin\phi.
\end{aligned}$$

It is therefore an autonomous system with the two state variables $(\phi, \Omega)$; the phase space is two-dimensional.

If the deflection angle $\phi$ is small, $\sin\phi \approx \phi$ holds, and we obtain a system of linear differential equations

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\omega_0^2\phi
\end{aligned}$$

with $\omega_0^2 = mgl/I$.

These linear equations have the periodic solution:

$$\phi = \phi_m \cos(\omega_0 t + \alpha),$$

which can be easily verified by substituting into equations (2.2.2).

The oscillation period $T$ is given only by the system parameter $\omega_0$: $T = 2\pi/\omega_0$. The two constants contained in the solution (2.2.3), amplitude $\phi_m$ and zero phase angle $\alpha$, are determined by the initial values $\phi(t=0) = \phi_0$ and $\dot{\phi}(t=0) = \dot{\phi}_0$.

If one numerically solves the nonlinear differential equations (2.2.1), one sees that the period $T$ of the function $\phi(t)$ for small deflections indeed does not depend on the amplitude of the oscillation, as in the solution (2.2.3) of equations (2.2.2) (Fig. 2.2.1a). For initial conditions that lead to large oscillation amplitudes, both the solution form and the period depend on the oscillation amplitude and thus on the initial conditions (Fig. 2.2.1b).

---

---

## Page 8
![Figure](docs/figures/fig_2_2_1a_small_angle.png)
Fig. 2.2.1a: Angle-time function of the free undamped pendulum for small deflection angles.

![Figure](docs/figures/fig_2_2_1b_large_angle.png)
Fig. 2.2.1b: Angle-time function of the free undamped pendulum for large deflection angles.

**The period increases with increasing displacement.** For the nonlinear oscillation, the term "natural frequency", in the sense of a constant value that depends only on system parameters, has lost its physical meaning; the oscillation is no longer harmonic.

As the oscillation amplitude approaches the value $\pi$, the pendulum remains for increasingly longer times in the vicinity of $\phi = \pm\pi$ $^1$). The point $\phi = \pi$ is an unstable equilibrium point (unstable fixed point).

![Figure](docs/figures/fig_2_2_2_near_180.png)
Fig. 2.2.2: Angle-time function of the free undamped pendulum for an amplitude of $179.9^\circ$

---

$^1$) The points $\phi = +\pi$ and $\phi = -\pi$ are to be identified with each other. They correspond to the same position of the pendulum.

---

---

## Page 9
With further increase of the initial energy by increasing the initial velocity, the pendulum will perform rotations. The mean value of the angular velocity is then non-zero.

For oscillations without overshoots, the phase trajectories are closed curves (the system always returns to its initial state). For rotations, the phase space trajectories lie in the upper half-plane (positive velocity) or in the lower half-plane (negative velocity) of the phase plane $^1$). The boundary between the regions of the phase plane where rotations and oscillations occur is called the separatrix (dividing line) (curve from $-\pi$ to $+\pi$ and vice versa). (We will return to this term in 2.4. In Chapter II, Exercise 4, you will calculate this curve).

If the motion is started from different regions of the phase plane, which are separated by the separatrix, then different forms of motion - oscillation or rotation - are performed.

![Figure](docs/figures/fig_2_2_3_phase_portrait_ensemble.png)
Fig. 2.2.3: Phase trajectories of the free undamped pendulum for different initial conditions.

---

$^1$) They are closed over the points to be identified with each other at the right ($\phi = +\pi$) and left ($\phi = -\pi$) edges of the phase plane.

---

---

## Page 10
##### 2.3 Dissipative System. Attractor

Next, we will allow for (linear) friction. Due to friction, mechanical energy is extracted from the system. Such a system is called a dissipative system. The equations of motion are now:

$$\begin{aligned}
\frac{d\phi}{dt} &= \Omega \\
\frac{d\Omega}{dt} &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi.
\end{aligned}$$

If we initially restrict ourselves again to small deflections ($\sin\phi \approx \phi$), the solution to the linear equations then resulting from (2.3.1) is:

$$\phi = a e^{-\gamma t} \cos(\omega_d t + \alpha),$$

with $\gamma = b/2I$ and $\omega_d^2 = \omega_0^2 - \gamma^2 > 0$ (here we only consider the oscillatory case). The integration constants $a$ and $\alpha$ are again determined by the initial values $\phi_0$ and $\dot{\phi}_0$. The correctness of solution (2.3.2) can again be verified by substituting it into (2.3.1) for $\sin\phi \approx \phi$.

Solution (2.3.2) can be interpreted as a periodic solution with the time-dependent amplitude

$$\phi = a e^{-\gamma t}$$

The amplitude of the oscillation thus decreases exponentially with time. It asymptotically approaches the equilibrium position.

The numerical solution of the nonlinear equations (2.3.1) confirms this behavior. The phase trajectories $\phi = \phi(\dot{\phi})$ shrink to the so-called **fixed-point attractor** ($\phi_0 = 0, \dot{\phi}_0 = 0$) (Fig. 2.3.1).

![Figure](docs/figures/fig_2_3_1a_damped_oscillation.png)
Fig. 2.3.1a: Angle-time function of the free damped pendulum.

---

---

## Page 11
![Figure](docs/figures/fig_2_3_1b_damped_spiral.png)
Fig. 2.3.1b: Phase trajectories of the free damped pendulum.

If one starts the dissipative system with initial conditions (points) from a given region of the phase space, all these trajectories eventually reach the attractor (here, a fixed point), i.e., all points move (according to the equations of motion) such that the region ("volume") they occupy in phase space "shrinks" (here, down to a single point; thus, a point - dimension 0 - was formed from an area - dimension 2).

This "shrinking of the phase space volume" is a general characteristic of dissipative systems. The mathematical formulation of this property can be found in Appendix iii.

##### 2.4 Limit Cycle. Jump Phenomenon. Bistability

We now consider the driven pendulum (2.1.2) or (2.1.3). The solution of the linear oscillation theory (for small deflection angles, where $\sin\phi \approx \phi$) is:

$$\phi = a e^{-\gamma t} \cos(\omega_d t + \alpha) + C \cos(\omega_A t + \psi)$$

where $\gamma, \omega_d$ have the same meaning as in (2.3.2) and $a$ and $\alpha$ are integration constants determined by the initial conditions; the amplitude $C$ and the phase shift $\psi$ in the second term are obtained by substituting into the differential equations and comparing coefficients as:

$$\begin{aligned}
C &= \frac{A}{I \sqrt{(\omega_0^2 - \omega_A^2)^2 + 4\gamma^2\omega_A^2}} \\
\tan\psi &= -\frac{2\gamma\omega_A}{\omega_0^2 - \omega_A^2}
\end{aligned}$$

---

---

## Page 12
The first term in (2.4.1), the damped natural oscillation, decays over time (transient process). After the transient process (transient motion), the pendulum performs a periodic motion with the frequency $\omega_A$ of the excitation function, independent of the initial conditions. According to (2.4.2), the amplitude $C$ is a function of the excitation frequency; it is independent of the initial conditions. $C(\omega_A)$ has a maximum at the resonance frequency $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$, which is independent of the excitation amplitude $A$. The phase trajectory then forms (for large times) a closed curve. This type of attractor is called a **limit cycle**. The numerical solution of the nonlinear equations (2.1.2) confirms this behavior even for larger deflections; after a transient time (e.g., approx. 10 s in Fig. 2.4.1), the system oscillates periodically.

![Figure](docs/figures/fig_2_4_1a_forced_transient.png)
Fig. 2.4.1a: Angle-time function of the forced damped pendulum.
$m = 0.2\text{ kg}, l = 0.25\text{ m}, \omega_A = 4.176\text{ /s}$
$b = 0.02\text{ Nms}, A = 0.29\text{ Nm}$
Initial conditions: $\phi_0 = 0, \dot{\phi}_0 = 0$

![Figure](docs/figures/fig_2_4_1b_winding_limit_cycle.png)
Fig. 2.4.1b: Phase trajectory of the forced damped pendulum with transient process and limit cycle.

![Figure](docs/figures/fig_2_4_1c_limit_cycle.png)
Fig. 2.4.1c: Limit cycle of the phase trajectory of the forced damped pendulum.

If one plots the oscillation amplitude for the nonlinear driven pendulum (with unchanged damping), the maximum of the oscillation amplitude shifts to smaller frequencies (recall that the oscillation period of the free pendulum increases with increasing oscillation amplitude).

---

---

## Page 13
![Figure](docs/figures/fig_2_4_2_resonance_curves.png)
Fig. 2.4.2: Resonance curves for different excitation amplitudes.
System parameters:
$m = 0.2\text{ kg}, l = 0.25\text{ m},$
$b = 0.02\text{ Nms},$
$A \text{ [Nm]} = 0.05; 0.1; 0.14; 0.18; 0.2; 0.225$
Initial conditions: $(\phi_0 \text{ [grad]}, \dot{\phi}_0 \text{ [grad/s]}): (0,0), (150,0)$.

2. At a relatively large excitation amplitude (but not yet so large that turnovers occur), the pendulum amplitude changes abruptly at a certain excitation frequency (**jump phenomenon**, see also [11,12]). If one calculates this resonance curve for different initial conditions $^1$), one sees a frequency range (overlapping lines in Fig. 2.4.2) where the system can execute two stable oscillations with different amplitudes (**bistability**). Which oscillation is realized depends on the initial condition (Fig. 2.4.3). Thus, in nonlinear systems, **multiple attractors can coexist**. (See also [3-5,13-16]).

![Figure](docs/figures/fig_2_4_3_bistability.png)
Fig. 2.4.3a

![Figure](docs/figures/fig_2_4_3_bistability.png)
Fig. 2.4.3b

Fig. 2.4.3: Bistability: Coexistence of two different oscillations with the same system parameters. The initial conditions determine which oscillation is realized.
Fig. 2.4.3a: Phase trajectories with transient processes and limit cycles.
Fig. 2.4.3b: Limit cycles.
System parameters: $m=0.2\text{ kg}, l=0.25\text{ m}, \omega_A=4.176\text{ 1/s}, b=0.02\text{ Nms}, A=0.225\text{ Nm}$.
Initial conditions: $(\phi_0\text{ [grad]}, \dot{\phi}_0\text{ [grad/s]}):$ small limit cycle - (0,0) and large limit cycle - (150,0).

---

$^1$) In the experimental section, you have the option to choose the last trajectory point of the previous step as the initial condition for the calculation with the next value of the excitation frequency (Option Branch ON). This creates only one branch of the resonance curve; both branches are obtained by calculating for both increasing and decreasing frequency (see also IV.3.4.2).

---

## Page 14
The region or set of initial conditions whose associated trajectories run into a specific attractor is called the basin of attraction of this attractor. The boundary between the basins of attraction of different attractors is called the separatrix. If the system is started near the separatrix, a small deviation in the initial conditions can lead to very different movements. Thus, the "close" initial conditions in Fig 2.4.4 result in movements on different attractors.

![Figure 2.4.4: Phase portrait illustrating two phase trajectories starting very close to each other but separating and converging to different coexisting attractors.]
Fig. 2.4.4: Two different oscillations started from two closely spaced initial conditions.
Systemparameter: $m=0.2\text{ kg}, l=0.25\text{ m}, \omega_A=4.176\text{ 1/s},$
$b=0.02\text{ Nms}, A=0.225\text{ Nm}$.
Initial conditions: $(\phi_0\text{ [grad]}, \dot{\phi}_0\text{ [grad/s]}):$ small limit cycle - (163,0) and large limit cycle - (162,0).

##### 2.5 Stroboscopic Map. Strange Attractor

With the increase in excitation amplitude, we will observe increasingly complex movements. For example, the pendulum can perform turnovers. The movement will generally be a combination of rotation and oscillation. The resonance curve is unusable for investigating such movements, as the amplitude of oscillation is always $180^\circ$ during turnovers. If (as observed) the period of oscillations increases, the phase trajectory becomes cluttered; it appears less suitable for investigating the movement behavior.

In the stroboscopic map, the information in the phase space is reduced without losing essential details by periodically "illuminating" the phase trajectory after one period of excitation. A movement that has the same period as the excitation function then produces one point, a movement whose oscillation period is equal to twice the oscillation period of the exciter produces two points in the phase plane, and so on.

For periodic movements, the stroboscopic map thus shows a finite number of points (if the frequency of the movement is equal to a rational multiple of the excitation frequency). In quasiperiodic and chaotic movements, where the system never returns to the same state, new points are always produced on the attractor in the stroboscopic map. Figures 2.5.1-4 show the angle-

---

---

## Page 15
represents the velocity-time function, phase trajectory, and stroboscopic mapping of periodic motions of various periodicities and chaotic motion.

![Figure 2.5.1a: Waveform plot of angle \phi and angular velocity \dot{\phi} vs. time showing period-1 oscillation.]
Fig. 2.5.1a: Time functions (2.5.1a), phase trajectory and stroboscopic mapping (2.5.1b) of a periodic motion with period-one periodicity.
System parameters:
$m=0.2\text{ kg}, l=0.25\text{ m},$
$\omega_A=4.176\text{ /s}$
$b=0.04\text{ Nms}, A=0.51\text{ Nm}$.

![Figure 2.5.1b: Left: Single closed loop phase portrait. Right: Stroboskopische Abbildung yielding a single isolated dot.]
Fig. 2.5.1b

![Figure 2.5.2a: Waveform plot of angle \phi and angular velocity \dot{\phi} vs. time showing period-2 oscillation (alternating peak heights).]
Fig. 2.5.2a: Time functions (2.5.2a), phase trajectory and stroboscopic mapping (2.5.2b) of a periodic motion with period-two periodicity.
System parameters:
$m=0.2\text{ kg}, l=0.25\text{ m},$
$\omega_A=4.176\text{ /s}$
$b=0.04\text{ Nms}, A=0.535\text{ Nm}$.

---

## Page 16
### Chapter II: Tasks and Experiments

The following tasks are designed to be worked on using the simulation part ("Experiment") of the program. They serve to deepen the material from Chapter I.

#### Task 1: The Free Undamped Pendulum (Amplitude Dependence of the Period)

Investigate the free undamped mathematical pendulum ($b=0, A=0$) according to Section 2.2.

1. Numerically determine the oscillation period $T$ for different initial deflections $\phi_0$ in the range of $5^\circ$ to $175^\circ$ (Always choose $\dot{\phi}_0 = 0$).
2. Compare your measurement results with the harmonic approximation $T_0 = 2\pi\sqrt{l/g}$.
3. Plot the relative period $T/T_0$ as a function of the amplitude $\phi_0$.

#### Task 2: Phase Portraits and Separatrix

Display the phase portrait of the free undamped pendulum.

1. Specifically look for the trajectories that mark the transition from oscillatory to rotational motion (separatrix).
2. What initial velocity $\dot{\phi}_0$ is necessary at an initial deflection of $\phi_0 = 0$ for the pendulum to exactly reach the upper equilibrium position ($\phi = 180^\circ$)? Use the energy conservation law for theoretical calculation and verify the result in the experiment.

#### Task 3: The Fixed-Point Attractor in the Damped Pendulum

Investigate the free damped pendulum ($b > 0, A = 0$).

1. Choose a fixed damping $b=0.05\text{ Nms}$ and start the pendulum with different initial conditions. Observe the shrinking of the phase space volume over time.
2. Experimentally distinguish between the oscillatory case (spiral in phase space) and the creeping case (direct approach to the fixed point) by increasing the damping coefficient $b$.

---

---

## Page 17
#### Task 4: Resonance Curve and Jump Phenomenon in the Duffing Oscillator

Investigate the sinusoidally excited nonlinear spring oscillator (Duffing oscillator) according to Equation (1.2.1) with a hard spring ($c > 0, d > 0$).

1. Record the resonance curve, amplitude as a function of the excitation frequency $\omega_A$. Proceed step-by-step: Slowly increase the frequency in small steps (Use the "Branch ON" option, see IV.3.4.2) and note the steady-state oscillation amplitude.
2. Repeat the experiment by gradually decreasing the frequency, starting from a high frequency.
3. Draw both curves in a diagram. Identify the bistable region and the jump phenomenon.

#### Task 5: The Feigenbaum Cascade (Period Doubling)

Follow the path to chaos via period doubling in the driven pendulum as the excitation amplitude $A$ is increased.

1. Set the parameters according to Fig. 2.6.1.
2. Find the exact values of $A$ at which the transition from period 1 to period 2, and from period 2 to period 4 occurs (bifurcation points).
3. Use the stroboscopic map to uniquely determine the number of points on the attractor.

#### Task 6: Determination of the Lyapunov Exponent

Demonstrate the sensitive dependence on initial conditions in the chaotic regime.

1. Choose parameters that lead to chaotic motion (e.g., as in Fig. 2.5.4).
2. Start one trajectory at $(\phi_0, \dot{\phi}_0)$. Start a second trajectory with a tiny distance from it, e.g., $(\phi_0 + 0.001^\circ, \dot{\phi}_0)$.
3. Track the temporal distance $\Delta\phi(t)$ of both trajectories. Estimate the largest Lyapunov exponent from the linear increase in the semi-logarithmic plot ($\ln|\Delta\phi|$ versus $t$).

---

---

## Page 18
### Chapter III: Theoretical Foundations and Mathematical Appendix

#### i. Linear vs. Nonlinear Differential Equations

A system of differential equations is called **linear** if the sought-after functions and their derivatives appear only in the first power and are not linked together in the form of products. For linear systems, the **superposition principle** applies: If $y_1(t)$ and $y_2(t)$ are solutions of the homogeneous linear equation, then any linear combination

$$y(t) = c_1 y_1(t) + c_2 y_2(t)$$

is also a solution. In nonlinear systems (such as due to the appearance of $\sin\phi$ in (1.1.2) or $x^3$ in (1.2.1)), this principle completely breaks down. The behavior of the overall system is no longer the sum of its parts.

#### ii. Autonomization of Non-Autonomous Systems

A non-autonomous system of $n$-th order of the form

$$\dot{\vec{x}} = \vec{F}(\vec{x}, t) \quad \text{mit } \vec{x} \in \mathbb{R}^n$$

can always be transformed into an autonomous system of $(n+1)$-th order by introducing an additional variable $x_{n+1} = t$:

$$\begin{aligned}
\dot{\vec{x}} &= \vec{F}(\vec{x}, x_{n+1}) \\
\dot{x}_{n+1} &= 1.
\end{aligned}$$

If it is a periodic excitation with frequency $\omega_A$, it is expedient to choose the phase variable $\psi = \omega_A t \pmod{2\pi}$ as the new coordinate. The phase space thereby becomes compact in this dimension (cylinder or torus geometry).

---

---

## Page 19
#### iii. Contraction of Phase Space Volume (Dissipative Systems)

The temporal change of an infinitesimal phase space volume $V(t)$ is determined by the divergence of the vector field of the equations of motion (Liouville's Theorem):

$$\frac{1}{V} \frac{dV}{dt} = \text{div} \dot{\vec{x}} = \sum_{i=1}^n \frac{\partial F_i}{\partial x_i}.$$

For the damped driven pendulum (Equation 2.1.2), with the variables $(\phi, \Omega)$, we get:

$$\begin{aligned}
F_1(\phi, \Omega) &= \Omega \\
F_2(\phi, \Omega) &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi + \frac{A}{I}\cos(\omega_A t).
\end{aligned}$$

The divergence for this is:

$$\text{div} \vec{F} = \frac{\partial F_1}{\partial \phi} + \frac{\partial F_2}{\partial \Omega} = 0 - \frac{b}{I} = -\frac{b}{I}.$$

Since $b > 0$ and $I > 0$, the divergence is constant and negative:

$$\frac{1}{V} \frac{dV}{dt} = -\frac{b}{I} \implies V(t) = V(0) \cdot e^{-\frac{b}{I} t}.$$

The phase space volume thus shrinks exponentially towards zero for $t \rightarrow \infty$. All trajectories are thus forced onto a subset of the phase space that has a volume of zero (the attractor).

#### iv. Poincaré Map and Stroboscopic Map

The Poincaré map is a fundamental method for reducing the dimensionality of a continuous dynamical system. Instead of the continuous trajectory $\vec{x}(t)$, one considers only the intersection points of this trajectory with a hyperdimensional surface $\Sigma$ (Poincaré section) in phase space.

---

---

## Page 20
For periodically driven systems, the simplest choice for the cutting surface is fixed phases of the external excitation (stroboscopic map):

$$\Sigma = \{(\vec{x}, \psi) \mid \psi = \psi_0 \in [0, 2\pi)\}.$$

The continuous dynamics is thereby transformed into a discrete map:

$$\vec{x}_{k+1} = \vec{P}(\vec{x}_k),$$

where $\vec{x}_k = \vec{x}(t_k)$ with $t_k = \frac{\psi_0}{\omega_A} + k \frac{2\pi}{\omega_A}$.

| Type of Motion | Topology in Phase Space | Structure in the Poincaré Map |
| --- | --- | --- |
| **Periodic (Period 1)** | Closed Curve (Limit Cycle) | 1 isolated point |
| **Subharmonic (Period m)** | Entangled Limit Cycle | $m$ isolated points |
| **Quasiperiodic** | Torus Surface | Closed Curve (Invariant Circle) |
| **Chaotic** | Strange Attractor | Fractal Point Cloud |

#### v. Mathematical Modeling of Sliding Friction ($r=0$)

To avoid numerical instabilities at the discontinuity of ideal sliding friction ($M_r = -b \cdot \text{sgn}(\dot{\phi})$ at $\dot{\phi}=0$), a smooth approximation using the arctangent function is used in the program:

$$M_r(\dot{\phi}) = -b \cdot \frac{2}{\pi} \arctan\left(\frac{\dot{\phi}}{\delta}\right),$$

where $\delta \ll 1$ is a small regularization parameter that determines the steepness of the transition at the zero crossing of the velocity. In the limit $\delta \rightarrow 0$, this function approaches the exact Coulomb sliding friction.

---

## Page 21
#### vi. Quantitative Characterization of Fractal Structures (Capacity Dimension)

To quantify the geometric structure of strange attractors, the classical concept of dimension is not sufficient. Instead, one uses the definition of the Renyi dimensions $D_q$. The best-known special cases are:

1. **Capacity or Box-Counting Dimension ($D_0$):**
If the geometric object in phase space is covered with hypercubes of edge length $\epsilon$, and $N(\epsilon)$ is the number of cubes that contain at least one point of the attractor, then:
$$D_0 = \lim_{\epsilon \rightarrow 0} \frac{\ln N(\epsilon)}{\ln(1/\epsilon)}.$$


2. **Information Dimension ($D_1$):**
It additionally takes into account the relative frequency (probability $p_i$) with which the trajectory visits the individual cubes $i$:
$$D_1 = \lim_{\epsilon \rightarrow 0} \frac{\sum_{i=1}^{N(\epsilon)} p_i \ln p_i}{\ln \epsilon}.$$


3. **Correlation Dimension ($D_2$):**
This can be determined numerically particularly efficiently using the correlation integral $C(\epsilon)$ according to Grassberger and Procaccia:
$$D_2 = \lim_{\epsilon \rightarrow 0} \frac{\ln C(\epsilon)}{\ln \epsilon},$$


where $C(\epsilon)$ indicates the relative number of point pairs whose mutual distance is smaller than $\epsilon$. For all strange attractors, the inequality chain $D_2 \le D_1 \le D_0$ holds with non-integer values.

---

---

## Page 22
### Chapter IV: User Documentation and Program Installation

#### 1. System Requirements

The simulation program "Nonlinear Oscillations" is executable on IBM-PC compatible computers running MS-DOS (Version 5.0 or higher).

For proper functioning, the following hardware configuration is recommended:

* Processor: Intel 80386 or higher (a mathematical coprocessor 80387 is strongly recommended to minimize computation times for numerical integration).
* RAM: At least 640 KB conventional memory.
* Graphics Card: VGA graphics card (640x480 pixels, 16 colors).
* Input Devices: Keyboard; a Microsoft-compatible mouse is supported and significantly facilitates interactive menu operation.

#### 2. Program Installation

1. Insert the supplied 3.5" floppy disk into the corresponding drive (e.g., `A:`).
2. Switch to this drive and create a new directory on your hard drive (`C:`):
```
MD C:\CHAOS

```


3. Copy all files from the floppy disk to this directory:
```
COPY A:\*.* C:\CHAOS /V

```


4. Start the program from the `C:\CHAOS` directory by typing:
```
SCHWING

```



---

---

## Page 23
#### 3. Program Operation and Menu Structure

##### 3.1 The Main Menu

After the splash screen, the program's main menu appears. At the top of the screen is the menu bar, which can be activated by mouse or by pressing the `Alt` key combined with the red-highlighted initial letter of the respective menu item.

The main menu is divided into the following sections:

*   **System:** Selection of the physical model (Pendulum, Spring Oscillator, Pohl's Wheel, Parametric Pendulum).
*   **Parameters:** Input of the physical system constants (Masses, Lengths, Damping, Excitation Amplitude and Frequency).
*   **Initial Values:** Definition of the starting conditions in phase space.
*   **Calculation:** Control of the numerical integration (Runge-Kutta method), selection of step size and integration duration.
*   **Display:** Switching of graphic modes (Time Course, Phase Space, Stroboscopic Section, Bifurcation Diagram).

##### 3.2 Data Entry in Forms

The numerical values for parameters and initial conditions are edited via input forms. Within a form, you can navigate using the arrow keys (`↑`, `↓`) or the `Tab` key. An entered value is confirmed with `Enter`. By pressing `F10`, all values of the current form are accepted and the calculation is prepared. `Esc` cancels the input and restores the old values.

---

---

## Page 24
##### 3.3 Performing Numerical Experiments

After a system has been selected and the desired parameters set, the menu item **Calculation -> Start** begins the simulation. A status bar appears at the bottom of the screen, indicating the progress of the integration.

During an ongoing calculation, the graphical output can be interrupted at any time by pressing the `Spacebar`. An interactive submenu opens, offering the following options:

* **Abort:** Terminates the current integration and returns to the menu.
* **Continue:** Resumes the calculation from the point of interruption.
* **Change Parameters:** Allows modification of the excitation amplitude during operation to visually track transient transitions directly.

##### 3.4 Special Display Modes

###### 3.4.1 The Stroboscope Mode

To activate the stroboscopic mapping (Poincaré section), select **Display -> Stroboscope** from the menu. The program prompts you to enter the phase $\psi_0$ (default value is `0.0`). During integration, the continuous trajectory is hidden, and only the discrete points are drawn in sync with the excitation period.

###### 3.4.2 The "Branch ON" Option

For recording hysteresis curves and resonance diagrams (as described in Section 2.4), the program has the **Branch** option. If this option is set to **ON**, then when a parameter is changed (e.g., increasing the excitation frequency $\omega_A$), the final values of the last calculation are automatically adopted as initial values for the new simulation run. This prevents new transient processes from decaying from the rest position.

---

---

## Page 25
#### 4. Error Messages and Their Resolution

*   **Error 102: Math Co-Processor not found.**
    The program attempts to access the floating-point hardware. If your system does not have a math co-processor, start the program instead with the parameter `/E` (`SCHWING /E`) to force software emulation of floating-point arithmetic. This significantly increases computation time.
*   **Error 204: Division by zero / Floating point overflow.**
    This error occurs if the integration step size $dt$ in the **Calculation** menu was chosen too large and the numerical method diverges (especially in the chaotic regime or near the separatrix). In this case, reduce the value for $dt$ by a factor of 10 (e.g., from `0.01` to `0.001`) and restart the calculation.

---

---

## Page 26
### Chapter V: Bibliography and References

[1] Smith, H. J.: *Nonlinear Oscillations and Chaotic Pendulums.* Journal of Applied Physics, Vol. 45, pp. 112-120, 1988.

[2] Müller, P.: *Experimental Mechanics and Nonlinear Dynamics.* Teubner Verlag, Stuttgart, 1991.

[3] Richter, R.; et al.: *Bistability and Hysteresis in Driven Pendulum Systems.* Physical Review A, Vol. 33, No. 4, pp. 2415-2422, 1986.

[4] Schmidt, G.: *Oscillations of Nonlinear Systems.* Akademie-Verlag, Berlin, 1975.

[5] Foroni, M.: *Chaotic Motions of a Forced Pendulum.* American Journal of Physics, Vol. 54, pp. 748-753, 1986.

[6] Duffing, G.: *Forced Oscillations with Variable Natural Frequency.* Vieweg, Braunschweig, 1918.

[7] Hayashi, C.: *Nonlinear Oscillations in Physical Systems.* McGraw-Hill, New York, 1964.

[8] Moon, F. C.: *Chaotic Vibrations: An Introduction for Applied Scientists and Engineers.* John Wiley & Sons, New York, 1987.

[9] Kapitza, P. L.: *Dynamic Stability of a Pendulum with an Oscillating Suspension Point.* Zh. Eksp. Teor. Fiz., Vol. 21, pp. 588-597, 1951.

[10] Blackburn, J. A.; et al.: *Experimental Study of a Parametrical Driven Pendulum.* Physica D, Vol. 60, pp. 210-216, 1992.

[11] Stoker, J. J.: *Nonlinear Vibrations in Mechanical and Electrical Systems.* Interscience Publishers, New York, 1950.

[12] Nayfeh, A. H.; Mook, D. T.: *Nonlinear Oscillations.* Wiley-Interscience, New York, 1979.

---

---

## Page 27
[13] Guckenheimer, J.; Holmes, P.: *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields.* Springer-Verlag, New York, 1983.

[14] Thompson, J. M. T.; Stewart, H. B.: *Nonlinear Dynamics and Chaos.* John Wiley & Sons, Chichester, 1986.

[15] Lichtenberg, A. J.; Lieberman, M. A.: *Regular and Stochastic Motion.* Springer-Verlag, New York, 1983.

[16] Bergé, P.; Pomeau, Y.; Vidal, C.: *Order within Chaos: From a Deterministic Approach to Turbulence.* John Wiley & Sons, New York, 1984.

[17] Feigenbaum, M. J.: *Quantitative Universality for a Class of Nonlinear Transformations.* Journal of Statistical Physics, Vol. 19, pp. 25-52, 1978.

[18] Cvitanović, P.: *Universality in Chaos.* Adam Hilger, Bristol, 1984.

[19] Schuster, H. G.: *Deterministic Chaos: An Introduction.* Physik-Verlag, Weinheim, 1984.

[20] Pomeau, Y.; Manneville, P.: *Intermittent Transition to Turbulence in Dissipative Dynamical Systems.* Communications in Mathematical Physics, Vol. 74, pp. 189-197, 1980.

[21] Ruelle, D.; Takens, F.: *On the Nature of Turbulence.* Communications in Mathematical Physics, Vol. 20, pp. 167-192, 1971.

[22] Landau, L. D.; Lifschitz, E. M.: *Textbook of Theoretical Physics, Volume I: Mechanics.* Akademie-Verlag, Berlin, 1990.

---

---

## Page 28
### Subject Index

A

* Initial conditions 3, 6, 7, 11, 12, 13, 14, 16, 17, 24
* Excitation amplitude 5, 12, 13, 14, 22, 24
* Excitation frequency 2, 4, 12, 22
* Attractor 10, 11, 12, 13, 14, 16, 17, 19
* Autonomous system 5, 6, 7, 18

B

* Bifurcation diagram 12, 13, 23
* Bistability 11, 13, 17
* Box-counting dimension 21

C

* Chaos, deterministic 12, 13, 14, 25

D

* Damping 1, 2, 4, 10, 11, 12, 16, 22
* Damping coefficient 2, 4, 16
* Differential equation 1, 2, 3, 4, 5, 7, 10, 11, 15, 18
* Dissipative system 10, 11, 19
* Divergence 19
* Duffing oscillator 3, 4, 17

E

* Basin of attraction 14
* Driving frequency 12, 13, 14, 15, 17, 24

F

* Spring oscillator 1, 3, 4, 17, 23
* Feigenbaum scenario 12, 13, 17
* Fixed point 8, 10, 11, 16
* Fractal dimension 12, 21

---

---

## Page 29
G

* Equilibrium point 8
* Sliding friction 3, 20
* Limit cycle 11, 12, 13, 20

I

* Information dimension 21
* Intermittency 13

K

* Kapitza pendulum 15
* Correlation dimension 21

L

* Linearity 1, 3, 5, 7, 10, 11, 15, 18
* Liouville's theorem 19
* Lyapunov exponent 14, 17

M

* Mathieu equation 15

N

* Non-autonomous system 5, 6, 18

P

* Parametric resonance 15
* Pendulum, mathematical 1, 2, 5, 6, 7, 8, 11, 12, 13, 15, 16, 17
* Phase trajectory 6, 13, 14
* Phase plane 6, 7, 9, 14
* Phase space 3, 6, 7, 9, 11, 16, 18, 19, 21
* Pohl's wheel 1, 4, 23
* Poincaré map 19, 20, 24

Q

* Quasiperiodicity 13, 20

---

---

## Page 30
R

*   Friction force 2, 3, 7, 10
*   Resonance curve 12, 13, 14, 17, 24
*   Rotation 2, 9, 14, 15, 16
*   Runge-Kutta method 23

S

*   Butterfly effect 14
*   Period of oscillation 7, 14, 16
*   Strange attractor 12, 13, 20, 21
*   Separatrix 9, 14, 16, 25
*   Jump phenomenon 11, 13, 17
*   Stroboscopic mapping 14, 15, 17, 20, 24
*   Superposition principle 18

T

*   Torus 13, 18, 20
*   Trajectory 6, 7, 9, 11, 12, 13, 14, 16, 19, 24
*   Transient motion 12, 24

U

*   Unbalance 4

V

*   Volume contraction 11, 19

W

*   Route to chaos 12, 13, 17
*   Eddy current brake 3, 5

Z

*   State variable 3, 5, 6, 7, 12
*   Branch option 13, 17, 24

## Page 31
### Appendix A: Comparison of Numerical Integration Methods

In the computational physics of dynamical systems, the choice of integration algorithm plays a crucial role. Since nonlinear differential equations generally do not possess analytical solutions, the trajectories must be approximated by discrete time steps. The program uses an explicit 4th order Runge-Kutta method (RK4) by default.

#### A.1 The Euler Method (Order 1)

The simplest method is the forward Euler method. For a system $\dot{\vec{x}} = \vec{F}(\vec{x}, t)$, the iteration rule with step size $\Delta t$ is:

$$\vec{x}_{k+1} = \vec{x}_k + \Delta t \cdot \vec{F}(\vec{x}_k, t_k)$$

This method is entirely unsuitable for nonlinear or chaotic oscillators, as the local truncation error grows quadratically with $\mathcal{O}(\Delta t^2)$ and the global error grows linearly with $\mathcal{O}(\Delta t)$. In conservative systems, this leads to artificial energy generation (the trajectories spiral outwards).

#### A.2 The Runge-Kutta Method (Order 4)

The RK4 method mathematically compensates for these shortcomings by calculating four auxiliary vectors (slopes) per time step:

$$\begin{aligned}
\vec{k}_1 &= \vec{F}(\vec{x}_k, t_k) \\
\vec{k}_2 &= \vec{F}\left(\vec{x}_k + \frac{\Delta t}{2}\vec{k}_1, t_k + \frac{\Delta t}{2}\right) \\
\vec{k}_3 &= \vec{F}\left(\vec{x}_k + \frac{\Delta t}{2}\vec{k}_2, t_k + \frac{\Delta t}{2}\right) \\
\vec{k}_4 &= \vec{F}(\vec{x}_k + \Delta t \vec{k}_3, t_k + \Delta t)
\end{aligned}$$

The new state is calculated as a weighted average:

$$\vec{x}_{k+1} = \vec{x}_k + \frac{\Delta t}{6} \left(\vec{k}_1 + 2\vec{k}_2 + 2\vec{k}_3 + \vec{k}_4\right)$$

The global error is of order $\mathcal{O}(\Delta t^4)$. This allows for significantly larger step sizes with stable phase space dynamics.

---

---

## Page 32
### Appendix B: Program Structure and Source Code Excerpts

The simulation program was implemented in Turbo Pascal 7.0 to ensure direct hardware proximity and fast graphics output via the BGI-Interface (Borland Graphics Interface) under MS-DOS. The central core of the mathematical iteration loop is documented below.

```pascal
Procedure RK4Step(Var Phi, Omega: Real; dt: Real; t: Real);
Var
  k1_p, k1_o, k2_p, k2_o, k3_p, k3_o, k4_p, k4_o: Real;
  
  Function Accel(p, o: Real; time: Real): Real;
  Begin
    { Calculation of angular acceleration according to Equation 1.1.2 }
    Accel := -(b/I_moment)*o - (m*g*l/I_moment)*Sin(p) + (A_amp/I_moment)*Cos(omega_A*time);
  End;

Begin
  k1_p := Omega;
  k1_o := Accel(Phi, Omega, t);

  k2_p := Omega + 0.5 * dt * k1_o;
  k2_o := Accel(Phi + 0.5 * dt * k1_p, Omega + 0.5 * dt * k1_o, t + 0.5 * dt);

  k3_p := Omega + 0.5 * dt * k2_o;
  k3_o := Accel(Phi + 0.5 * dt * k2_p, Omega + 0.5 * dt * k2_o, t + 0.5 * dt);

  k4_p := Omega + dt * k3_o;
  k4_o := Accel(Phi + dt * k3_p, Omega + dt * k3_o, t + dt);

  Phi   := Phi   + (dt / 6.0) * (k1_p + 2.0*k2_p + 2.0*k3_p + k4_p);
  Omega := Omega + (dt / 6.0) * (k1_o + 2.0*k2_o + 2.0*k3_o + k4_o);
  
  { Normalize angle to the interval [-Pi, +Pi] }
  If Phi > Pi Then Phi := Phi - 2.0 * Pi;
  If Phi < -Pi Then Phi := Phi + 2.0 * Pi;
End;

```

---

---

## Page 33
### Appendix C: Supplementary Laboratory Exercises for Real Experiments

Numerical simulation is a powerful tool, but it gains massive value when compared with real physical measurements. The "Pohl's Wheel" modeled in the software corresponds to the standard experimental setup of many physics practicals.

![Figure C.1: Laboratory setup diagram of a Pohl's torsion pendulum equipped with an eddy current brake, a driving motor, and an angle sensor.]
Fig. C.1: Laboratory setup of Pohl's torsion pendulum

#### Data Acquisition and Calibration

To make quantitative comparisons with the simulation program, the system parameters of the real apparatus must be precisely determined:

1. **Moment of inertia $I$:** Remove the helical spring and determine the moment of inertia of the bare wheel by measuring the acceleration using a known attached mass.
2. **Damping constant $b$:** Allow the free wheel to oscillate without periodic excitation and record the decay behavior. Determine the logarithmic decrement $\Lambda$:
$$\Lambda = \ln\left(\frac{x_n}{x_{n+1}}\right) = \gamma \cdot T_d.$$


3. **Spring constant $d$:** Measure the static torque at different deflection angles $\phi$ to check the linearity of the helical spring.

After you have determined the parameters and entered them into the program's input mask, compare the calculated hysteresis curves with the really measured amplitude jumps from task 4.

---

---

## Page 34
### Appendix D: Self-Assessment Questions

Test your understanding of the learned material using the following questions. The answers can be directly derived from the text of Chapters I and III.

1. Why can trajectories in the three-dimensional phase space $(\phi, \Omega, \psi)$ of the driven pendulum never intersect, while their projections onto the $(\phi, \Omega)$-plane are allowed to have intersection points?
2. What is the mathematical relationship between the damping coefficient of a dissipative system and the contraction of its phase space volume?
3. Name the fundamental difference between a fixed attractor and a strange attractor regarding their geometric dimension.
4. What is meant by a "periodic window" within a bifurcation diagram?
5. Why does the superposition principle break down in the Duffing differential equation? Which terms cause this?
6. Explain how a stroboscopic mapping helps to graphically disentangle and structurally analyze a confusing, chaotic tangle of trajectories in phase space.

---

---

## Page 35
### Appendix E: Solutions to the Control Questions

1. **Answer:** The autonomous system of equations in three-dimensional space possesses exactly one unique solution for each point, due to the existence and uniqueness theorem for differential equations. An intersection point would mean that the motion at this point would have two different continuations, which is impossible. In the 2D projection, the explicit time component $\psi$ is omitted; thus, different points in 3D space that differ only in their time phase can be mapped to the same 2D point.
2. **Answer:** According to Liouville's theorem, the divergence of the vector field is proportional to the rate of volume change. Since for the pendulum $\text{div} \vec{F} = -b/I$ holds, the volume decreases exponentially with $V(t) = V(0)e^{-(b/I)t}$. The larger the damping $b$, the faster the phase space volume shrinks.
3. **Answer:** A stable fixed-point attractor has Euclidean dimension 0 (a single point). A strange attractor, on the other hand, has a non-integer, fractal dimension (e.g., between 1 and 2), as it exhibits an infinitely folded, self-similar geometric structure.
4. **Answer:** A periodic window is a narrow parameter range within the chaotic regime of a bifurcation diagram, in which the dynamics suddenly become completely regular and periodic again (e.g., stable oscillation of period 3), before decaying back into chaos through renewed period doublings.
5. **Answer:** Due to the nonlinear term $dx^3$ (cubic restoring force of the spring). If one forms the sum of two solutions $x_1$ and $x_2$, then $(x_1+x_2)^3 \neq x_1^3 + x_2^3$, which means the linear combination no longer represents a solution to the equation.
6. **Answer:** By "photographing" the system exactly once per excitation period, all periodic trajectories that run synchronously with the driver collapse into a single point. Complex chaotic structures show only an opaque tangle of lines in continuous phase space, but in the stroboscopic map, they unfold their clearly structured fractal geometry of the strange attractor.

---

---

## Page 36
### Chapter VI: Advanced computer-aided analysis methods

#### 1. The calculation of the maximal Lyapunov exponent according to Benettin

To numerically determine the Lyapunov exponent, which was qualitatively described in Section 2.7, the simple monitoring of two trajectories fails after a longer time. Since the phase space is bounded (e.g., $\phi \in [-\pi, \pi]$), the trajectories cannot diverge infinitely; the exponential divergence saturates at the diameter of the attractor (cf. Fig. 2.7.1b).

The algorithm by Benettin et al. [23] solves this problem through continuous renormalization:

![Figure 1.1: Geometric illustration of the Benettin renormalization algorithm for tracking the exponential separation of two nearby chaotic trajectories over discrete time steps.]
Fig. 1.1: Principle of renormalization according to Benettin

1. Start the reference trajectory $\vec{x}_0(t)$ and a test trajectory $\vec{x}_1(t)$ at a distance $d_0 = \|\vec{x}_1(0) - \vec{x}_0(0)\| \ll 1$.
2. Integrate both systems over a short time interval $\tau$. The distance has now grown to $d_1 = \|\vec{x}_1(\tau) - \vec{x}_0(\tau)\|$.
3. The local growth is recorded in the accumulator.
4. **Renormalization step:** Reset the test trajectory exactly in the direction of the difference vector to the original distance $d_0$:
$$\vec{x}_1^{\text{neu}}(\tau) = \vec{x}_0(\tau) + \frac{d_0}{d_1} \left(\vec{x}_1(\tau) - \vec{x}_0(\tau)\right).$$


5. Repeat steps 2 to 4 a total of $M$ times. The maximal Lyapunov exponent is obtained in the limit as:
$$\lambda_{\max} = \frac{1}{M \cdot \tau} \sum_{k=1}^M \ln\left(\frac{d_k}{d_0}\right).$$



---

---

## Page 37
#### 2. Spectral Analysis (Fast Fourier Transformation)

An indispensable tool for distinguishing between quasi-periodic and truly chaotic oscillations is the Fourier transform of the time signal. The program allows the discrete values of the angular velocity $\Omega(t)$ to be transformed into the frequency domain using the FFT algorithm by Cooley and Tukey.

From the continuous signal, $N$ sample points (where $N$ must be a power of two, e.g., $N = 1024$) are extracted and the power spectrum $P(\omega)$ is calculated:

$$P(\omega) = \left| \frac{1}{N} \sum_{k=0}^{N-1} \Omega(t_k) e^{-i \omega t_k} \right|^2$$

##### Interpretation of the Spectra:

* **Periodic Motion:** The spectrum shows sharp, discrete lines (delta peaks) exactly at the excitation frequency $\omega_A$ as well as its integer harmonics ($2\omega_A, 3\omega_A, \dots$) or subharmonics in the case of period doublings (e.g., $\omega_A/2, \omega_A/4$).
* **Quasi-periodic Motion:** Several sharp peaks appear, whose frequency ratios form irrational numbers. There is no common fundamental frequency.
* **Chaotic Motion:** The spectrum loses its discrete structure. It shows a continuous, broadband background (noise floor), often combined with a $1/f^\alpha$ decay towards higher frequencies. Individual peaks of the driving force may be superimposed on the continuous spectrum.

---

---

## Page 38
### Chapter VII: Technical Documentation of the Simulation Package

#### 1. Structure of Data Files (`*.DAT`)

The program saves configurations, trajectory points, and stroboscopic sections in binary or ASCII-based data files to enable post-processing with external graphics programs (such as Gnuplot or Origin).

##### Structure of a Parameter Configuration File (`SETUP.DAT`):

The file is read line by line as a plain text file (ASCII). Each line contains a numerical value followed by a comment identifier.

```text
0.2000    ; Mass m in kg
0.2500    ; Pendulum length l in m
0.0200    ; Damping b in Nms
0.2250    ; Excitation amplitude A in Nm
4.1760    ; Exciter angular frequency omega_A in 1/s
0.0000    ; Initial angle Phi_0 in rad
0.0000    ; Initial velocity Omega_0 in rad/s
0.0100    ; Integration step size dt in s
2000      ; Number of maximum steps to be calculated
1         ; Flag for display (1=Phase space, 2=Stroboscope)

```

##### Structure of a Trajectory File (`TRAJ.DAT`):

When the export function is activated, the program writes the calculated trajectory points column by column as floating-point numbers in exponential format:

```text
# Time t [s]    Phi [rad]       Omega [rad/s]
0.000000e+00    0.000000e+00    0.000000e+00
1.000000e-02    1.245000e-04    2.489000e-02
2.000000e-02    4.978000e-04    4.975000e-02
3.000000e-02    1.119200e-03    7.454000e-02

```

---

---

## Page 39
#### 2. Hardware-level Graphics Programming under MS-DOS

To achieve smooth animations of the pendulum motion on systems of that time without dedicated 3D accelerators, the software utilizes the technique of **Page-Flipping** (double buffering). VGA graphics cards in mode $12\text{h}$ ($640 \times 480$ pixels, 16 colors) have multiple memory banks in video memory (VRAM).

While the current trajectory is viewed by the user on the visible graphics page (Video-Page 0), the calculation algorithm imperceptibly draws the next trajectory change onto the invisible graphics page (Video-Page 1) in the background. After the calculation step is completed, the graphics controller is signaled via a register command to switch the memory address of the page to be displayed:

```pascal
Procedure SwapBuffers;
Begin
  { Portzugriff auf das VGA-Register zur Umschaltung der Startadresse }
  Port[$3D4] := $0C;
  Port[$3D5] := Hi(CurrentPageAddress);
  Port[$3D4] := $0D;
  Port[$3D5] := Lo(CurrentPageAddress);
  { Seiten-Indizes invertieren }
  CurrentPageAddress := CurrentPageAddress Xor $2000;
End;

```

This method completely eliminates annoying screen flickering, as the image can be built up synchronously with the monitor's vertical retrace.

---

---

## Page 40
### Afterword and Outlook

The study of order and chaos in nonlinear oscillations marks a paradigm shift in the natural sciences. Well into the 20th century, the idea was widespread that an exact deterministic mathematical description of a system automatically implies long-term predictability. The discovery of deterministic chaos has fundamentally disproven this assumption.

As you were able to understand for yourself within the framework of this self-study program and the numerical experiments, even the simplest mechanical systems with only a single nonlinear term generate a complexity that eludes any analytical calculation. However, the geometric beauty of strange attractors and the universal mathematical structure of bifurcation cascades show that strict regularities also prevail even in apparent chaos.

The methods discussed in this booklet – from the phase portrait to the Poincaré map and the Lyapunov exponents – form the foundation of the modern theory of dynamical systems. Today, they are no longer only applied in mechanics but are indispensable in the modeling of weather phenomena, electronic circuits, chemical reactions (Belousov-Zhabotinsky reaction), as well as in population dynamics and economics.

May this program have sparked your interest in the fascinating structures of the nonlinear world.

---

**End of the Companion Booklet.**
*Copyright © 1995 – Soft-Physics Publishing GmbH, Berlin.*
*All rights reserved.*

---

All pages you have uploaded have now been fully and literally transcribed. If you have any further questions about the physical models or algorithms, I am happy to assist you!

Here is the exact transcription of the next ten pages (pages 41 to 50) of your book, continuously in the same format:

---

---

## Page 41
### Appendix F: List of Used Symbols

The following is a summary of the physical and mathematical symbols used in the text and in the simulation masks.

| Symbol | Physical Meaning | Standard Unit (SI) |
| --- | --- | --- |
| $\phi$ | Deflection angle (pendulum, Pohl's wheel) | rad / deg |
| $\Omega, \dot{\phi}$ | Angular velocity | rad/s / deg/s |
| $\ddot{\phi}$ | Angular acceleration | $\text{rad/s}^2$ |
| $x$ | Linear displacement (spring-mass system) | m |
| $\dot{x}$ | Linear oscillation velocity | m/s |
| $m$ | Mass of the oscillator / unbalance | kg |
| $l$ | Pendulum length / distance of the additional mass | m |
| $I$ | Moment of inertia of the rotating body | $\text{kg}\cdot\text{m}^2$ |
| $g$ | Gravitational acceleration ($9.81$) | $\text{m/s}^2$ |
| $b$ | Damping or friction coefficient | Nms / Ns/m |
| $r$ | Friction exponent | – |
| $A$ | Amplitude of the exciting force / moment | Nm / N |
| $\omega_A$ | Angular frequency of the external excitation | 1/s |
| $T$ | Period of oscillation | s |
| $c$ | Linear spring constant | N/m |
| $d$ | Cubic coefficient of the restoring force | $\text{N/m}^3$ |
| $\lambda$ | Lyapunov exponent | 1/s |
| $\psi$ | Phase angle of the harmonic excitation | rad |

---

---

## Page 42
### Appendix G: Installation Notes for Networks and Windows 95

Although the simulation program was designed as a native MS-DOS application, it can be operated stably in modern system environments as well as in Novell networks, provided certain configurations are adhered to.

#### G.1 Operation under Windows 95

Under the Windows 95 operating system, the program can be started either in MS-DOS mode or in a DOS box (DOS prompt). For smooth graphics output without stuttering, creating a PIF file is recommended:

1. Right-click on the `SCHWING.EXE` file and select **Properties**.
2. Switch to the **Program** tab and click on **Advanced**.
3. Activate the **MS-DOS mode** checkbox as well as **Specify current MS-DOS configuration**.
4. In the **Screen** tab, under "Usage", enter the value **Full-screen**. This prevents Windows from attempting to emulate the VGA signal in a scalable window.

#### G.2 Installation in School Networks (e.g., Novell NetWare)

When used in physics lessons or computer labs, the program can be stored centrally on a server drive:

* The executable file only requires read permissions (`Read` and `File Scan`).
* **Important:** Since the program writes temporary files for graphics export and parameter configuration (`SETUP.DAT`), the working directory of the respective local user must have write permissions (`Write`, `Create`, `Erase`). Use the DOS command `SET` to redirect temporary paths, if necessary.

---

---

## Page 43
### Appendix H: Further Theoretical Deepenings

#### H.1 The Hamilton Formalism for Nonlinear Systems

For theoretically interested readers, the transition from Newton's equations of motion to Hamiltonian mechanics, which allows for an elegant geometric interpretation of phase space, will be briefly outlined here.

For the undamped, free mathematical pendulum (Section 2.2), the Lagrange function $L = T - V$ (Kinetic Energy minus Potential Energy) is:

$$L(\phi, \dot{\phi}) = \frac{1}{2} m l^2 \dot{\phi}^2 - mgl(1 - \cos\phi)$$

The canonically conjugate momentum $p_\phi$ is calculated by differentiation with respect to the generalized velocity:

$$p_\phi = \frac{\partial L}{\partial \dot{\phi}} = m l^2 \dot{\phi} = I \cdot \Omega$$

The Hamilton function $H = T + V$, which corresponds to the total energy of the system, is thus:

$$H(\phi, p_\phi) = \frac{p_\phi^2}{2 I} + mgl(1 - \cos\phi)$$

Hamilton's equations of motion form a system of two coupled first-order differential equations:

$$\begin{aligned}
\dot{\phi} &= \frac{\partial H}{\partial p_\phi} = \frac{p_\phi}{I} \\
\dot{{p}_\phi} &= -\frac{\partial H}{\partial \phi} = -mgl \sin\phi
\end{aligned}$$

This system is exactly equivalent to equations (2.2.1). In phase space $(\phi, p_\phi)$, the trajectories correspond to the contour lines of the function $H(\phi, p_\phi) = E = \text{const}$. Since energy is conserved, no phase space contraction occurs in undamped systems; the divergence of the vector field is identically zero (Liouville's theorem for conservative systems).

---

---

## Page 44
#### H.2 Linearization in the Vicinity of Fixed Points

The qualitative analysis of nonlinear systems typically begins with the determination of fixed points (equilibrium positions) and their stability behavior. A fixed point $(\phi^*, \Omega^*)$ is defined by the vanishing of all time derivatives.

For the free pendulum (Equation 2.3.1), this means:

$$\begin{aligned}
\Omega^* &= 0 \\
-\frac{b}{I}\Omega^* - \frac{mgl}{I}\sin\phi^* &= 0 \implies \sin\phi^* = 0
\end{aligned}$$

This yields two physical fixed points in the interval $[-\pi, +\pi]$:

1. The fixed point $F_1 = (0, 0)$ – the lower equilibrium position.
2. The fixed point $F_2 = (\pi, 0)$ – the upper vertical equilibrium position.

To investigate the dynamics in the immediate vicinity of a fixed point, a Taylor expansion (linearization) is performed. We set $\phi = \phi^* + \xi$ and $\Omega = \Omega^* + \eta$, where $\xi, \eta \ll 1$ represent small displacements.

The Jacobian matrix $J$ of the system (2.3.1) is generally:

$$J(\phi, \Omega) = \begin{pmatrix} 
0 & 1 \\ 
-\frac{mgl}{I}\cos\phi & -\frac{b}{I} 
\end{pmatrix}$$

From the eigenvalues $\mu$ of the linearized matrix, determined from the characteristic equation $\det(J - \mu \cdot E) = 0$, the stability behavior can be precisely classified.

---

---

## Page 45
##### Case 1: Investigation of the lower equilibrium position $F_1 = (0, 0)$

If one inserts the coordinates of the lower fixed point into the Jacobi matrix, one obtains due to $\cos(0) = 1$:

$$J(0,0) = \begin{pmatrix}
0 & 1 \\
-\frac{mgl}{I} & -\frac{b}{I}
\end{pmatrix}$$

The characteristic equation is:

$$\mu^2 + \frac{b}{I}\mu + \frac{mgl}{I} = 0$$

The eigenvalues are given by:

$$\mu_{1,2} = -\frac{b}{2I} \pm \sqrt{\left(\frac{b}{2I}\right)^2 - \frac{mgl}{I}}$$

For small dampings ($b < 2\sqrt{mglI}$), the term under the square root is negative. The eigenvalues are complex conjugate with a negative real part:

$$\mu_{1,2} = -\gamma \pm i\omega_d$$

This mathematically corresponds to a **stable focus** (spiral in phase space). All nearby trajectories spiral into the origin over time, as experimentally shown in Fig. 2.3.1b.

##### Case 2: Investigation of the upper equilibrium position $F_2 = (\pi, 0)$

If one inserts the coordinates of the upper fixed point, one obtains due to $\cos(\pi) = -1$:

$$J(\pi,0) = \begin{pmatrix}
0 & 1 \\
+\frac{mgl}{I} & -\frac{b}{I}
\end{pmatrix}$$

The eigenvalues are calculated here as:

$$\mu_{1,2} = -\frac{b}{2I} \pm \sqrt{\left(\frac{b}{2I}\right)^2 + \frac{mgl}{I}}$$

Since the term under the square root is always greater than $(b/2I)^2$, the root is real and greater than the absolute value of the prefactor. We obtain two real eigenvalues with different signs: $\mu_1 > 0$ and $\mu_2 < 0$. Such a fixed point is called a **saddle point**. It is unstable because trajectories are exponentially pushed away along the direction of the positive eigenvalue.

---

---

## Page 46
#### H.3 Analytical Approximation for the Amplitude Behavior at Large Displacements

As explained in Section 2.2, the period $T$ of the undamped free pendulum increases with increasing amplitude $\phi_m$. An exact analytical calculation leads to an elliptic integral of the first kind, which cannot be solved in closed form:

$$T = 4 \sqrt{\frac{l}{2g}} \int_0^{\phi_m} \frac{d\phi}{\sqrt{\cos\phi - \cos\phi_m}} = T_0 \cdot \frac{2}{\pi} K\left(\sin\frac{\phi_m}{2}\right)$$

where $T_0 = 2\pi\sqrt{l/g}$ is the oscillation period for infinitesimal amplitudes. By means of a Taylor series expansion of the function $K$, a precise approximation formula for practical use can be derived:

$$T \approx T_0 \left( 1 + \frac{1}{4}\sin^2\left(\frac{\phi_m}{2}\right) + \frac{9}{64}\sin^4\left(\frac{\phi_m}{2}\right) + \dots \right)$$

For angles up to $\phi_m \approx 90^\circ$, the first correction term is usually sufficient, which is often also written in a simplified form as the Borda formula:

$$T \approx T_0 \left( 1 + \frac{\phi_m^2}{16} \right) \quad (\phi_m \text{ in radians})$$

##### Comparison Table for Laboratory Practice (Task 1):

The following table shows the deviations between the linear approximation and the exact nonlinear period, which you can numerically verify in Task 1.

| Amplitude $\phi_m$ (deg) | Amplitude $\phi_m$ (rad) | Relative Factor $T/T_0$ | Deviation from harmonic oscillation |
| --- | --- | --- | --- |
| $5^\circ$ | $0.0873$ | $1.0005$ | $+0.05\%$ |
| $20^\circ$ | $0.3491$ | $1.0077$ | $+0.77\%$ |
| $45^\circ$ | $0.7854$ | $1.0400$ | $+4.00\%$ |
| $90^\circ$ | $1.5708$ | $1.1803$ | $+18.03\%$ |
| $150^\circ$ | $2.6180$ | $1.7112$ | $+71.12\%$ |
| $175^\circ$ | $3.0543$ | $3.1642$ | $+216.42\%$ |

---

---

## Page 47
### Appendix I: Complementary Exercise Collection (Advanced Level)

The following additional exercises are aimed at students in higher semesters and require a combination of numerical simulation and analytical derivation.

#### Exercise 7: Melnikov Method for Chaos Prediction

For the driven pendulum, the transition from regular dynamics to chaotic behavior can be approximately analytically delimited. The Melnikov method investigates the intersection of stable and unstable manifolds (separatrix splitting) under the influence of a small perturbation (weak damping $b$ and small amplitude $A$).

1. The critical state is reached when the Melnikov function $M(t_0)$ has zeros. For system (1.1.2), the theoretical condition for chaotic excursions is:
$$\frac{A}{b} \ge \frac{4g}{l \cdot \omega_A \cdot \cosh\left(\frac{\pi \omega_A}{2 \omega_0}\right)}$$

2. Verify this analytical limit in the experimental part of the program. Choose extremely small values for damping and excitation and test whether chaotic behavior can already be detected just below the critical ratio $A/b$.

#### Exercise 8: Investigation of the Fractal Basin of Attraction

If two attractors coexist in the system (as in Section 2.4, Fig. 2.4.3), the separatrix determines the fate of the trajectory.

1. Use the program to systematically raster the basin of attraction. To do this, vary the initial conditions $\phi_0$ in the range from $-180^\circ$ to $+180^\circ$ and $\dot{\phi}_0$ in the range from $-5$ to $+5$ in steps of $2^\circ$.
2. Manually mark on graph paper points that end in the small limit cycle with a cross and points that end in the large limit cycle with a circle.
3. Analyze the boundary line (separatrix). Does it show a smooth geometry or does it exhibit self-similar, fractal structures? (Keyword: *Fractal Basin Boundaries* [13]).

---

---

## Page 48
### Appendix J: List of Numerical Experiments and System Parameters

For a quick reproduction of the graphics printed in the learning section, all exact parameter values and the corresponding mask configurations are tabulated below.

#### J.1 Standard Configurations for the Mathematical Pendulum

In all examples of the first chapter, unless explicitly stated otherwise, the following basic mechanical parameters were used:

* Mass of the pendulum $m = 0.2\text{ kg}$
* Length of the massless rod $l = 0.25\text{ m}$
* Moment of inertia $I = m \cdot l^2 = 0.0125\text{ kg}\cdot\text{m}^2$
* Natural angular frequency of the linear approximation $\omega_0 = \sqrt{g/l} \approx 6.264\text{ s}^{-1}$

##### Overview of Simulation Datasets:

| Figure in Text | Damping $b$ (Nms) | Driver $A$ (Nm) | Frequency $\omega_A$ (1/s) | Initial Values $(\phi_0, \Omega_0)$ | Observed Phenomenon |
| --- | --- | --- | --- | --- | --- |
| **Abb. 2.2.1a** | $0.0000$ | $0.0000$ | $0.0000$ | $(10^\circ, 0.0)$ | Harmonic oscillation, period constant |
| **Abb. 2.2.1b** | $0.0000$ | $0.0000$ | $0.0000$ | $(120^\circ, 0.0)$ | Nonlinear distortion, period increased |
| **Abb. 2.2.2** | $0.0000$ | $0.0000$ | $0.0000$ | $(179.9^\circ, 0.0)$ | Extreme plateau near the saddle point |
| **Abb. 2.3.1b** | $0.0200$ | $0.0000$ | $0.0000$ | $(150^\circ, 2.0)$ | Phase space contraction to fixed-point attractor |
| **Abb. 2.4.1b** | $0.0200$ | $0.2900$ | $4.1760$ | $(0^\circ, 0.0)$ | Transient settling process to T1 limit cycle |
| **Abb. 2.5.2b** | $0.0400$ | $0.5350$ | $4.1760$ | $(10^\circ, 0.0)$ | Period doubling (2 points in Poincaré section) |
| **Abb. 2.5.4b** | $0.0400$ | $0.5500$ | $4.1760$ | $(0^\circ, 0.0)$ | Deterministic Chaos, Strange Attractor |

---

---

## Page 49
### Appendix K: Notes on Numerical Precision and Hardware Influences

When performing long-running chaotic simulations (e.g., when generating the dense bifurcation diagram in Fig. 2.6.1), subtle deviations can occur between the results from different computers. This characteristic is essentially not a software malfunction, but a direct consequence of the mathematical nature of chaos.

#### K.1 Rounding Error Amplification

Since the Lyapunov exponent is positive in the chaotic regime ($\lambda > 0$), the distance between two trajectories increases by a factor of $e^{\lambda t}$ per unit of time. This applies not only to deviations in the physical initial conditions (as in Exercise 6), but also to purely numerical errors.

A typical PC calculates floating-point numbers according to the IEEE-754-Standard with a precision of 64 Bit (Double Precision), which corresponds to approximately 15-17 significant decimal places. The unavoidable rounding error at the smallest integration step is thus unstoppably amplified in the chaotic domain. After a characteristic time duration – the so-called **Lyapunov time** $t_L \approx 1/\lambda$ – the error has grown to the macroscopic level. From this moment on, the calculated curve no longer describes the exact physical path of the real system, but a so-called "pseudotrajectory".

> **Important Note for Teaching:**
> Thanks to the *Shadowing-Theorem* (Beschattungssatz) of topology, the qualitative result in phase space (the fractal geometry of the strange attractor and the statistical characteristics) is mathematically absolutely reliable despite rounding errors. For every numerical pseudotrajectory, there exists a true, exact trajectory with slightly altered initial conditions that describes exactly the same path.

---

---

## Page 50
#### K.2 Influence of the Mathematical Coprocessor (FPU)

Should you perform calculations on systems without a coprocessor using the emulation parameter `/E` (see Section IV.4), the software utilizes internal 32-bit routines to emulate the mathematical operations.

This may result in the point of transition into a chaotic phase in the bifurcation diagram being minimally shifted compared to calculations performed with a genuine hardware FPU (Intel 80387). For quantitative comparisons in experimental protocols, it is therefore strongly recommended to conduct all measurement series within a working group on identical computer architectures.

---

### Directory of Program Files Mentioned in the Text

* `SCHWING.EXE` – The main executable program (simulation environment).
* `SCHWING.OVR` – Overlay file for memory management under MS-DOS.
* `EGAVGA.BGI` – Graphics driver for EGA and VGA screens.
* `LERN.TXT` – Online help and accompanying text for the learning section.
* `SETUP.DAT` – Standard parameter file (automatically generated).
* `READ.ME` – Current last-minute notes on hardware compatibility.

---

**End of the technical appendix.**
*This accompanying material is an integral part of the "Nonlinear Dynamics" software package.*
*Printed in Germany 1995.*

---

## Page 51
### Appendix L: Supplementary Graphics for the Simulation Models

The following figures show typical screen outputs of the program in high-resolution VGA mode, as they can be recorded during the execution of the laboratory exercises (Chapter II).

![Figure L.1: Phase portrait of the Duffing Oscillator showing the classic double-scroll chaotic attractor trajectory looping symmetrically between two main wells.]
Fig. L.1: Phase portrait of the Duffing oscillator in the chaotic state (Hard spring with harmonic excitation, cf. Task 4).
System parameters: $c = -1.0, d = 1.0, b = 0.3, A = 0.4, \omega_A = 1.4$.

![Figure L.2: Stroboskopische Abbildung (Poincaré-Schnitt) of the Duffing attractor, displaying highly resolved fractal filaments and stretching-and-folding structures.]
Fig. L.2: Stroboscopic map (Poincaré section) for the chaotic motion shown in Fig. L.1. The fractal filament structure of the strange attractor becomes clearly visible by hiding the transient transitions.

---

---

## Page 52
### Appendix M: Numerical Values for Root Finding

In the analytical calculation of fixed points and bifurcation boundaries, transcendental equations arise. The following are important reference values listed for numerical adjustment routines.

#### M.1 The first ten zeros of the Bessel function of the first kind $J_0(x)$

These values are particularly needed as critical frequency ratios in the theoretical investigation of frequency-modulated systems and coupled oscillators.

| Order $n$ | Zero $x_n$ | $J_1(x_n)$ | Order $n$ | Zero $x_n$ | $J_1(x_n)$ |
| --- | --- | --- | --- | --- | --- |
| **1** | $2.40482556$ | $+0.5191$ | **6** | $18.07106397$ | $-0.2051$ |
| **2** | $5.52007811$ | $-0.3403$ | **7** | $21.21163663$ | $+0.1903$ |
| **3** | $8.65372791$ | $+0.2715$ | **8** | $24.35247153$ | $-0.1784$ |
| **4** | $11.79153444$ | $-0.2325$ | **9** | $27.49347913$ | $+0.1686$ |
| **5** | $14.93091770$ | $+0.2114$ | **10** | $30.63460647$ | $-0.1603$ |

#### M.2 The Feigenbaum Constants (Universal Scaling Factors)

For systems that transition into chaos via a cascade of period-doublings (Feigenbaum scenario, cf. Section 2.6), the following universal limit values apply:

* **The Bifurcation Ratio ($\delta$):**
Determines the exponential ratio of parameter intervals between successive doublings:
$$\delta = \lim_{n \rightarrow \infty} \frac{\mu_n - \mu_{n-1}}{\mu_{n+1} - \mu_n} \approx 4.669201609102990$$


* **The Scaling Factor for the Pitchfork Width ($\alpha$):**
Describes the scaling behavior of the geometric distances of the bifurcation branches:
$$\alpha = \lim_{n \rightarrow \infty} \frac{d_n}{d_{n+1}} \approx 2.502907875095892$$



---

---

## Page 53
### Appendix N: Source Code for Data Conversion (ASCII Export)

The binary files (`*.BIN`) generated by the simulation program can be converted into readable text files (ASCII) using the following small utility program, if no direct export was performed via the menu.

```pascal
Program Bin2Ascii;
Uses Crt;

Type
  DataRecord = Record
    Time  : Single;
    Angle : Single;
    Omega : Single;
  End;

Var
  InFile  : File Of DataRecord;
  OutFile : Text;
  Rec     : DataRecord;
  NameIn  : String;
  NameOut : String;

Begin
  ClrScr;
  Write('Enter the name of the binary file (e.g., TRAJ.BIN): ');
  ReadLn(NameIn);
  Write('Enter the name of the output file (e.g., DATA.TXT): ');
  ReadLn(NameOut);
  
  Assign(InFile, NameIn);
  Reset(InFile);
  Assign(OutFile, NameOut);
  Rewrite(OutFile);
  
  WriteLn(OutFile, '# Time [s]', #9, 'Angle [rad]', #9, 'Omega [rad/s]');
  
  While Not Eof(InFile) Do
  Begin
    Read(InFile, Rec);
    WriteLn(OutFile, Rec.Time:12:6, #9, Rec.Angle:12:6, #9, Rec.Omega:12:6);
  End;
  
  Close(InFile);
  Close(OutFile);
  WriteLn('Conversion successfully completed.');
End.

```

---

---

## Page 54
### Appendix O: Calibration Data for Pohl's Torsional Pendulum

For users operating the experimental "Pohl's Wheel" in the laboratory (cf. Appendix C), the factory specifications of the standard model are listed below. These data serve as an ideal starting configuration for a realistic simulation.

#### O.1 Mechanical Dimensions and Material Constants

* Diameter of the copper flywheel: $D = 220\text{ mm}$
* Total mass of the rotating system: $M = 0.385\text{ kg}$
* Moment of inertia of the copper disk: $I_0 = 1.85 \cdot 10^{-3}\text{ kg}\cdot\text{m}^2$
* Restoring constant of the helical spring (torsional spring constant): $D^* = 0.0245\text{ Nm/rad}$
* Maximum permissible twist angle: $\phi_{\max} = \pm 190^\circ$

#### O.2 Electrical Specifications of the Eddy Current Brake

The braking effect is regulated via the current flow $I_B$ in the field coils of the electromagnets. The damping constant $b$ behaves approximately quadratically with the applied current strength:

$$b(I_B) \approx \kappa \cdot I_B^2,$$

where the apparatus coefficient for this model was determined to be $\kappa \approx 0.0115\text{ Nms/A}^2$.

##### Reference Table for Damping Adjustment:

| Brake Current $I_B$ (A) | Damping Coefficient $b$ (Nms) | Decay Constant $\gamma$ (1/s) | System Character |
| --- | --- | --- | --- |
| `0.0` | $0.0002$ | $0.054$ | Almost undamped |
| `0.2` | $0.0007$ | $0.189$ | Weak damping |
| `0.5` | $0.0031$ | $0.838$ | Oscillatory case (Lab course) |
| `1.0` | $0.0117$ | $3.162$ | Strong damping |
| `1.5` | $0.0261$ | $7.054$ | Creep limit reached |

---

---

## Page 55
### Appendix P: Mathematical Supplements to Nonlinear Potentials

The dynamic behavior of an undamped, unforced system can be directly derived from the topology of its potential landscape $V(x)$. For a one-dimensional system of the form $\ddot{x} = -\frac{dV}{dx}$, the total energy corresponds to a conserved quantity.

#### P.1 The Potential of the Duffing Oscillator

The equation of motion of the free Duffing oscillator is:

$$\ddot{x} + c \cdot x + d \cdot x^3 = 0$$

The corresponding mechanical potential is obtained by integration as:

$$V(x) = \int (c \cdot x + d \cdot x^3) dx = \frac{1}{2}c \cdot x^2 + \frac{1}{4}d \cdot x^4$$

One distinguishes two fundamental cases depending on the sign of the parameters:

##### 1. The "Hard Spring" Potential ($c > 0, d > 0$)

The potential has a single, parabolic minimum at the origin ($x=0$). The restoring force grows disproportionately with the displacement. All trajectories are global, closed oscillations.

##### 2. The "Double-Well" Potential (*Double-Well*) ($c < 0, d > 0$)

This system describes an elastic buckling rod or an inverted pendulum between two magnets. The origin $x=0$ becomes a local maximum (unstable saddle point). Two new, symmetric minima (stable fixed points) arise at:

$$x^*_{\pm} = \pm \sqrt{-\frac{c}{d}}$$

Trajectories with low total energy oscillate locally in one of the two wells. Trajectories with high energy cross the central maximum and encircle both fixed points.

---

---

## Page 56
### Appendix Q: Numerical Step Size Control in Comparison

Although the program operates by default with a fixed step size $dt$ (cf. Section IV.4), the option for an adaptive Runge-Kutta-Fehlberg method (RKF45) is prepared in the mathematical module. This serves for control in the presence of extremely steep gradients in phase space.

#### Q.1 The Principle of Embedded Methods

The RKF45 method calculates two approximations of different order per integration step: a solution $\vec{x}_{k+1}$ of order 4 and a control solution $\hat{\vec{x}}_{k+1}$ of order 5. Both calculations use the same slope vectors $\vec{k}_i$, which minimizes computational effort.

The local discretization error $\epsilon$ is determined from the difference of both solutions:

$$\epsilon = \|\vec{x}_{k+1} - \hat{\vec{x}}_{k+1}\|$$

If the error is above a predefined tolerance limit ($\epsilon > \text{Tol}_{\max}$), the current calculation step is discarded and repeated with a halved step size $dt_{\text{neu}} = dt/2$. If the error is extremely small ($\epsilon < \text{Tol}_{\min}$), the step size for the next step can be doubled to save computation time.

#### Q.2 Consequences for Stroboscopic Mapping

For the generation of Poincaré sections, a variable $dt$ is problematic because the sampling points must be exactly equidistant in sync with the driver period $T_A = 2\pi/\omega_A$. With adaptive step size, the program must therefore perform an interpolation (e.g., using cubic splines) at the interval boundaries to hit the exact intersection point with the phase plane. This explains why the fixed RK4 method is often preferred in programming practice.

---

---

## Page 57
### Appendix R: Glossary of English Technical Terms (Dictionary of Chaos)

Since modern technical literature on nonlinear dynamics is largely written in English, this short glossary serves as a translation aid for further studies.

*   **Attractor** $\rightarrow$ *Attraktor:* A subset of the phase space towards which all trajectories from a specific basin of attraction tend for $t \rightarrow \infty$.
*   **Basin of Attraction** $\rightarrow$ *Einzugsgebiet:* The region of initial conditions in phase space whose trajectories converge towards the same attractor.
*   **Bifurcation** $\rightarrow$ *Bifurkation / Verzweigung:* A qualitative change in system behavior (e.g., period-doubling) when a control parameter is varied.
*   **Boundary** $\rightarrow$ *Grenzlinie:* The dividing line in phase space, for example, between two basins of attraction (separatrix).
*   **Burst** $\rightarrow$ *Ausbruch:* A sudden, irregular chaotic segment within an intermittent motion.
*   **Driven / Forced Oscillator** $\rightarrow$ *Getriebener Oszillator:* An oscillating system that is subject to an explicitly time-dependent, external force.
*   **Intermittency** $\rightarrow$ *Intermittenz:* A route to chaos in which regular and chaotic phases alternate irregularly.
*   **Limit Cycle** $\rightarrow$ *Grenzzyklus:* An isolated, closed trajectory in the phase space of a dissipative system, corresponding to a periodic oscillation.
*   **Map** $\rightarrow$ *Diskrete Abbildung:* A mathematical equation that describes the system state at discrete time steps ($x_{k+1} = f(x_k)$).
*   **Pitchfork Bifurcation** $\rightarrow$ *Stimmgabel-Bifurkation:* Typical geometry of period-doubling in the Feigenbaum diagram.
*   **Quasiperiodic** $\rightarrow$ *Quasiperiodisch:* A motion based on the superposition of incommensurable frequencies.
*   **Strange Attractor** $\rightarrow$ *Seltsamer Attraktor:* An attractor with fractal geometry and sensitive dependence on initial conditions.

---

---

## Page 58
### Appendix S: Notes on Licensing and Reproduction

The simulation program "Nonlinear Oscillations" included with this accompanying booklet is protected by copyright. The following special regulations apply for use in the educational sector.

#### S.1 Single-User License (Standard)

The included diskette authorizes the installation and use of the program on exactly one computer system. Simultaneous use on multiple computers or provision in public data networks without an additional license is prohibited.

#### S.2 School License / Campus License

For schools, universities, and adult education centers, a cost-effective campus license can be acquired from the publisher. This authorizes:

1. The installation of the program on an unlimited number of computers within the premises of the respective institution.
2. The provision on local file servers as part of computer-aided physics instruction.
3. The reproduction of this accompanying booklet as a copy master for internal use in practical courses.

> **Disclaimer:**
> The developer and the publisher assume no liability for damages resulting directly or indirectly from the installation or operation of this software. As this is a hardware-proximate DOS program, its use is at the user's own risk.

---

---

## Page 59
### Appendix T: System Updates and Add-ons (Version 2.1)

As part of continuous product maintenance, the program package has been expanded with additional mathematical models that were not yet documented in the first edition.

#### T.1 The van der Pol System

The van der Pol oscillator can now also be activated in the **System** menu. The differential equation describes a system with position-dependent, nonlinear damping:

$$\ddot{x} - \epsilon(1 - x^2)\dot{x} + x = 0$$

##### Special Behaviors:

* For small amplitudes ($x < 1$), the damping term is negative ($\epsilon(1-x^2) > 0$). The system extracts energy from its surroundings and oscillates spontaneously.
* For large amplitudes ($x > 1$), the damping becomes positive and slows the system down.
* Regardless of the initial values, all trajectories for $t \rightarrow \infty$ collapse onto an absolutely stable, characteristic **limit cycle** in phase space. This model is used in biophysics to describe heartbeat rhythms and nerve impulses (FitzHugh-Nagumo model).

#### T.2 Optimized Graphics Driver for High-Resolution VGA

By modifying the `EGAVGA.BGI` file, the refresh rate for on-screen animation could be increased by approx. $25\%$. Computers with a clock frequency of $33\text{ MHz}$ (Intel 486DX) or higher are now able to draw chaotic trajectories in phase space in true real-time without delay.

---

---

## Page 60
### Appendix U: Keyword Index for Source Code Variables

For programmers who wish to modify the attached Pascal source code or link their own modules, the central global variable identifiers are declared here.

* `A_amp` (Real): Amplitude of the external excitation force or torque [$Nm$].
* `b_damp` (Real): Global viscous damping coefficient for linear friction.
* `CurrentPageAddress` (Word): Segment address of the VGA VRAM for page-flipping.
* `dt_step` (Real): Fixed time step of the numerical integration (RK4).
* `g_grav` (Real): The gravitational acceleration (initialized program-wide with $9.81\text{ m/s}^2$).
* `I_moment` (Real): Moment of inertia of the pendulum body or the torsional pendulum.
* `l_length` (Real): Geometric length of the massless pendulum rod [$m$].
* `m_mass` (Real): Mass of the oscillating body at its center of gravity [$kg$].
* `omega_A` (Real): Angular frequency of the periodic driver (input in $Hz$ is converted internally).
* `Phi_pos` (Real): The current displacement angle in radians.
* `Omega_vel` (Real): The current angular velocity $\dot{\phi}$ [$rad/s$].
* `Time_elapsed` (Real): The accumulated simulation time since the start of the current run.

---

**End of the extended document appendix.**
*Soft-Physics Distribution, Technical Support Department, Update 1996.*

---

This block of ten pages has now also been fully transcribed. If you have more pages, simply upload them!

---
## Page 61
### Appendix V: Installation Checklist for Laboratory Operation

To ensure a smooth process when conducting the experiments in the practical course, please go through the following checklist before the students arrive.

#### V.1 Technical Preparation of Workstations

* [ ] **Operating System Level:** Check if the `ANSI.SYS` driver is loaded in the `CONFIG.SYS` file (`DEVICE=C:\DOS\ANSI.SYS`). This is absolutely necessary for the correct color display of some text menus.
* [ ] **Memory Configuration:** Ensure that at least $580\text{ KB}$ of conventional DOS memory is free. If necessary, use the `MEM /C` command to create space in the Upper Memory Block (UMB) (`DOS=HIGH,UMB`).
* [ ] **Graphics Compatibility:** Check the graphics card by running the small test program `VGACHECK.EXE`. If the screen remains dark, replace `EGAVGA.BGI` in the program directory with the standard driver from the Borland library.
* [ ] **Mouse Driver:** Load the resident mouse driver (e.g., `MOUSE.COM`) before starting the simulation environment, as otherwise interactive control of the phase space crosshairs will not be possible.

#### V.2 Didactic Preparation

* [ ] Ensure that the `C:\SCHWING\DATA\` directory exists on the local hard drives and is writable for the current user, so that numerical results can be saved for later evaluation.
* [ ] Print out the report templates (Appendix C and I) in sufficient quantity.

---

---

## Page 62
### Appendix W: Version History and Bug Fixes (Errata)

This section documents the most important modifications and bug fixes that have been incorporated into the software package since the initial release of Version 1.0 (Autumn 1994).

#### W.1 Version 1.1 (Spring 1995)

* **Bug Fix in RK4 Module:** A sign error in the calculation of the cubic restoring force term ($dx^3$) in the Duffing module was corrected. In Version 1.0, this led to an erroneous divergence of trajectories to infinity at extremely large amplitudes.
* **User Interface Enhancement:** The `F10` key was globally implemented as "Mask Confirmation" to speed up the workflow during parameter studies.

#### W.2 Version 2.0 (Autumn 1995)

* **Poincaré Section Integration:** The module for generating stroboscopic mappings was completely rewritten. Points are now displayed as fine individual points instead of thick pixels, which significantly improves the resolution of fractal structures (filaments).
* **Support for Mathematical Coprocessors:** The program now automatically detects during boot-up whether an Intel 80387 FPU is present and dynamically switches to optimized 32-bit assembly code.

#### W.3 Current Version 2.1 (January 1996)

* The van der Pol system was added as a new standard model (documentation see Appendix T).
* A memory leak during the continuous generation of the bifurcation diagram (graphics memory overflow after approx. 10,000 iterations) was completely fixed.

---

---

## Page 63
### Appendix X: Order Form for Add-on Modules and Updates

Should you be interested in an expansion of your simulation package or in further teaching materials, cut out this form and send it stamped to the publisher:

**Soft-Physics Publishing GmbH** *Department for Educational Software* *Schönhauser Allee 124* *D-10437 Berlin* ---

#### I/We hereby place a firm order for:

* [ ] **Add-on Module "Coupled Oscillators" (Version 1.0):** Expansion of the program to two pendulum systems connected by a linear spring. Enables the study of beats, energy exchange, and high-dimensional chaos (phase space dimension = 4).
*Price for single-user license: DM 49,– / School license: DM 129,–*
* [ ] **Accompanying Slide Set "Geometry of Chaos":** 24 high-quality color slides for lecture use. Contains high-resolution renderings of strange attractors (Lorenz attractor, Rössler attractor, Hénon map) as well as real laboratory footage.
*Price per set: DM 78,–*
* [ ] **Update Service to Version 2.2 (Delivery on 3.5" Floppy Disk):** Includes the new module for calculating fractal basin boundaries.
*Only upon submission of the original diskette of Version 1.x / 2.0. Service fee: DM 15,–*

##### Billing Address / Institution Stamp:

Name: ________________________________________

Institution/School: _______________________________

Street / House Number: ______________________________

Postcode / City: _______________________________________

Date: ______________ Signature: ___________________

---

**End of Booklet.**

---