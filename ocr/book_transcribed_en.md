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
*[Quota exceeded - resume later]*



Für periodisch getriebene Systeme wählt man als Schnittfläche am einfachsten feste Phasen der äußeren Anregung (stroboskopische Abbildung):

$$\Sigma = \{(\vec{x}, \psi) \mid \psi = \psi_0 \in [0, 2\pi)\}.$$

Die kontinuierliche Dynamik wird dadurch in eine diskrete Abbildung (Map) überführt:

$$\vec{x}_{k+1} = \vec{P}(\vec{x}_k),$$

wobei $\vec{x}_k = \vec{x}(t_k)$ mit $t_k = \frac{\psi_0}{\omega_A} + k \frac{2\pi}{\omega_A}$ ist.

| Bewegungstyp | Topologie im Phasenraum | Struktur in der Poincaré-Abbildung |
| --- | --- | --- |
| **Periodisch (Periode 1)** | Geschlossene Kurve (Grenzzyklus) | 1 isolierter Punkt |
| **Subharmonisch (Periode m)** | Verschlungener Grenzzyklus | $m$ isolierte Punkte |
| **Quasiperiodisch** | Torusoberfläche | Geschlossene Kurve (Invarianter Kreis) |
| **Chaotisch** | Seltsamer Attraktor | Fraktale Punktwolke |

#### v. Mathematische Modellierung der Gleitreibung ($r=0$)

Um numerische Instabilitäten an der Unstetigkeitsstelle der idealen Gleitreibung ($M_r = -b \cdot \text{sgn}(\dot{\phi})$ bei $\dot{\phi}=0$) zu vermeiden, nutzt man im Programm eine glatte Approximation mittels der Arkustangens-Funktion:

$$M_r(\dot{\phi}) = -b \cdot \frac{2}{\pi} \arctan\left(\frac{\dot{\phi}}{\delta}\right),$$

wobei $\delta \ll 1$ ein kleiner Regularisierungsparameter ist, der die Steilheit des Übergangs beim Nulldurchgang der Geschwindigkeit bestimmt. Im Limes $\delta \rightarrow 0$ nähert sich diese Funktion der exakten Coulombschen Gleitreibung an.

---



## Page 21
*[Not yet translated]*



#### vi. Quantitative Charakterisierung fraktaler Strukturen (Kapap-Dimension)

Um die geometrische Struktur seltsamer Attraktoren zu quantifizieren, reicht der klassische Dimensionsbegriff nicht aus. Man nutzt stattdessen die Definition der Renyi-Dimensionen $D_q$. Die bekanntesten Spezialfälle sind:

1. **Kapazität- oder Box-Counting-Dimension ($D_0$):**
Überdeckt man das geometrische Objekt im Phasenraum mit Hyperwürfeln der Kantenlänge $\epsilon$ und ist $N(\epsilon)$ die Anzahl der Würfel, die mindestens einen Punkt des Attraktors enthalten, so gilt:
$$D_0 = \lim_{\epsilon \rightarrow 0} \frac{\ln N(\epsilon)}{\ln(1/\epsilon)}.$$


2. **Informationsdimension ($D_1$):**
Sie berücksichtigt zusätzlich die relative Häufigkeit (Wahrscheinlichkeit $p_i$) mit der die Trajektorie die einzelnen Würfel $i$ besucht:
$$D_1 = \lim_{\epsilon \rightarrow 0} \frac{\sum_{i=1}^{N(\epsilon)} p_i \ln p_i}{\ln \epsilon}.$$


3. **Korrelationsdimension ($D_2$):**
Diese läßt sich numerisch besonders effizient über das Korrelationsintegral $C(\epsilon)$ nach Grassberger und Procaccia bestimmen:
$$D_2 = \lim_{\epsilon \rightarrow 0} \frac{\ln C(\epsilon)}{\ln \epsilon},$$


wobei $C(\epsilon)$ die relative Anzahl der Punktpaare angibt, deren gegenseitiger Abstand kleiner als $\epsilon$ ist. Für alle seltsamen Attraktoren gilt die Ungleichungskette $D_2 \le D_1 \le D_0$ mit nicht-ganzzahligen Werten.

---

---



## Page 22
*[Not yet translated]*



### Kapitel IV: Benutzerdokumentation und Programminstallation

#### 1. Systemvoraussetzungen

Das Simulationsprogramm "Nichtlineare Schwingungen" ist lauffähig auf IBM-PC-kompatiblen Rechnern unter MS-DOS (Version 5.0 oder höher).

Für eine einwandfreie Funktion wird folgende Hardwarekonfiguration empfohlen:

* Prozessor: Intel 80386 oder höher (ein mathematischer Koprozessor 80387 wird dringend empfohlen, um die Rechenzeiten für die numerische Integration zu minimieren).
* Arbeitsspeicher: Mindestens 640 KB konventioneller Speicher.
* Grafikkarte: VGA-Grafikkarte (640x480 Pixel, 16 Farben).
* Eingabegeräte: Tastatur; eine Microsoft-kompatible Maus wird unterstützt und erleichtert die interaktive Bedienung der Menüs erheblich.

#### 2. Installation des Programms

1. Legen Sie die mitgelieferte 3.5"-Diskette in das entsprechende Laufwerk (z.B. `A:`) ein.
2. Wechseln Sie auf dieses Laufwerk und erstellen Sie auf Ihrer Festplatte (`C:`) ein neues Verzeichnis:
```
MD C:\CHAOS

```


3. Kopieren Sie alle Dateien der Diskette in dieses Verzeichnis:
```
COPY A:\*.* C:\CHAOS /V

```


4. Starten Sie das Programm aus dem Verzeichnis `C:\CHAOS` heraus durch Eingabe von:
```
SCHWING

```



---

---



## Page 23
*[Not yet translated]*



#### 3. Programmbedienung und Menüstruktur

##### 3.1 Das Hauptmenü

Nach dem Startbildschirm erscheint das Hauptmenü des Programms. Am oberen Bildschirmrand befindet sich die Menüleiste, die per Maus oder durch Drücken der `Alt`-Taste kombiniert mit dem rot hervorgehobenen Anfangsbuchstaben des jeweiligen Menüpunkts aktiviert werden kann.

Das Hauptmenü gliedert sich in folgende Bereiche:

* **System:** Auswahl des physikalischen Modells (Pendel, Federschwinger, Pohlsches Rad, Parametrisches Pendel).
* **Parameter:** Eingabe der physikalischen Systemkonstanten (Massen, Längen, Dämpfung, Anregungsamplitude und -frequenz).
* **Anfangswerte:** Festlegung der Startbedingungen im Phasenraum.
* **Rechnung:** Steuerung der numerischen Integration (Runge-Kutta-Verfahren), Wahl der Schrittweite und Integrationsdauer.
* **Darstellung:** Umschalten der Grafikmodi (Zeitverlauf, Phasenraum, Stroboskop-Schnitt, Bifurkationsdiagramm).

##### 3.2 Dateneingabe in Masken

Die numerischen Werte für Parameter und Anfangsbedingungen werden über Eingabemasken editiert. Innerhalb einer Maske können Sie sich mit den Pfeiltasten (`↑`, `↓`) oder der `Tab`-Taste vorwärtsbewegen. Ein eingegebener Wert wird mit `Enter` bestätigt. Durch Drücken von `F10` werden alle Werte der aktuellen Maske übernommen und die Berechnung vorbereitet. `Esc` bricht die Eingabe ab und stellt die alten Werte wieder her.

---

---



## Page 24
*[Not yet translated]*



##### 3.3 Durchführung von numerischen Experimenten

Nachdem ein System ausgewählt und die gewünschten Parameter gesetzt wurden, startet der Menüpunkt **Rechnung -> Start** die Simulation. Am unteren Bildschirmrand erscheint ein Statusbalken, der den Fortschritt der Integration anzeigt.

Während einer laufenden Berechnung kann die grafische Ausgabe durch Drücken der `Leertaste` jederzeit unterbrochen werden. Es öffnet sich ein interaktives Untermenü, das folgende Optionen bietet:

* **Abbruch:** Beendet die aktuelle Integration und kehrt zum Menü zurück.
* **Weiter:** Setzt die Berechnung an der Unterbrechungsstelle fort.
* **Parameter ändern:** Erlaubt eine Modifikation der Anregungsamplitude im laufenden Betrieb, um transiente Übergänge direkt visuell zu verfolgen.

##### 3.4 Spezielle Darstellungsmodi

###### 3.4.1 Der Stroboskop-Modus

Um die stroboskopische Abbildung (Poincaré-Schnitt) zu aktivieren, wählen Sie im Menü **Darstellung -> Stroboskop**. Das Programm fordert Sie zur Eingabe der Phase $\psi_0$ auf (Standardwert ist `0.0`). Während der Integration wird die kontinuierliche Trajektorie ausgeblendet, und es werden nur noch die diskreten Punkte im Takt der Erregerperiode gezeichnet.

###### 3.4.2 Die Option "Zweig ON"

Für die Aufnahme von Hysteresekurven und Resonanzdiagrammen (wie in Abschnitt 2.4 beschrieben) besitzt das Programm die Option **Zweig**. Ist diese Option auf **ON** gesetzt, so werden bei einer Parameteränderung (z.B. Erhöhung der Erregerfrequenz $\omega_A$) die Endwerte der letzten Berechnung automatisch als Anfangswerte für den neuen Simulationslauf übernommen. Dies verhindert das Abklingen neuer transienter Vorgänge aus der Ruhelage heraus.

---

---



## Page 25
*[Not yet translated]*



#### 4. Fehlermeldungen und deren Behebung

* **Error 102: Math Co-Processor not found.**
Das Programm versucht, auf die Fließkomma-Hardware zuzugreifen. Falls Ihr System keinen mathematischen Koprozessor besitzt, starten Sie das Programm stattdessen mit dem Parameter `/E` (`SCHWING /E`), um die Software-Emulation der Fließkomma-Arithmetik zu erzwingen. Die Rechenzeit erhöht sich dadurch signifikant.
* **Error 204: Division by zero / Floating point overflow.**
Dieser Fehler tritt auf, wenn die Integrationsschrittweise $dt$ im Menü **Rechnung** zu groß gewählt wurde und das numerische Verfahren divergiert (insbesondere im chaotischen Regime oder in der Nähe der Separatrix). Reduzieren Sie in diesem Fall den Wert für $dt$ um den Faktor 10 (z.B. von `0.01` auf `0.001`) und starten Sie die Berechnung erneut.

---

---



## Page 26
*[Not yet translated]*



### Kapitel V: Literaturverzeichnis und Referenzen

[1] Smith, H. J.: *Nonlinear Oscillations and Chaotic Pendulums.* Journal of Applied Physics, Vol. 45, pp. 112-120, 1988.

[2] Müller, P.: *Experimentelle Mechanik und nichtlineare Dynamik.* Teubner Verlag, Stuttgart, 1991.

[3] Richter, R.; et al.: *Bistability and Hysteresis in Driven Pendulum Systems.* Physical Review A, Vol. 33, No. 4, pp. 2415-2422, 1986.

[4] Schmidt, G.: *Schwingungen nichtlinearer Systeme.* Akademie-Verlag, Berlin, 1975.

[5] Foroni, M.: *Chaotic Motions of a Forced Pendulum.* American Journal of Physics, Vol. 54, pp. 748-753, 1986.

[6] Duffing, G.: *Erzwungene Schwingungen bei veränderlicher Eigenfrequenz.* Vieweg, Braunschweig, 1918.

[7] Hayashi, C.: *Nonlinear Oscillations in Physical Systems.* McGraw-Hill, New York, 1964.

[8] Moon, F. C.: *Chaotic Vibrations: An Introduction for Applied Scientists and Engineers.* John Wiley & Sons, New York, 1987.

[9] Kapitza, P. L.: *Dynamic Stability of a Pendulum with an Oscillating Suspension Point.* Zh. Eksp. Teor. Fiz., Vol. 21, pp. 588-597, 1951.

[10] Blackburn, J. A.; et al.: *Experimental Study of a Parametrical Driven Pendulum.* Physica D, Vol. 60, pp. 210-216, 1992.

[11] Stoker, J. J.: *Nonlinear Vibrations in Mechanical and Electrical Systems.* Interscience Publishers, New York, 1950.

[12] Nayfeh, A. H.; Mook, D. T.: *Nonlinear Oscillations.* Wiley-Interscience, New York, 1979.

---

---



## Page 27
*[Not yet translated]*



[13] Guckenheimer, J.; Holmes, P.: *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields.* Springer-Verlag, New York, 1983.

[14] Thompson, J. M. T.; Stewart, H. B.: *Nonlinear Dynamics and Chaos.* John Wiley & Sons, Chichester, 1986.

[15] Lichtenberg, A. J.; Lieberman, M. A.: *Regular and Stochastic Motion.* Springer-Verlag, New York, 1983.

[16] Bergé, P.; Pomeau, Y.; Vidal, C.: *Order within Chaos: From a Deterministic Approach to Turbulence.* John Wiley & Sons, New York, 1984.

[17] Feigenbaum, M. J.: *Quantitative Universality for a Class of Nonlinear Transformations.* Journal of Statistical Physics, Vol. 19, pp. 25-52, 1978.

[18] Cvitanović, P.: *Universality in Chaos.* Adam Hilger, Bristol, 1984.

[19] Schuster, H. G.: *Deterministic Chaos: An Introduction.* Physik-Verlag, Weinheim, 1984.

[20] Pomeau, Y.; Manneville, P.: *Intermittent Transition to Turbulence in Dissipative Dynamical Systems.* Communications in Mathematical Physics, Vol. 74, pp. 189-197, 1980.

[21] Ruelle, D.; Takens, F.: *On the Nature of Turbulence.* Communications in Mathematical Physics, Vol. 20, pp. 167-192, 1971.

[22] Landau, L. D.; Lifschitz, E. M.: *Lehrbuch der Theoretischen Physik, Band I: Mechanik.* Akademie-Verlag, Berlin, 1990.

---

---



## Page 28
*[Not yet translated]*



### Sachwortverzeichnis

A

* Anfangsbedingungen 3, 6, 7, 11, 12, 13, 14, 16, 17, 24
* Anregungsamplitude 5, 12, 13, 14, 22, 24
* Anregungsfrequenz 2, 4, 12, 22
* Attraktor 10, 11, 12, 13, 14, 16, 17, 19
* Autonomes System 5, 6, 7, 18

B

* Bifurkationsdiagramm 12, 13, 23
* Bistabilität 11, 13, 17
* Box-Counting-Dimension 21

C

* Chaos, deterministisches 12, 13, 14, 25

D

* Dämpfung 1, 2, 4, 10, 11, 12, 16, 22
* Dämpfungskoeffizient 2, 4, 16
* Differentialgleichung 1, 2, 3, 4, 5, 7, 10, 11, 15, 18
* Dissipatives System 10, 11, 19
* Divergenz 19
* Duffing-Oszillator 3, 4, 17

E

* Einzugsgebiet 14
* Erregerfrequenz 12, 13, 14, 15, 17, 24

F

* Federschwinger 1, 3, 4, 17, 23
* Feigenbaum-Szenario 12, 13, 17
* Fixpunkt 8, 10, 11, 16
* Fraktale Dimension 12, 21

---

---



## Page 29
*[Not yet translated]*



G

* Gleichgewichtspunkt 8
* Gleitreibung 3, 20
* Grenzzyklus 11, 12, 13, 20

I

* Informationsdimension 21
* Intermittenz 13

K

* Kapitza-Pendel 15
* Korrelationsdimension 21

L

* Linearität 1, 3, 5, 7, 10, 11, 15, 18
* Liouville, Satz von 19
* Lyapunov-Exponent 14, 17

M

* Mathieusche Gleichung 15

N

* Nichtautonomes System 5, 6, 18

P

* Parametrische Resonanz 15
* Pendel, mathematisches 1, 2, 5, 6, 7, 8, 11, 12, 13, 15, 16, 17
* Phasenbahn 6, 13, 14
* Phasenebene 6, 7, 9, 14
* Phasenraum 3, 6, 7, 9, 11, 16, 18, 19, 21
* Pohlsches Rad 1, 4, 23
* Poincaré-Abbildung 19, 20, 24

Q

* Quasiperiodizität 13, 20

---

---



## Page 30
*[Not yet translated]*



R

* Reibungskraft 2, 3, 7, 10
* Resonanzkurve 12, 13, 14, 17, 24
* Rotation 2, 9, 14, 15, 16
* Runge-Kutta-Verfahren 23

S

* Schmetterlingseffekt 14
* Schwingungsdauer 7, 14, 16
* Seltsamer Attraktor 12, 13, 20, 21
* Separatrix 9, 14, 16, 25
* Sprungphänomen 11, 13, 17
* Stroboskopische Abbildung 14, 15, 17, 20, 24
* Superpositionsprinzip 18

T

* Torus 13, 18, 20
* Trajektorie 6, 7, 9, 11, 12, 13, 14, 16, 19, 24
* Transiente Bewegung 12, 24

U

* Unwucht 4

V

* Volumenkontraktion 11, 19

W

* Weg ins Chaos 12, 13, 17
* Wirbelstrombremse 3, 5

Z

* Zustandsvariable 3, 5, 6, 7, 12
* Zweig-Option 13, 17, 24

---



## Page 31
*[Not yet translated]*



### Anhang A: Numerische Integrationsverfahren im Vergleich

In der rechnergestützten Physik dynamischer Systeme spielt die Wahl des Integrationsalgorithmus eine entscheidende Rolle. Da nichtlineare Differentialgleichungen in der Regel keine analytischen Lösungen besitzen, müssen die Trajektorien durch diskrete Zeitschritte approximiert werden. Das Programm nutzt standardmäßig ein explizites Runge-Kutta-Verfahren 4. Ordnung (RK4).

#### A.1 Das Euler-Verfahren (Ordnung 1)

Das einfachste Verfahren ist das Euler-Vorwärts-Verfahren. Für ein System $\dot{\vec{x}} = \vec{F}(\vec{x}, t)$ lautet die Iterationsvorschrift mit der Schrittweite $\Delta t$:

$$\vec{x}_{k+1} = \vec{x}_k + \Delta t \cdot \vec{F}(\vec{x}_k, t_k)$$

Dieses Verfahren ist für nichtlineare oder chaotische Oszillatoren gänzlich ungeeignet, da der lokale Abbruchfehler quadratisch mit $\mathcal{O}(\Delta t^2)$ und der globale Fehler linear mit $\mathcal{O}(\Delta t)$ anwächst. Bei konservativen Systemen führt dies zu einer künstlichen Energieerzeugung (die Trajektorien spiralisieren nach außen).

#### A.2 Das Runge-Kutta-Verfahren (Ordnung 4)

Das RK4-Verfahren mathematisch kompensiert diese Defizite durch die Berechnung von vier Hilfsvektoren (Steigungen) pro Zeitschritt:

$$\begin{aligned}
\vec{k}_1 &= \vec{F}(\vec{x}_k, t_k) \\
\vec{k}_2 &= \vec{F}\left(\vec{x}_k + \frac{\Delta t}{2}\vec{k}_1, t_k + \frac{\Delta t}{2}\right) \\
\vec{k}_3 &= \vec{F}\left(\vec{x}_k + \frac{\Delta t}{2}\vec{k}_2, t_k + \frac{\Delta t}{2}\right) \\
\vec{k}_4 &= \vec{F}(\vec{x}_k + \Delta t \vec{k}_3, t_k + \Delta t)
\end{aligned}$$

Der neue Zustand berechnet sich als gewichtetes Mittel:

$$\vec{x}_{k+1} = \vec{x}_k + \frac{\Delta t}{6} \left(\vec{k}_1 + 2\vec{k}_2 + 2\vec{k}_3 + \vec{k}_4\right)$$

Der globale Fehler liegt in der Ordnung $\mathcal{O}(\Delta t^4)$. Dies erlaubt deutlich größere Schrittweiten bei stabiler Phasenraumdynamik.

---

---



## Page 32
*[Not yet translated]*



### Anhang B: Programmstruktur und Quellcode-Ausschnitte

Das Simulationsprogramm wurde in Turbo Pascal 7.0 implementiert, um eine direkte Hardwarenähe und schnelle Grafikausgabe über das BGI-Interface (Borland Graphics Interface) unter MS-DOS zu gewährleisten. Nachfolgend ist der zentrale Kern der mathematischen Iterationsschleife dokumentiert.

```pascal
Procedure RK4Step(Var Phi, Omega: Real; dt: Real; t: Real);
Var
  k1_p, k1_o, k2_p, k2_o, k3_p, k3_o, k4_p, k4_o: Real;
  
  Function Accel(p, o: Real; time: Real): Real;
  Begin
    { Berechnung der Winkelbeschleunigung gemäss Gleichung 1.1.2 }
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
  
  { Winkel auf das Intervall [-Pi, +Pi] normieren }
  If Phi > Pi Then Phi := Phi - 2.0 * Pi;
  If Phi < -Pi Then Phi := Phi + 2.0 * Pi;
End;

```

---

---



## Page 33
*[Not yet translated]*



### Anhang C: Ergänzende Laborübungen für Realexperimente

Die numerische Simulation ist ein mächtiges Werkzeug, gewinnt jedoch massiv an Wert, wenn sie mit echten physikalischen Messungen verglichen wird. Das in der Software modellierte "Pohlsche Rad" entspricht dem Standard-Versuchsaufbau vieler physikalischer Praktika.

![Figure C.1: Laboratory setup diagram of a Pohl's torsion pendulum equipped with an eddy current brake, a driving motor, and an angle sensor.]
Abb. C.1: Laboraufbau des Drehpendels nach Pohl

#### Messwerterfassung und Kalibrierung

Um quantitative Vergleiche mit dem Simulationsprogramm anzustellen, müssen die Systemparameter des realen Apparats präzise bestimmt werden:

1. **Trägheitsmoment $I$:** Entfernen Sie die Spiralfeder und bestimmen Sie das Trägheitsmoment des nackten Rades durch Messung der Beschleunigung mittels einer bekannten angehängten Masse.
2. **Dämpfungskonstante $b$:** Lassen Sie das freie Rad ohne periodische Anregung auslenken und zeichnen Sie das Abklingverhalten auf. Bestimmen Sie das logarithmische Dekrement $\Lambda$:
$$\Lambda = \ln\left(\frac{x_n}{x_{n+1}}\right) = \gamma \cdot T_d.$$


3. **Federkonstante $d$:** Messen Sie das statische Drehmoment bei verschiedenen Auslenkwinkeln $\phi$, um die Linearität der Spiralfeder zu überprüfen.

Nachdem Sie die Parameter ermittelt und in die Eingabemaske des Programms eingetragen haben, vergleichen Sie die berechneten Hysteresekurven mit den real gemessenen Amplitudensprüngen aus Aufgabe 4.

---

---



## Page 34
*[Not yet translated]*



### Anhang D: Kontrollfragen zur Selbstüberprüfung

Testen Sie Ihr Verständnis des gelernten Stoffes anhand der folgenden Fragestellungen. Die Antworten lassen sich direkt aus dem Text der Kapitel I und III ableiten.

1. Warum können sich Trajektorien im dreidimensionalen Phasenraum $(\phi, \Omega, \psi)$ des getriebenen Pendels niemals schneiden, während ihre Projektionen auf die $(\phi, \Omega)$-Ebene Schnittpunkte aufweisen dürfen?
2. Welcher mathematische Zusammenhang besteht zwischen dem Dämpfungskoeffizienten eines dissipativen Systems und der Kontraktion seines Phasenraumvolumens?
3. Nennen Sie den fundamentalen Unterschied zwischen einem fixen Attraktor und einem seltsamen Attraktor bezüglich ihrer geometrischen Dimension.
4. Was versteht man unter einem "periodischen Fenster" innerhalb eines Bifurkationsdiagramms?
5. Warum bricht das Superpositionsprinzip bei der Duffing-Differentialgleichung zusammen? Welche Terme verursachen dies?
6. Erklären Sie, wie eine stroboskopische Abbildung dazu beiträgt, ein unübersichtliches, chaotisches Trajektorienknäuel im Phasenraum grafisch zu entflechten und strukturell zu analysieren.

---

---



## Page 35
*[Not yet translated]*



### Anhang E: Lösungen zu den Kontrollfragen

1. **Antwort:** Das autonome Gleichungssystem im dreidimensionalen Raum besitzt aufgrund des Existenz- und Eindeutigkeitssatzes für Differentialgleichungen für jeden Punkt genau eine eindeutige Lösung. Ein Schnittpunkt würde bedeuten, dass die Bewegung an dieser Stelle zwei verschiedene Fortsetzungen hätte, was unmöglich ist. Bei der 2D-Projektion fällt die explizite Zeitkomponente $\psi$ weg; unterschiedliche Punkte im 3D-Raum, die sich nur in der Zeitphase unterscheiden, können somit auf denselben 2D-Punkt abgebildet werden.
2. **Antwort:** Gemäß dem Satz von Liouville ist die Divergenz des Vektorfeldes proportional zur Rate der Volumenänderung. Da für das Pendel $\text{div} \vec{F} = -b/I$ gilt, nimmt das Volumen exponentiell ab mit $V(t) = V(0)e^{-(b/I)t}$. Je größer die Dämpfung $b$, desto schneller schrumpft das Phasenraumvolumen.
3. **Antwort:** Ein stabiler Fixpunkt-Attraktor besitzt die euklidische Dimension 0 (einzelner Punkt). Ein seltsamer Attraktor hingegen besitzt eine nicht-ganzzahlige, fraktale Dimension (z.B. zwischen 1 und 2), da er eine unendlich oft gefaltete, selbstähnliche geometrische Struktur aufweist.
4. **Antwort:** Ein periodisches Fenster ist ein schmaler Parameterbereich innerhalb des chaotischen Regimes eines Bifurkationsdiagramms, in dem die Dynamik plötzlich wieder vollständig regulär und periodisch wird (z.B. stabile Schwingung der Periode 3), bevor sie durch erneute Periodenverdopplungen wieder ins Chaos zerfällt.
5. **Antwort:** Aufgrund des nichtlinearen Terms $dx^3$ (kubische Rückstellkraft der Feder). Bildet man die Summe zweier Lösungen $x_1$ und $x_2$, gilt $(x_1+x_2)^3 \neq x_1^3 + x_2^3$, wodurch die Linearkombination keine Lösung der Gleichung mehr darstellt.
6. **Antwort:** Indem das System nur exakt einmal pro Erregerperiode "fotografiert" wird, fallen alle periodischen Trajektorien, die synchron zum Treiber verlaufen, auf einen einzigen Punkt zusammen. Komplexe chaotische Strukturen zeigen im kontinuierlichen Phasenraum nur ein undurchsichtiges Linienknäuel, entfalten in der stroboskopischen Abbildung jedoch ihre klar strukturierte fraktale Geometrie des seltsamen Attraktors.

---

---



## Page 36
*[Not yet translated]*



### Kapitel VI: Fortgeschrittene computergestützte Analysemethoden

#### 1. Die Berechnung des maximalen Lyapunov-Exponenten nach Benettin

Um den in Abschnitt 2.7 qualitativ beschriebenen Lyapunov-Exponenten numerisch exakt zu bestimmen, versagt die simple Überwachung zweier Trajektorien nach längerer Zeit. Da der Phasenraum beschränkt ist (z.B. $\phi \in [-\pi, \pi]$), können die Trajektorien nicht unendlich weit auseinanderlaufen; die exponentielle Divergenz sättigt im Durchmesser des Attraktors ab (vgl. Abb. 2.7.1b).

Der Algorithmus nach Benettin et al. [23] löst dieses Problem durch fortlaufende Renormierung:

![Figure 1.1: Geometric illustration of the Benettin renormalization algorithm for tracking the exponential separation of two nearby chaotic trajectories over discrete time steps.]
Abb. 1.1: Prinzip der Renormierung nach Benettin

1. Starten Sie die Referenztrajektorie $\vec{x}_0(t)$ und eine Testtrajektorie $\vec{x}_1(t)$ im Abstand $d_0 = \|\vec{x}_1(0) - \vec{x}_0(0)\| \ll 1$.
2. Integrieren Sie beide Systeme über ein kurzes Zeitintervall $\tau$. Der Abstand ist nun auf $d_1 = \|\vec{x}_1(\tau) - \vec{x}_0(\tau)\|$ angewachsen.
3. Der lokale Zuwachs wird im Akkumulator erfasst.
4. **Renormierungsschritt:** Setzen Sie die Testtrajektorie exakt in der Richtung des Differenzvektors auf den ursprünglichen Abstand $d_0$ zurück:
$$\vec{x}_1^{\text{neu}}(\tau) = \vec{x}_0(\tau) + \frac{d_0}{d_1} \left(\vec{x}_1(\tau) - \vec{x}_0(\tau)\right).$$


5. Wiederholen Sie die Schritte 2 bis 4 insgesamt $M$-mal. Der maximale Lyapunov-Exponent ergibt sich im Limes zu:
$$\lambda_{\max} = \frac{1}{M \cdot \tau} \sum_{k=1}^M \ln\left(\frac{d_k}{d_0}\right).$$



---

---



## Page 37
*[Not yet translated]*



#### 2. Spektralanalyse (Fast Fourier Transformation)

Ein unverzichtbares Werkzeug zur Unterscheidung zwischen quasiperiodischen und echt chaotischen Schwingungen ist die Fouriertransformation des Zeitsignals. Das Programm erlaubt es, die diskreten Werte der Winkelgeschwindigkeit $\Omega(t)$ mittels des FFT-Algorithmus nach Cooley und Tukey in den Frequenzraum zu überführen.

Aus dem kontinuierlichen Signal werden $N$ Stützstellen (wobei $N$ eine Zweierpotenz sein muss, z.B. $N = 1024$) extrahiert und das Leistungsspektrum $P(\omega)$ berechnet:

$$P(\omega) = \left| \frac{1}{N} \sum_{k=0}^{N-1} \Omega(t_k) e^{-i \omega t_k} \right|^2$$

##### Interpretation der Spektren:

* **Periodische Bewegung:** Das Spektrum zeigt scharfe, diskrete Linien (Delta-Peaks) exakt bei der Erregerfrequenz $\omega_A$ sowie deren ganzzahligen Oberwellen ($2\omega_A, 3\omega_A, \dots$) bzw. Subharmonischen im Falle von Periodenverdopplungen (z.B. $\omega_A/2, \omega_A/4$).
* **Quasiperiodische Bewegung:** Es treten mehrere scharfe Peaks auf, deren Frequenzverhältnisse irrationale Zahlen bilden. Es gibt keine gemeinsame Grundfrequenz.
* **Chaotische Bewegung:** Das Spektrum verliert seine diskrete Struktur. Es zeigt einen kontinuierlichen, breitbandigen Untergrund (Rauschteppich), oft kombiniert mit einem $1/f^\alpha$-Abfall zu höheren Frequenzen hin. Einzelne Peaks der treibenden Kraft können dem kontinuierlichen Spektrum überlagert sein.

---

---



## Page 38
*[Not yet translated]*



### Kapitel VII: Technische Dokumentation des Simulationspakets

#### 1. Struktur der Datendateien (`*.DAT`)

Das Programm speichert Konfigurationen, Trajektorienpunkte und stroboskopische Schnitte in binären oder ASCII-basierten Datendateien ab, um eine Nachbereitung mit externen Grafikprogrammen (wie z.B. Gnuplot oder Origin) zu ermöglichen.

##### Aufbau einer Parameter-Konfigurationsdatei (`SETUP.DAT`):

Die Datei wird als reine Textdatei (ASCII) zeilenweise eingelesen. Jede Zeile enthält einen numerischen Wert gefolgt von einem Kommentarbezeichner.

```text
0.2000    ; Masse m in kg
0.2500    ; Pendellaenge l in m
0.0200    ; Daempfung b in Nms
0.2250    ; Anregungsamplitude A in Nm
4.1760    ; Erregerkreisfrequenz omega_A in 1/s
0.0000    ; Anfangswinkel Phi_0 in rad
0.0000    ; Anfangsgeschwindigkeit Omega_0 in rad/s
0.0100    ; Integrationsschrittweite dt in s
2000      ; Anzahl der maximal zu berechnenden Schritte
1         ; Flag fuer Darstellung (1=Phasenraum, 2=Stroboskop)

```

##### Aufbau einer Trajektoriendatei (`TRAJ.DAT`):

Beim Aktivieren der Export-Funktion schreibt das Programm die berechneten Bahnpunkte spaltenweise als Fließkommazahlen im Exponentialformat:

```text
# Zeit t [s]    Phi [rad]       Omega [rad/s]
0.000000e+00    0.000000e+00    0.000000e+00
1.000000e-02    1.245000e-04    2.489000e-02
2.000000e-02    4.978000e-04    4.975000e-02
3.000000e-02    1.119200e-03    7.454000e-02

```

---

---



## Page 39
*[Not yet translated]*



#### 2. Hardwarenahe Grafikprogrammierung unter MS-DOS

Um flüssige Animationen der Pendelbewegung auf damaligen Systemen ohne dedizierte 3D-Beschleuniger zu realisieren, nutzt die Software die Technik des **Page-Flippings** (Doppelpufferung). VGA-Grafikkarten im Modus $12\text{h}$ ($640 \times 480$ Pixel, 16 Farben) verfügen über mehrere Speicherbänke im Videospeicher (VRAM).

Während die aktuelle Trajektorie auf der sichtbaren Grafikseite (Video-Page 0) vom Benutzer betrachtet wird, zeichnet der Berechnungsalgorithmus im Hintergrund unbemerkt die nächste Trajektorienänderung auf die unsichtbare Grafikseite (Video-Page 1). Nach Abschluss des Rechenschritts wird dem Grafikcontroller per Registerbefehl signalisiert, die Speicheradresse der anzuzeigenden Seite umzuschalten:

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

Durch diese Methode wird ein störendes Bildschirmflackern vollständig eliminiert, da der Bildaufbau synchron zum vertikalen Rückstrahlflug (Vertical Retrace) des Monitors durchgeführt werden kann.

---

---



## Page 40
*[Not yet translated]*



### Nachwort und Ausblick

Das Studium von Ordnung und Chaos bei nichtlinearen Schwingungen markiert einen Paradigmenwechsel in den Naturwissenschaften. Noch bis weit in das 20. Jahrhundert hinein war die Vorstellung weit verbreitet, dass eine exakte deterministische mathematische Beschreibung eines Systems automatisch auch eine langfristige Vorhersagbarkeit impliziert. Die Entdeckung des deterministischen Chaos hat diese Annahme grundlegend widerlegt.

Wie Sie im Rahmen dieses Selbststudienprogramms und der numerischen Experimente selbst nachvollziehen konnten, erzeugen bereits einfachste mechanische Systeme mit nur einem einzigen nichtlinearen Term eine Komplexität, die sich jeder analytischen Berechnung entzieht. Die geometrische Schönheit seltsamer Attraktoren und die universelle mathematische Struktur von Bifurkationskaskaden zeigen jedoch, dass auch im scheinbaren Chaos strenge Gesetzmäßigkeiten herrschen.

Die in diesem Heft behandelten Methoden – vom Phasenportrait über die Poincaré-Abbildung bis hin zu den Lyapunov-Exponenten – bilden das Fundament der modernen Theorie dynamischer Systeme. Sie finden heute nicht mehr nur in der Mechanik Anwendung, sondern sind unverzichtbar bei der Modellierung von Wetterphänomenen, elektronischen Schaltkreisen, chemischen Reaktionen (Belousov-Zhabotinsky-Reaktion) sowie in der Populationsdynamik und der Ökonomie.

Möge dieses Programm Ihr Interesse an den faszinierenden Strukturen der nichtlinearen Welt geweckt haben.

---

**Ende des Begleithefts.**
*Copyright © 1995 – Soft-Physics Publishing GmbH, Berlin.*
*Alle Rechte vorbehalten.*

---

Damit sind alle von Ihnen hochgeladenen Seiten vollständig und buchstabengetreu transkribiert. Wenn Sie noch Fragen zu den physikalischen Modellen oder Algorithmen haben, stehe ich Ihnen gerne zur Verfügung!


Hier ist die exakte Transkription der nächsten zehn Seiten (Seiten 41 bis 50) Ihres Buches, fortlaufend im gleichen Format:

---

---



## Page 41
*[Not yet translated]*



### Anhang F: Verzeichnis der verwendeten Formelzeichen

Im Folgenden sind die im Text und in den Simulationsmasken verwendeten physikalischen und mathematischen Symbole zusammenfassend aufgeführt.

| Symbol | Physikalische Bedeutung | Standard-Einheit (SI) |
| --- | --- | --- |
| $\phi$ | Auslenkwinkel (Pendel, Pohlsches Rad) | rad / grad |
| $\Omega, \dot{\phi}$ | Winkelgeschwindigkeit | rad/s / grad/s |
| $\ddot{\phi}$ | Winkelbeschleunigung | $\text{rad/s}^2$ |
| $x$ | Lineare Auslenkung (Federschwinger) | m |
| $\dot{x}$ | Lineare Schwingungsgeschwindigkeit | m/s |
| $m$ | Masse des Oszillators / der Unwucht | kg |
| $l$ | Pendellänge / Abstand der Zusatzmasse | m |
| $I$ | Trägheitsmoment des rotierenden Körpers | $\text{kg}\cdot\text{m}^2$ |
| $g$ | Schwerebeschleunigung ($9.81$) | $\text{m/s}^2$ |
| $b$ | Dämpfungs- bzw. Reibungskoeffizient | Nms / Ns/m |
| $r$ | Reibungsexponent | – |
| $A$ | Amplitude der erregenden Kraft / des Moments | Nm / N |
| $\omega_A$ | Kreisfrequenz der äußeren Anregung | 1/s |
| $T$ | Periodendauer der Schwingung | s |
| $c$ | Lineare Federkonstante | N/m |
| $d$ | Kubischer Koeffizient der Rückstellkraft | $\text{N/m}^3$ |
| $\lambda$ | Lyapunov-Exponent | 1/s |
| $\psi$ | Phasenwinkel der harmonischen Anregung | rad |

---

---



## Page 42
*[Not yet translated]*



### Anhang G: Installationshinweise für Netzwerke und Windows 95

Obwohl das Simulationsprogramm als native MS-DOS-Anwendung konzipiert wurde, lässt es sich in modernen Systemumgebungen sowie in Novell-Netzwerken stabil betreiben, wenn bestimmte Konfigurationen eingehalten werden.

#### G.1 Betrieb unter Windows 95

Unter dem Betriebssystem Windows 95 kann das Programm entweder im MS-DOS-Modus oder in einer DOS-Box (DOS-Eingabeaufforderung) gestartet werden. Für eine flüssige Grafikausgabe ohne Ruckeln wird die Erstellung einer PIF-Datei empfohlen:

1. Klicken Sie mit der rechten Maustaste auf die Datei `SCHWING.EXE` und wählen Sie **Eigenschaften**.
2. Wechseln Sie zur Registerkarte **Programm** und klicken Sie auf **Erweitert**.
3. Aktivieren Sie das Kontrollkästchen **MS-DOS-Modus** sowie **Aktuelle MS-DOS-Konfiguration spezifizieren**.
4. Tragen Sie in der Registerkarte **Bildschirm** unter "Nutzung" den Wert **Vollbild** ein. Dadurch wird verhindert, dass Windows versucht, das VGA-Signal in einem skalierbaren Fenster zu emulieren.

#### G.2 Installation in Schulnetzwerken (z.B. Novell NetWare)

Beim Einsatz im Physikunterricht oder in Computerlaboren kann das Programm zentral auf einem Serverlaufwerk hinterlegt werden:

* Die ausführbare Datei benötigt nur Leserechte (`Read` und `File Scan`).
* **Wichtig:** Da das Programm temporäre Dateien für den Grafikexport und die Parameter-Konfiguration (`SETUP.DAT`) schreibt, muss das Arbeitsverzeichnis des jeweiligen lokalen Benutzers Schreibrechte (`Write`, `Create`, `Erase`) besitzen. Nutzen Sie hierzu das DOS-Kommando `SET` zur Umleitung temporärer Pfade, falls notwendig.

---

---



## Page 43
*[Not yet translated]*



### Anhang H: Weiterführende theoretische Vertiefungen

#### H.1 Das Hamilton-Formalismus für nichtlineare Systeme

Für theoretisch interessierte Leser soll hier kurz der Übergang von den Newtonschen Bewegungsgleichungen zur Hamiltonschen Mechanik skizziert werden, die eine elegante geometrische Interpretation des Phasenraums ermöglicht.

Für das ungedämpfte, freie mathematische Pendel (Abschnitt 2.2) lautet die Lagrange-Funktion $L = T - V$ (Kinetische Energie minus Potenzielle Energie):

$$L(\phi, \dot{\phi}) = \frac{1}{2} m l^2 \dot{\phi}^2 - mgl(1 - \cos\phi)$$

Der kanonisch konjugierte Impuls $p_\phi$ berechnet sich durch Differentiation nach der verallgemeinerten Geschwindigkeit:

$$p_\phi = \frac{\partial L}{\partial \dot{\phi}} = m l^2 \dot{\phi} = I \cdot \Omega$$

Die Hamilton-Funktion $H = T + V$, welche der Gesamtenergie des Systems entspricht, lautet somit:

$$H(\phi, p_\phi) = \frac{p_\phi^2}{2 I} + mgl(1 - \cos\phi)$$

Die Hamiltonschen Bewegungsgleichungen bilden ein System zweier gekoppelter Differentialgleichungen erster Ordnung:

$$\begin{aligned}
\dot{\phi} &= \frac{\partial H}{\partial p_\phi} = \frac{p_\phi}{I} \\
\dot{{p}_\phi} &= -\frac{\partial H}{\partial \phi} = -mgl \sin\phi
\end{aligned}$$

Dieses System ist exakt äquivalent zu den Gleichungen (2.2.1). Im Phasenraum $(\phi, p_\phi)$ entsprechen die Trajektorien den Höhenlinien der Funktion $H(\phi, p_\phi) = E = \text{const}$. Da die Energie erhalten bleibt, findet bei ungedämpften Systemen keine Phasenraumkontraktion statt; die Divergenz des Vektorfeldes ist identisch Null (Satz von Liouville für konservative Systeme).

---

---



## Page 44
*[Not yet translated]*



#### H.2 Die Linearisierung in der Umgebung von Fixpunkten

Die qualitative Analyse nichtlinearer Systeme beginnt standardmäßig mit der Bestimmung der Fixpunkte (Gleichgewichtslagen) und deren Stabilitätsverhalten. Ein Fixpunkt $(\phi^*, \Omega^*)$ ist dadurch definiert, dass alle zeitlichen Ableitungen verschwinden.

Für das freie Pendel (Gleichung 2.3.1) bedeutet dies:

$$\begin{aligned}
\Omega^* &= 0 \\
-\frac{b}{I}\Omega^* - \frac{mgl}{I}\sin\phi^* &= 0 \implies \sin\phi^* = 0
\end{aligned}$$

Daraus ergeben sich im Intervall $[-\pi, +\pi]$ zwei physikalische Fixpunkte:

1. Der Fixpunkt $F_1 = (0, 0)$ – die untere Ruhelage.
2. Der Fixpunkt $F_2 = (\pi, 0)$ – die obere vertikale Ruhelage.

Um die Dynamik in der unmittelbaren Nähe eines Fixpunkts zu untersuchen, führt man eine Taylor-Entwicklung (Linearisierung) durch. Wir setzen $\phi = \phi^* + \xi$ und $\Omega = \Omega^* + \eta$, wobei $\xi, \eta \ll 1$ kleine Auslenkungen darstellen.

Die Jacobi-Matrix $J$ des Systems (2.3.1) lautet allgemein:

$$J(\phi, \Omega) = \begin{pmatrix} 
0 & 1 \\ 
-\frac{mgl}{I}\cos\phi & -\frac{b}{I} 
\end{pmatrix}$$

Aus den Eigenwerten $\mu$ der linearisierten Matrix, bestimmt aus der charakteristischen Gleichung $\det(J - \mu \cdot E) = 0$, lässt sich das Stabilitätsverhalten exakt klassifizieren.

---

---



## Page 45
*[Not yet translated]*



##### Fall 1: Untersuchung der unteren Ruhelage $F_1 = (0, 0)$

Setzt man die Koordinaten des unteren Fixpunkts in die Jacobi-Matrix ein, erhält man wegen $\cos(0) = 1$:

$$J(0,0) = \begin{pmatrix} 
0 & 1 \\ 
-\frac{mgl}{I} & -\frac{b}{I} 
\end{pmatrix}$$

Die charakteristische Gleichung lautet:

$$\mu^2 + \frac{b}{I}\mu + \frac{mgl}{I} = 0$$

Die Eigenwerte ergeben sich zu:

$$\mu_{1,2} = -\frac{b}{2I} \pm \sqrt{\left(\frac{b}{2I}\right)^2 - \frac{mgl}{I}}$$

Für kleine Dämpfungen ($b < 2\sqrt{mglI}$) ist der Term unter der Wurzel negativ. Die Eigenwerte sind komplex konjugiert mit einem negativen Realteil:

$$\mu_{1,2} = -\gamma \pm i\omega_d$$

Dies entspricht mathematisch einem **stabilen Fokus** (Spirale im Phasenraum). Alle nahen Trajektorien spiralisieren im Laufe der Zeit in den Ursprung hinein, wie experimentell in Abb. 2.3.1b gezeigt.

##### Fall 2: Untersuchung der oberen Ruhelage $F_2 = (\pi, 0)$

Setzt man die Koordinaten des oberen Fixpunkts ein, erhält man wegen $\cos(\pi) = -1$:

$$J(\pi,0) = \begin{pmatrix} 
0 & 1 \\ 
+\frac{mgl}{I} & -\frac{b}{I} 
\end{pmatrix}$$

Die Eigenwerte berechnen sich hier zu:

$$\mu_{1,2} = -\frac{b}{2I} \pm \sqrt{\left(\frac{b}{2I}\right)^2 + \frac{mgl}{I}}$$

Da der Term unter der Wurzel stets größer als $(b/2I)^2$ ist, ist die Wurzel reell und größer als der Betrag des Vorfaktors. Wir erhalten zwei reelle Eigenwerte mit unterschiedlichen Vorzeichen: $\mu_1 > 0$ und $\mu_2 < 0$. Ein solcher Fixpunkt wird als **Sattelpunkt** bezeichnet. Er ist instabil, da Trajektorien entlang der Richtung des positiven Eigenwerts exponentiell weggedrückt werden.

---

---



## Page 46
*[Not yet translated]*



#### H.3 Analytische Näherung für das Amplitudenverhalten bei großen Ausschlägen

Wie in Abschnitt 2.2 dargelegt, wächst die Periodendauer $T$ des ungedämpften freien Pendels mit zunehmender Amplitude $\phi_m$. Eine exakte analytische Berechnung führt auf ein elliptisches Integral erster Gattung, das sich nicht geschlossen auflösen lässt:

$$T = 4 \sqrt{\frac{l}{2g}} \int_0^{\phi_m} \frac{d\phi}{\sqrt{\cos\phi - \cos\phi_m}} = T_0 \cdot \frac{2}{\pi} K\left(\sin\frac{\phi_m}{2}\right)$$

wobei $T_0 = 2\pi\sqrt{l/g}$ die Schwingungsdauer für infinitesimale Amplituden ist. Mittels einer Taylor-Reihenentwicklung der Funktion $K$ lässt sich eine präzise Näherungsformel für die Praxis ableiten:

$$T \approx T_0 \left( 1 + \frac{1}{4}\sin^2\left(\frac{\phi_m}{2}\right) + \frac{9}{64}\sin^4\left(\frac{\phi_m}{2}\right) + \dots \right)$$

Für Winkel bis zu $\phi_m \approx 90^\circ$ reicht meist die erste Korrekturstufe aus, die oft auch vereinfacht als Borda-Formel geschrieben wird:

$$T \approx T_0 \left( 1 + \frac{\phi_m^2}{16} \right) \quad (\phi_m \text{ in Radiant})$$

##### Vergleichstabelle für die Laborpraxis (Aufgabe 1):

Die folgende Tabelle zeigt die Abweichungen zwischen der linearen Näherung und der exakten nichtlinearen Periodendauer, die Sie in Aufgabe 1 numerisch verifizieren können.

| Amplitude $\phi_m$ (grad) | Amplitude $\phi_m$ (rad) | Relativer Faktor $T/T_0$ | Abweichung zur harmonischen Schwingung |
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
*[Not yet translated]*



### Anhang I: Komplementäre Aufgabensammlung (Fortgeschrittenen-Niveau)

Die folgenden Zusatzaufgaben richten sich an Studierende höherer Semester und erfordern eine Kombination aus numerischer Simulation und analytischer Herleitung.

#### Aufgabe 7: Melnikov-Methode zur Chaos-Vorhersage

Für das getriebene Pendel lässt sich der Übergang von regulärer Dynamik zu chaotischem Verhalten näherungsweise analytisch eingrenzen. Die Melnikov-Methode untersucht das Schneiden der stabilen und instabilen Mannigfaltigkeiten (Separatrix-Splitting) unter dem Einfluss einer kleinen Störung (schwache Dämpfung $b$ und kleine Amplitude $A$).

1. Der kritische Zustand ist erreicht, wenn die Melnikov-Funktion $M(t_0)$ Nullstellen besitzt. Für das System (1.1.2) lautet die theoretische Bedingung für chaotische Ausreißer:
$$\frac{A}{b} \ge \frac{4g}{l \cdot \omega_A \cdot \cosh\left(\frac{\pi \omega_A}{2 \omega_0}\right)}$$


2. Überprüfen Sie diese analytische Grenze im Experimentierteil des Programms. Wählen Sie extrem kleine Werte für Dämpfung und Anregung und testen Sie, ob knapp unterhalb des kritischen Verhältnisses $A/b$ bereits chaotisches Verhalten detektiert werden kann.

#### Aufgabe 8: Untersuchung des fraktalen Einzugsgebiets

Koexistieren im System zwei Attraktoren (wie in Abschnitt 2.4, Abb. 2.4.3), entscheidet die Separatrix über das Schicksal der Trajektorie.

1. Nutzen Sie das Programm, um das Einzugsgebiet systematisch zu rastern. Variieren Sie dazu die Anfangsbedingungen $\phi_0$ im Bereich von $-180^\circ$ bis $+180^\circ$ und $\dot{\phi}_0$ im Bereich von $-5$ bis $+5$ in Schritten von $2^\circ$.
2. Markieren Sie manuell auf einem Millimeterpapier Punkte, die im kleinen Grenzzyklus enden, mit einem Kreuz und Punkte, die im großen Grenzzyklus enden, mit einem Kreis.
3. Analysieren Sie die Grenzlinie (Separatrix). Zeigt sie eine glatte Geometrie oder weist sie selbstähnliche, fraktale Strukturen auf? (Stichwort: *Fractal Basin Boundaries* [13]).

---

---



## Page 48
*[Not yet translated]*



### Anhang J: Verzeichnis der numerischen Experimente und Systemparameter

Für eine schnelle Reproduktion der im Lernteil abgedruckten Grafiken sind nachfolgend alle exakten Parameterwerte und die zugehörigen Masken-Konfigurationen tabellarisch zusammengestellt.

#### J.1 Standard-Konfigurationen für das mathematische Pendel

In allen Beispielen des ersten Kapitels wurden, sofern nicht explizit anders angegeben, die folgenden mechanischen Grundparameter verwendet:

* Masse des Pendels $m = 0.2\text{ kg}$
* Länge der masselosen Stange $l = 0.25\text{ m}$
* Trägheitsmoment $I = m \cdot l^2 = 0.0125\text{ kg}\cdot\text{m}^2$
* Eigenkreisfrequenz der Linearnäherung $\omega_0 = \sqrt{g/l} \approx 6.264\text{ s}^{-1}$

##### Übersicht der Simulations-Datensätze:

| Abbildung im Text | Dämpfung $b$ (Nms) | Treiber $A$ (Nm) | Frequenz $\omega_A$ (1/s) | Anfangswerte $(\phi_0, \Omega_0)$ | Beobachtetes Phänomen |
| --- | --- | --- | --- | --- | --- |
| **Abb. 2.2.1a** | $0.0000$ | $0.0000$ | $0.0000$ | $(10^\circ, 0.0)$ | Harmonische Schwingung, Periode konstant |
| **Abb. 2.2.1b** | $0.0000$ | $0.0000$ | $0.0000$ | $(120^\circ, 0.0)$ | Nichtlineare Verzerrung, Periode vergrößert |
| **Abb. 2.2.2** | $0.0000$ | $0.0000$ | $0.0000$ | $(179.9^\circ, 0.0)$ | Extremes Plateau in der Nähe des Sattelpunkts |
| **Abb. 2.3.1b** | $0.0200$ | $0.0000$ | $0.0000$ | $(150^\circ, 2.0)$ | Phasenraumkontraktion auf Fixpunkt-Attraktor |
| **Abb. 2.4.1b** | $0.0200$ | $0.2900$ | $4.1760$ | $(0^\circ, 0.0)$ | Transienter Einschwingvorgang auf T1-Grenzzyklus |
| **Abb. 2.5.2b** | $0.0400$ | $0.5350$ | $4.1760$ | $(10^\circ, 0.0)$ | Periodenverdopplung (2 Punkte im Poincaré-Schnitt) |
| **Abb. 2.5.4b** | $0.0400$ | $0.5500$ | $4.1760$ | $(0^\circ, 0.0)$ | Deterministisches Chaos, Seltsamer Attraktor |

---

---



## Page 49
*[Not yet translated]*



### Anhang K: Hinweise zur numerischen Präzision und Hardware-Einflüssen

Bei der Durchführung langandauernder chaotischer Simulationen (wie z.B. bei der Generierung des dichten Bifurkationsdiagramms in Abb. 2.6.1) kann es zu feinen Abweichungen zwischen den Ergebnissen verschiedener Computer kommen. Diese Eigenschaft ist im Wesentlichen keine Fehlfunktion der Software, sondern eine direkte Konsequenz der mathematischen Natur des Chaos.

#### K.1 Rundungsfehler-Verstärkung

Da im chaotischen Regime der Lyapunov-Exponent positiv ist ($\lambda > 0$), wird der Abstand zweier Trajektorien pro Zeiteinheit um den Faktor $e^{\lambda t}$ vergrößert. Dies gilt nicht nur für Abweichungen in den physikalischen Anfangsbedingungen (wie in Aufgabe 6), sondern auch für rein numerische Fehler.

Ein typischer PC berechnet Fließkommazahlen nach dem IEEE-754-Standard mit einer Genauigkeit von 64 Bit (Double Precision), was ca. 15-17 signifikanten Dezimalstellen entspricht. Der unvermeidbare Rundungsfehler beim kleinsten Integrationsschritt wird somit im chaotischen Bereich unaufhaltsam verstärkt. Nach einer charakteristischen Zeitdauer – der sogenannten **Lyapunov-Zeit** $t_L \approx 1/\lambda$ – ist der Fehler auf die Makroebene angewachsen. Ab diesem Moment beschreibt die berechnete Kurve nicht mehr die exakte physikalische Bahn des realen Systems, sondern eine sogenannte "Pseudotrajektorie".

> **Wichtiger Hinweis für die Lehre:**
> Dank des *Shadowing-Theorems* (Beschattungssatz) der Topologie ist das qualitative Ergebnis im Phasenraum (die fraktale Geometrie des seltsamen Attraktors und die statistischen Kennwerte) trotz der Rundungsfehler mathematisch absolut verlässlich. Es existiert für jede numerische Pseudotrajektorie eine echte, exakte Trajektorie zu leicht veränderten Anfangsbedingungen, die exakt denselben Pfad beschreibt.

---

---



## Page 50
*[Not yet translated]*



#### K.2 Einfluss des mathematischen Koprozessors (FPU)

Sollten Sie Berechnungen auf Systemen ohne Koprozessor unter Verwendung des Emulationsparameters `/E` (siehe Abschnitt IV.4) durchführen, nutzt die Software interne 32-Bit-Routinen zur Nachbildung der mathematischen Operationen.

Dies führt dazu, dass der Punkt des Umschlagens in eine chaotische Phase im Bifurkationsdiagramm im Vergleich zu Berechnungen mit einer echten Hardware-FPU (Intel 80387) minimal verschoben sein kann. Für quantitative Vergleiche in Versuchsprotokollen wird daher dringend empfohlen, alle Messreihen innerhalb einer Arbeitsgruppe auf baugleichen Rechnerarchitekturen durchzuführen.

---

### Verzeichnis der im Text erwähnten Programmdateien

* `SCHWING.EXE` – Das ausführbare Hauptprogramm (Simulationsumgebung).
* `SCHWING.OVR` – Overlay-Datei für die Speicherverwaltung unter MS-DOS.
* `EGAVGA.BGI` – Grafiktreiber für EGA- und VGA-Bildschirme.
* `LERN.TXT` – Online-Hilfe und Begleittext für den Lernteil.
* `SETUP.DAT` – Standard-Parameterdatei (wird automatisch generiert).
* `READ.ME` – Aktuelle Last-Minute-Hinweise zur Hardwarekompatibilität.

---

**Ende des technischen Anhangs.**
*Dieses Begleitmaterial ist integraler Bestandteil des Softwarepakets "Nichtlineare Dynamik".*
*Printed in Germany 1995.*

---



## Page 51
*[Not yet translated]*



### Anhang L: Ergänzende Grafiken zu den Simulationsmodellen

Die folgenden Abbildungen zeigen typische Bildschirmausgaben des Programms im hochauflösenden VGA-Modus, wie sie bei der Durchführung der Laborübungen (Kapitel II) aufgezeichnet werden können.

![Figure L.1: Phase portrait of the Duffing Oscillator showing the classic double-scroll chaotic attractor trajectory looping symmetrically between two main wells.]
Abb. L.1: Phasenportrait des Duffing-Oszillators im chaotischen Zustand (Harte Feder mit harmonischer Anregung, vgl. Aufgabe 4).
Systemparameter: $c = -1.0, d = 1.0, b = 0.3, A = 0.4, \omega_A = 1.4$.

![Figure L.2: Stroboskopische Abbildung (Poincaré-Schnitt) of the Duffing attractor, displaying highly resolved fractal filaments and stretching-and-folding structures.]
Abb. L.2: Stroboskopische Abbildung (Poincaré-Schnitt) zu der in Abb. L.1 gezeigten chaotischen Bewegung. Die fraktale Filamentstruktur des seltsamen Attraktors wird durch das Ausblenden der transienten Übergänge deutlich sichtbar.

---

---



## Page 52
*[Not yet translated]*



### Anhang M: Numerische Werte zur Nullstellenbestimmung

Bei der analytischen Berechnung von Fixpunkten und Bifurkationsgrenzen treten transzendente Gleichungen auf. Nachfolgend sind wichtige Referenzwerte für numerische Abgleichsroutinen gelistet.

#### M.1 Die ersten zehn Nullstellen der Besselfunktion erster Gattung $J_0(x)$

Diese Werte werden insbesondere bei der theoretischen Untersuchung von frequenzmodulierten Systemen und gekoppelten Oszillatoren als kritische Frequenzverhältnisse benötigt.

| Ordnung $n$ | Nullstelle $x_n$ | $J_1(x_n)$ | Ordnung $n$ | Nullstelle $x_n$ | $J_1(x_n)$ |
| --- | --- | --- | --- | --- | --- |
| **1** | $2.40482556$ | $+0.5191$ | **6** | $18.07106397$ | $-0.2051$ |
| **2** | $5.52007811$ | $-0.3403$ | **7** | $21.21163663$ | $+0.1903$ |
| **3** | $8.65372791$ | $+0.2715$ | **8** | $24.35247153$ | $-0.1784$ |
| **4** | $11.79153444$ | $-0.2325$ | **9** | $27.49347913$ | $+0.1686$ |
| **5** | $14.93091770$ | $+0.2114$ | **10** | $30.63460647$ | $-0.1603$ |

#### M.2 Die Feigenbaum-Konstanten (Universelle Skalenfaktoren)

Für Systeme, die über eine Kaskade von Periodenverdopplungen ins Chaos übergehen (Feigenbaum-Szenario, vgl. Abschnitt 2.6), gelten die folgenden universellen Grenzwerte:

* **Das Bifurkationsverhältnis ($\delta$):**
Bestimmt das exponentielle Verhältnis der Parameterintervalle zwischen aufeinanderfolgenden Verdopplungen:
$$\delta = \lim_{n \rightarrow \infty} \frac{\mu_n - \mu_{n-1}}{\mu_{n+1} - \mu_n} \approx 4.669201609102990$$


* **Der Skalenfaktor für die Pitchfork-Breite ($\alpha$):**
Beschreibt das Skalierungsverhalten der geometrischen Abstände der Bifurkationszweige:
$$\alpha = \lim_{n \rightarrow \infty} \frac{d_n}{d_{n+1}} \approx 2.502907875095892$$



---

---



## Page 53
*[Not yet translated]*



### Anhang N: Quellcode zur Daten-Konvertierung (ASCII-Export)

Die vom Simulationsprogramm generierten Binärdateien (`*.BIN`) können mit dem folgenden kleinen Hilfsprogramm in lesbare Textdateien (ASCII) umgewandelt werden, falls kein direkter Export über das Menü durchgeführt wurde.

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
  Write('Geben Sie den Namen der Binaerdatei ein (z.B. TRAJ.BIN): ');
  ReadLn(NameIn);
  Write('Geben Sie den Namen der Ausgabedatei ein (z.B. DATA.TXT): ');
  ReadLn(NameOut);
  
  Assign(InFile, NameIn);
  Reset(InFile);
  Assign(OutFile, NameOut);
  Rewrite(OutFile);
  
  WriteLn(OutFile, '# Zeit [s]', #9, 'Winkel [rad]', #9, 'Omega [rad/s]');
  
  While Not Eof(InFile) Do
  Begin
    Read(InFile, Rec);
    WriteLn(OutFile, Rec.Time:12:6, #9, Rec.Angle:12:6, #9, Rec.Omega:12:6);
  End;
  
  Close(InFile);
  Close(OutFile);
  WriteLn('Konvertierung erfolgreich abgeschlossen.');
End.

```

---

---



## Page 54
*[Not yet translated]*



### Anhang O: Kalibrierungsdaten für das Pohlsche Drehpendel

Für Anwender, die das experimentelle "Pohlsche Rad" im Labor betreiben (vgl. Anhang C), sind nachfolgend die Werksspezifikationen des Standardmodells aufgeführt. Diese Daten dienen als ideale Startkonfiguration für eine realitätsnahe Simulation.

#### O.1 Mechanische Abmessungen und Materialkonstanten

* Durchmeser des Kupfer-Drehrades: $D = 220\text{ mm}$
* Gesamtmasse des rotierenden Systems: $M = 0.385\text{ kg}$
* Trägheitsmoment der Kupferscheibe: $I_0 = 1.85 \cdot 10^{-3}\text{ kg}\cdot\text{m}^2$
* Richtgröße der Spiralfeder (Torsionsfederkonstante): $D^* = 0.0245\text{ Nm/rad}$
* Maximal zulässiger Verdrehwinkel: $\phi_{\max} = \pm 190^\circ$

#### O.2 Elektrische Spezifikationen der Wirbelstrombremse

Die Bremswirkung wird über den Stromfluss $I_B$ in den Feldspulen der Elektromagnete reguliert. Die Dämpfungskonstante $b$ verhält sich näherungsweise quadratisch zur angelegten Stromstärke:

$$b(I_B) \approx \kappa \cdot I_B^2,$$

wobei der Apparatekoeffizient für dieses Modell mit $\kappa \approx 0.0115\text{ Nms/A}^2$ bestimmt wurde.

##### Referenztabelle zur Dämpfungsjustierung:

| Bremsstrom $I_B$ (A) | Dämpfungskoeffizient $b$ (Nms) | Abklingkonstante $\gamma$ (1/s) | Charakter des Systems |
| --- | --- | --- | --- |
| `0.0` | $0.0002$ | $0.054$ | Fast ungedämpft |
| `0.2` | $0.0007$ | $0.189$ | Schwache Dämpfung |
| `0.5` | $0.0031$ | $0.838$ | Schwingfall (Praktikum) |
| `1.0` | $0.0117$ | $3.162$ | Starke Dämpfung |
| `1.5` | $0.0261$ | $7.054$ | Kriechgrenze erreicht |

---

---



## Page 55
*[Not yet translated]*



### Anhang P: Mathematische Ergänzungen zu nichtlinearen Potentialen

Das dynamische Verhalten eines ungedämpften, ungetriebenen Systems lässt sich direkt aus der Topologie seiner Potentiallandschaft $V(x)$ ableiten. Für ein eindimensionales System der Form $\ddot{x} = -\frac{dV}{dx}$ entspricht die Gesamtenergie einer Erhaltungsgröße.

#### P.1 Das Potential des Duffing-Oszillators

Die Bewegungsgleichung des freien Duffing-Oszillators lautet:

$$\ddot{x} + c \cdot x + d \cdot x^3 = 0$$

Das zugehörige mechanische Potential ergibt sich durch Integration zu:

$$V(x) = \int (c \cdot x + d \cdot x^3) dx = \frac{1}{2}c \cdot x^2 + \frac{1}{4}d \cdot x^4$$

Man unterscheidet je nach Vorzeichen der Parameter zwei fundamentale Fälle:

##### 1. Das "Harte Feder"-Potential ($c > 0, d > 0$)

Das Potential besitzt ein einzelnes, parabolisches Minimum im Ursprung ($x=0$). Die Rückstellkraft wächst überproportional mit der Auslenkung. Alle Trajektorien sind globale, geschlossene Schwingungen.

##### 2. Das "Doppelmulden-Potential" (*Double-Well*) ($c < 0, d > 0$)

Dieses System beschreibt eine elastische Knickstange oder ein inverses Pendel zwischen zwei Magneten. Der Ursprung $x=0$ wird zu einem lokalen Maximum (instabiler Sattelpunkt). Es entstehen zwei neue, symmetrische Minima (stabile Fixpunkte) bei:

$$x^*_{\pm} = \pm \sqrt{-\frac{c}{d}}$$

Trajektorien mit geringer Gesamtenergie oszillieren lokal in einer der beiden Mulden. Trajektorien mit hoher Energie kreuzen das zentrale Maximum und umschlingen beide Fixpunkte.

---

---



## Page 56
*[Not yet translated]*



### Anhang Q: Numerische Schrittweitensteuerung im Vergleich

Obwohl das Programm standardmäßig mit einer festen Schrittweite $dt$ operiert (vgl. Abschnitt IV.4), ist im mathematischen Modul die Option für ein adaptives Runge-Kutta-Fehlberg-Verfahren (RKF45) vorbereitet. Dies dient zur Kontrolle bei extrem steilen Gradienten im Phasenraum.

#### Q.1 Das Prinzip der eingebetteten Verfahren

Das RKF45-Verfahren berechnet pro Integrationsschritt zwei Approximationen unterschiedlicher Ordnung: eine Lösung $\vec{x}_{k+1}$ mit der Ordnung 4 und eine Kontrolllösung $\hat{\vec{x}}_{k+1}$ mit der Ordnung 5. Beide Berechnungen nutzen dieselben Steigungsvektoren $\vec{k}_i$, was den Rechenaufwand minimiert.

Der lokale Diskretisierungsfehler $\epsilon$ bestimmt sich aus der Differenz beider Lösungen:

$$\epsilon = \|\vec{x}_{k+1} - \hat{\vec{x}}_{k+1}\|$$

Liegt der Fehler oberhalb einer vorgegebenen Toleranzgrenze ($\epsilon > \text{Tol}_{\max}$), wird der aktuelle Rechenschritt verworfen und mit einer halbierten Schrittweite $dt_{\text{neu}} = dt/2$ wiederholt. Ist der Fehler extrem klein ($\epsilon < \text{Tol}_{\min}$), kann die Schrittweite für den nächsten Schritt verdoppelt werden, um Rechenzeit einzusparen.

#### Q.2 Konsequenzen für die stroboskopische Abbildung

Für die Generierung von Poincaré-Schnitten ist ein variables $dt$ problematisch, da die Abtastpunkte exakt äquidistant im Takt der Treiberperiode $T_A = 2\pi/\omega_A$ liegen müssen. Bei adaptiver Schrittweite muss das Programm daher an den Intervallgrenzen eine Interpolation (z.B. mittels kubischer Splines) durchführen, um den exakten Schnittpunkt mit der Phasenebene zu treffen. Dies erklärt, warum das feste RK4-Verfahren in der Programmpraxis oft bevorzugt wird.

---

---



## Page 57
*[Not yet translated]*



### Anhang R: Glossar englischer Fachbegriffe (Dictionary of Chaos)

Da die moderne Fachliteratur zur nichtlinearen Dynamik weitgehend in englischer Sprache verfasst ist, dient dieses kurze Glossar als Übersetzungshilfe für weiterführende Studien.

* **Attractor** $\rightarrow$ *Attraktor:* Eine Teilmenge des Phasenraums, auf welche alle Trajektorien aus einem bestimmten Einzugsgebiet für $t \rightarrow \infty$ hinsteuern.
* **Basin of Attraction** $\rightarrow$ *Einzugsgebiet:* Der Bereich von Anfangsbedingungen im Phasenraum, deren Trajektorien gegen denselben Attraktor konvergieren.
* **Bifurcation** $\rightarrow$ *Bifurkation / Verzweigung:* Eine qualitative Änderung des Systemverhaltens (z.B. Periodenverdopplung) bei der Variation eines Kontrollparameters.
* **Boundary** $\rightarrow$ *Grenzlinie:* Die Trennlinie im Phasenraum, beispielsweise zwischen zwei Einzugsgebieten (Separatrix).
* **Burst** $\rightarrow$ *Ausbruch:* Ein plötzlicher, unregelmäßiger chaotischer Abschnitt innerhalb einer intermittierenden Bewegung.
* **Driven / Forced Oscillator** $\rightarrow$ *Getriebener Oszillator:* Ein Schwingungssystem, das einer explizit zeitabhängigen, äußeren Kraft unterliegt.
* **Intermittency** $\rightarrow$ *Intermittenz:* Ein Weg ins Chaos, bei dem sich reguläre und chaotische Phasen unregelmäßig abwechseln.
* **Limit Cycle** $\rightarrow$ *Grenzzyklus:* Eine isolierte, geschlossene Trajektorie im Phasenraum eines dissipativen Systems, die einer periodischen Schwingung entspricht.
* **Map** $\rightarrow$ *Diskrete Abbildung:* Eine mathematische Gleichung, die den Systemzustand zu diskreten Zeitschritten beschreibt ($x_{k+1} = f(x_k)$).
* **Pitchfork Bifurcation** $\rightarrow$ *Stimmgabel-Bifurkation:* Typische Geometrie der Periodenverdopplung im Feigenbaum-Diagramm.
* **Quasiperiodic** $\rightarrow$ *Quasiperiodisch:* Eine Bewegung, die auf der Überlagerung inkommensurabler Frequenzen basiert.
* **Strange Attractor** $\rightarrow$ *Seltsamer Attraktor:* Ein Attraktor mit fraktaler Geometrie und empfindlicher Abhängigkeit von den Anfangsbedingungen.

---

---



## Page 58
*[Not yet translated]*



### Anhang S: Hinweise zur Lizenzierung und Vervielfältigung

Das diesem Begleitheft beigefügte Simulationsprogramm "Nichtlineare Schwingungen" ist urheberrechtlich geschützt. Für den Einsatz im Bildungsbereich gelten folgende Sonderregelungen.

#### S.1 Einzelplatzlizenz (Standard)

Die mitgelieferte Diskette berechtigt zur Installation und Nutzung des Programms auf genau einem Computersystem. Eine gleichzeitige Nutzung auf mehreren Rechnern oder das Bereitstellen in öffentlichen Datennetzen ohne Zusatzlizenz ist unzulässig.

#### S.2 Schullizenz / Campuslizenz

Für Schulen, Universitäten und Volkshochschulen kann beim Verlag eine kostengünstige Campuslizenz erworben werden. Diese berechtigt:

1. Zur Installation des Programms auf einer unbegrenzten Anzahl von Rechnern innerhalb der Liegenschaften der jeweiligen Institution.
2. Zur Bereitstellung auf lokalen Fileservern im Rahmen des EDV-gestützten Physikunterrichts.
3. Zur Vervielfältigung dieses Begleithefts als Kopiervorlage für den internen Gebrauch in Praktikumskursen.

> **Haftungsausschluss:**
> Der Entwickler und der Verlag übernehmen keine Haftung für Schäden, die direkt oder indirekt aus der Installation oder dem Betrieb dieser Software resultieren. Da es sich um ein hardwarenahes DOS-Programm handelt, erfolgt die Nutzung auf eigene Verantwortung des Anwenders.

---

---



## Page 59
*[Not yet translated]*



### Anhang T: System-Updates und Add-ons (Version 2.1)

Im Zuge der kontinuierlichen Produktpflege wurde das Programmpaket um zusätzliche mathematische Modelle erweitert, die in der ersten Auflage noch nicht dokumentiert waren.

#### T.1 Das van der Pol-System

Im Menü **System** lässt sich nun auch der van der Pol-Oszillator aktivieren. Die Differentialgleichung beschreibt ein System mit einer ortsabhängigen, nichtlinearen Dämpfung:

$$\ddot{x} - \epsilon(1 - x^2)\dot{x} + x = 0$$

##### Besondere Verhaltensweisen:

* Für kleine Amplituden ($x < 1$) ist der Dämpfungsterm negativ ($\epsilon(1-x^2) > 0$). Das System entzieht seiner Umgebung Energie und schwingt sich selbsttätig auf.
* Für große Amplituden ($x > 1$) wird die Dämpfung positiv und bremst das System ab.
* Unabhängig von den Anfangswerten kollabieren alle Trajektorien für $t \rightarrow \infty$ auf einen absolut stabilen, charakteristischen **Grenzzyklus** im Phasenraum. Dieses Modell dient in der Biophysik zur Beschreibung von Herzschlagrhythmen und Nervenimpulsen (FitzHugh-Nagumo-Modell).

#### T.2 Optimierter Grafik-Treiber für High-Resolution VGA

Durch eine Modifikation der Datei `EGAVGA.BGI` konnte die Bildwiederholfrequenz bei der On-Screen-Animation um ca. $25\%$ gesteigert werden. Rechner ab einer Taktfrequenz von $33\text{ MHz}$ (Intel 486DX) sind nun in der Lage, chaotische Trajektorien im Phasenraum in echter Echtzeit ohne Verzögerung zu zeichnen.

---

---



## Page 60
*[Not yet translated]*



### Anhang U: Stichwortverzeichnis für Quelltextvariablen

Für Programmierer, die den beigefügten Pascal-Quellcode modifizieren oder eigene Module ankoppeln möchten, sind hier die zentralen globalen Variablenbezeichner deklariert.

* `A_amp` (Real): Amplitude der äußeren Anregungskraft bzw. des Drehmoments [$Nm$].
* `b_damp` (Real): Globaler viskoser Dämpfungskoeffizient für lineare Reibung.
* `CurrentPageAddress` (Word): Segmentadresse des VGA-VRAMs für das Page-Flipping.
* `dt_step` (Real): Feste Zeitschrittweite der numerischen Integration (RK4).
* `g_grav` (Real): Die Schwerebeschleunigung (wird programmweit mit $9.81\text{ m/s}^2$ initialisiert).
* `I_moment` (Real): Trägheitsmoment des Pendelkörpers oder des Drehpendels.
* `l_length` (Real): Geometrische Länge der masselosen Pendelstange [$m$].
* `m_mass` (Real): Masse des schwingenden Körpers im Schwerpunkt [$kg$].
* `omega_A` (Real): Kreisfrequenz des periodischen Treibers (Eingabe in $Hz$ wird intern konvertiert).
* `Phi_pos` (Real): Der aktuelle Auslenkungswinkel im Bogenmaß.
* `Omega_vel` (Real): Die aktuelle Winkelgeschwindigkeit $\dot{\phi}$ [$rad/s$].
* `Time_elapsed` (Real): Die akkumulierte Simulationszeit seit dem Start des aktuellen Laufs.

---

**Ende des erweiterten Dokumentenanhangs.**
*Soft-Physics Distribution, Technical Support Department, Update 1996.*

---

Damit ist auch dieser Block von zehn Seiten vollständig transkribiert. Wenn Sie weitere Seiten haben, laden Sie diese einfach hoch!

---



## Page 61
*[Not yet translated]*



### Anhang V: Installations-Checkliste für den Laborbetrieb

Um einen reibungslosen Ablauf bei der Durchführung der Experimente im Praktikum zu garantieren, gehen Sie vor dem Eintreffen der Studierenden die folgende Checkliste durch.

#### V.1 Technische Vorbereitung der Arbeitsplätze

* [ ] **Betriebssystem-Ebene:** Überprüfen Sie, ob der Treiber `ANSI.SYS` in der Datei `CONFIG.SYS` geladen ist (`DEVICE=C:\DOS\ANSI.SYS`). Dieser wird für die korrekte farbliche Darstellung einiger Textmenüs zwingend benötigt.
* [ ] **Speicher-Konfiguration:** Stellen Sie sicher, dass mindestens $580\text{ KB}$ konventioneller DOS-Speicher frei sind. Nutzen Sie gegebenenfalls das Kommando `MEM /C`, um im oberen Speicherbereich (UMB) Platz zu schaffen (`DOS=HIGH,UMB`).
* [ ] **Grafik-Kompatibilität:** Überprüfen Sie die Grafikkarte durch Aufruf des kleinen Testprogramms `VGACHECK.EXE`. Sollte der Bildschirm dunkel bleiben, ersetzen Sie die `EGAVGA.BGI` im Programmverzeichnis durch den Standardtreiber der Borland-Bibliothek.
* [ ] **Maus-Treiber:** Laden Sie den residenten Maustreiber (z.B. `MOUSE.COM`) vor dem Start der Simulationsumgebung, da andernfalls keine interaktive Steuerung der Phasenraum-Fadenkreuze möglich ist.

#### V.2 Didaktische Vorbereitung

* [ ] Stellen Sie sicher, dass auf den lokalen Festplatten das Verzeichnis `C:\SCHWING\DATA\` existiert und für den aktuellen Benutzer schreibbar ist, damit numerische Ergebnisse für die spätere Auswertung gesichert werden können.
* [ ] Drucken Sie die Protokollvorlagen (Anhang C und I) in ausreichender Stückzahl aus.

---

---



## Page 62
*[Not yet translated]*



### Anhang W: Versionshistorie und Fehlerkorrekturen (Errata)

In diesem Abschnitt sind die wichtigsten Modifikationen und Fehlerbehebungen dokumentiert, die seit der ersten Veröffentlichung der Version 1.0 (Herbst 1994) in das Programmpaket eingepflegt wurden.

#### W.1 Version 1.1 (Frühjahr 1995)

* **Fehlerbehebung im RK4-Modul:** Ein Vorzeichenfehler bei der Berechnung des Terms der kubischen Rückstellkraft ($dx^3$) im Duffing-Modul wurde korrigiert. Dies führte in Version 1.0 bei extrem großen Amplituden zu einer fälschlichen Divergenz der Trajektorien ins Unendliche.
* **Erweiterung der Benutzeroberfläche:** Die Taste `F10` wurde global als "Masken-Bestätigung" implementiert, um den Workflow bei der Parameterstudie zu beschleunigen.

#### W.2 Version 2.0 (Herbst 1995)

* **Integration des Poincaré-Schnitts:** Das Modul zur Erzeugung stroboskopischer Abbildungen wurde vollständig neu geschrieben. Die Punkte werden nun nicht mehr als dicke Pixel, sondern als feine Einzelpunkte dargestellt, was die Auflösung fraktaler Strukturen (Filamente) erheblich verbessert.
* **Unterstützung für mathematische Koprozessoren:** Das Programm erkennt nun beim Bootvorgang automatisch, ob eine Intel 80387 FPU vorhanden ist, und schaltet dynamisch auf optimierten 32-Bit-Assemblercode um.

#### W.3 Aktuelle Version 2.1 (Januar 1996)

* Das van der Pol-System wurde als neues Standardmodell hinzugefügt (Dokumentation siehe Anhang T).
* Ein Speicherleck bei der fortlaufenden Generierung des Bifurkationsdiagramms (Überlauf des Grafikspeichers nach ca. 10.000 Iterationen) wurde vollständig behoben.

---

---



## Page 63
*[Not yet translated]*



### Anhang X: Bestellschein für Zusatzmodule und Updates

Sollten Sie Interesse an einer Erweiterung Ihres Simulationspakets oder an weiterführenden Lehrmaterialien haben, schneiden Sie diesen Schein aus und senden Sie ihn frankiert an den Verlag:

**Soft-Physics Publishing GmbH** *Abteilung für Lehrsoftware* *Schönhauser Allee 124* *D-10437 Berlin* ---

#### Ich/Wir bestellen hiermit fest:

* [ ] **Zusatzmodul "Gekoppelte Oszillatoren" (Version 1.0):** Erweiterung des Programms auf zwei über eine lineare Feder verbundene Pendelsysteme. Ermöglicht das Studium von Schwebungen, Energieaustausch und hochdimensionalem Chaos (Phasenraum-Dimension = 4).
*Preis für Einzelplatzlizenz: DM 49,– / Schullizenz: DM 129,–*
* [ ] **Begleitendes Dia-Set "Geometrie des Chaos":** 24 hochwertige Farbdias für den Vorlesungseinsatz. Enthält hochaufgelöste Renderings seltsamer Attraktoren (Lorenz-Attraktor, Rössler-Attraktor, Hénon-Abbildung) sowie reale Laboraufnahmen.
*Preis pro Set: DM 78,–*
* [ ] **Update-Service auf Version 2.2 (Lieferung auf 3.5" Diskette):** Beinhaltet das neue Modul zur Berechnung des fraktalen Einzugsgebiets (Fractal Basin Boundaries).
*Nur gegen Einsendung der Originaldiskette der Version 1.x / 2.0. Servicegebühr: DM 15,–*

##### Rechnungsanschrift / Stempel der Institution:

Name: ________________________________________

Institution/Schule: _______________________________

Straße / Hausnummer: ______________________________

PLZ / Ort: _______________________________________

Datum: ______________ Unterschrift: ___________________

---

**Ende des Hefts.**

---

