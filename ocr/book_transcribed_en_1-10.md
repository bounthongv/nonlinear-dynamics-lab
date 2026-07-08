
## Page 1

### Order and Chaos in Nonlinear Oscillations

#### Companion Booklet for the Computer Simulation Program

---

**Soft-Physics Publishing GmbH, Berlin 1995** *Author: Dr. rer. nat. Martin Schorn* *Version 2.1 for MS-DOS*

---

### Table of Contents

* **Chapter I: Physical Models and Foundations**
* 1. Introduction to Nonlinear Dynamics (p. 2)


* 2. The Mathematical Pendulum (p. 5)


* 3. The Duffing Oscillator and Pohl's Torsion Pendulum (p. 3)




* **Chapter II: Laboratory Guide for Numerical Experiments**
* 1. Experiment 1: Period Length as a Function of Amplitude (p. 10)


* 2. Experiment 2: Phase Portrait and Attractors (p. 11)


* 3. Experiment 3: Bifurcations and the Path to Chaos (p. 12)




* **Chapter III: Mathematical Background**
* 1. Phase Space and Phase Flow (p. 16)


* 2. Poincaré Maps and Fractal Structures (p. 19)





---

## Page 2

### Chapter I: Physical Models and Foundations

#### 1. Introduction to Nonlinear Dynamics

The classical physics of oscillations is largely based on the idealization of linear systems. A system is called linear if it satisfies the principle of superposition. This means that if $x_1(t)$ and $x_2(t)$ are two valid solutions of the system, then their linear combination

$$x(t) = \alpha \cdot x_1(t) + \beta \cdot x_2(t)$$

is also a solution. In reality, however, almost all physical systems are nonlinear. Nonlinearities arise from large deflection angles of a pendulum, non-proportional spring forces, or complex friction phenomena.

##### 1.1 Classification of Oscillating Systems

Oscillating systems can be categorized according to their properties and the nature of the forces acting upon them:

* **Autonomous Systems:** The governing differential equations do not explicitly depend on time. The system oscillates freely after an initial excitation.
* **Non-autonomous Systems:** The system is subject to an explicitly time-dependent external force, such as a periodic driving force (harmonic excitation).
* **Conservative Systems:** There is no loss of energy due to friction or damping. The total energy remains constant over time.
* **Dissipative Systems:** Energy is continuously dissipated due to frictional forces (e.g., sliding friction, viscous damping). These systems tend toward stationary states, so-called attractors.

---

## Page 3

#### 2. The Mathematical Pendulum

The simplest example of a nonlinear mechanical system is the mathematical pendulum (rigid pendulum). It consists of a point mass $m$ attached to a mass-less rod of length $l$, which can rotate in a vertical plane.

![Figure 1.1: Schematic diagram of a mathematical pendulum suspended from a fixed pivot, showing mass m, length l, deflection angle phi, and gravitational force mg.]

> **Figure 1.1: Schematic diagram of a mathematical pendulum.** > *Description:* A schematic vector diagram showing a pendulum suspended from a fixed ceiling pivot. The rod has length $l$ and is deflected at an angle $\phi$ relative to the vertical axis. The gravitational force acting vertically downward on the mass $m$ is split into a radial component along the rod ($mg \cos\phi$) and a tangential restoring component ($mg \sin\phi$).

Applying Newton's second law for rotational motion yields the equation of motion:

$$I \cdot \ddot{\phi} + m \cdot g \cdot l \cdot \sin\phi = 0$$

where $I = m \cdot l^2$ represents the moment of inertia of the point mass, and $g$ is the acceleration due to gravity ($9.81\text{ m/s}^2$). Dividing by $I$ simplifies the equation to:

$$\ddot{\phi} + \frac{g}{l} \sin\phi = 0$$

The nonlinearity of this equation is rooted in the term $\sin\phi$. Only for very small deflections ($\phi \ll 1\text{ rad}$) can the sine function be approximated by its linear Taylor expansion ($\sin\phi \approx \phi$). This yields the well-known linear differential equation of the harmonic oscillator.

---

## Page 4

#### 3. The Duffing Oscillator and Pohl's Torsion Pendulum

While the mathematical pendulum possesses a restoring force governed by the sine function, the Duffing oscillator models a system with a cubic nonlinear restoring force. It is often used to describe real mechanical springs that exhibit "hardening" or "softening" characteristics under large deformations.

The differential equation of the forced, damped Duffing oscillator is given by:

$$m \cdot \ddot{x} + b \cdot \dot{x} + c \cdot x + d \cdot x^3 = A \cdot \cos(\omega_A \cdot t)$$

where:

* $b$ is the viscous damping coefficient,
* $c$ represents the linear spring constant,
* $d$ denotes the cubic nonlinearity parameter (for $d > 0$ the spring hardens),
* $A$ and $\omega_A$ specify the amplitude and angular frequency of the external driver.

##### 3.1 Real Experimentation: Pohl's Torsion Pendulum

In physics laboratories, nonlinear dynamics is frequently demonstrated using a Pohl's torsion pendulum. It consists of a copper wheel mounted on a bearing, connected to a spiral torsion spring.

An adjustable electromagnetic eddy current brake provides variable dissipative damping. A DC motor with an eccentric link applies a periodic external torque. By mounting an additional eccentric mass (a small unsymmetrical weight) onto the wheel, a highly nonlinear gravitational restoring force is superimposed, allowing the transition from regular oscillations to deterministic chaos to be studied experimentally.

---

## Page 5

### Chapter II: Laboratory Guide for Numerical Experiments

The following laboratory assignments are designed to be performed interactivly using the computer simulation program "Nichtlineare Schwingungen" (Nonlinear Oscillations).

#### 1. Experiment 1: Period Length as a Function of Amplitude

##### Objective:

To investigate the breakdown of the small-angle approximation ($\sin\phi \approx \phi$) for the mathematical pendulum and to determine the amplitude dependence of the period length $T$.

##### Program Setup:

* **System:** Mathematical Pendulum (free, unforced)
* **Parameters:** Length $l = 0.25\text{ m}$, Mass $m = 0.2\text{ kg}$, Dämpfung (Damping) $b = 0.0\text{ Nms}$ (conservative system)
* **Rechnung (Calculation):** Step size $dt = 0.01\text{ s}$, Total time $t_{\max} = 10.0\text{ s}$

##### Procedure:

1. Open the **Anfangswerte (Initial Values)** input mask. Set the initial angular velocity $\Omega_0 = 0.0\text{ rad/s}$.
2. Perform consecutive simulation runs with the following initial deflection angles $\phi_0$: $5^\circ$, $20^\circ$, $45^\circ$, $90^\circ$, and $150^\circ$.
3. Measure the time between three consecutive zero crossings in the **Zeitverlauf (Time History)** graphic window to determine the exact period length $T$.
4. Record your measured values in a table and compare them with the theoretical period of the idealized linear harmonic oscillator:
$$T_0 = 2\pi \sqrt{\frac{l}{g}} \approx 1.003\text{ s}.$$



---

## Page 6

#### 2. Experiment 2: Phase Portrait and Attractors

##### Objective:

To understand the geometric representation of a motion in phase space and to analyze the differences between conservative trajectories and dissipative attractors.

##### Theory Briefing:

The state of a mechanical system with one degree of freedom is completely defined at any instant by its position $\phi$ and its velocity $\Omega = \dot{\phi}$. The coordinate system spanned by these two variables is called **Phase Space** (or phase plane).

##### Procedure part A (Conservative System):

1. Choose the free mathematical pendulum without damping ($b = 0.0$).
2. Set the display mode to **Phasenraum (Phase Space)**.
3. Start several calculations with different initial values:
* **Case A:** Small oscillations near the bottom equilibrium ($\phi_0 = 10^\circ, \Omega_0 = 0.0$).
* **Case B:** Large oscillations ($\phi_0 = 120^\circ, \Omega_0 = 0.0$).
* **Case C:** Rotational motion where the pendulum loops around the top pivot continuously ($\phi_0 = 0^\circ, \Omega_0 = 8.0\text{ rad/s}$).



Sketch the resulting curves. Note that for conservative systems, the trajectories form closed loops (orbits) or infinite wavy lines that never intersect.

---

## Page 7

##### Procedure part B (Dissipative System / Attractors):

Now introduce energy dissipation into the system by changing the parameters.

1. Set the damping coefficient to a non-zero value: $b = 0.02\text{ Nms}$.
2. Repeat the calculations using the exact same initial values as in part A ($\phi_0 = 10^\circ, 120^\circ$, and $\Omega_0 = 8.0$).
3. Observe how the trajectories behave over a longer simulation time ($t_{\max} = 30.0\text{ s}$).

![Figure 2.3.1: Phase space plots comparing a conservative system with closed orbits to a dissipative system where trajectories spiral down into a stable focal point.]

> **Figure 2.3.1: Comparison of phase portraits.** > *Description:* Two side-by-side two-dimensional phase plane plots ($\phi$ on the x-axis, $\Omega$ on the y-axis).
> * **Left Plot (a):** A family of concentric closed elliptical curves representing periodic conservative oscillations around the center $(0,0)$, bounded by a distinct wavy line (separatrix).
> * **Right Plot (b):** Inward-spiraling trajectories starting from various initial conditions, all converging toward the origin $(0,0)$, illustrating a stable focus or point attractor.
> 
> 

##### Evaluation:

Describe the observations in your lab report. Explain why the open paths from part A turn into spirals that all terminate at the origin $(0,0)$. This point is the simplest form of an **Attractor** (a stable fixed point).

---

## Page 8

#### 3. Experiment 3: Bifurcations and the Path to Chaos

##### Objective:

To observe the phenomenon of period doubling (Feigenbaum scenario) in a periodically driven, nonlinear pendulum and to document the transition to deterministic chaos.

##### Program Setup:

* **System:** Forced Mathematical Pendulum with Damping.
* **Parameters:** $l = 0.25\text{ m}$, $m = 0.2\text{ kg}$, Damping $b = 0.04\text{ Nms}$.
* **Driver:** Angular frequency $\omega_A = 4.176\text{ s}^{-1}$ (This corresponds to a frequency ratio of $\omega_A / \omega_0 \approx 2/3$).
* **Initial Values:** $\phi_0 = 0.0\text{ rad}$, $\Omega_0 = 0.0\text{ rad/s}$ (Start from rest).

##### Procedure:

In this experiment, the amplitude of the external driving torque $A$ serves as the control parameter. We will systematically increase $A$ and analyze the stationary response after transient oscillations have died out.

1. **Step 1 (Period 1 Schwingung):** Set $A = 0.250\text{ Nm}$. Start the simulation and look at the time history. After a short transient phase, a regular periodic oscillation establishes itself. Its period length matches the driver period $T_A = 2\pi / \omega_A$.
2. **Step 2 (Periodenverdopplung - Periode 2):** Increase the driving amplitude to $A = 0.535\text{ Nm}$. Observe the phase portrait. The trajectory no longer closes after a single loop, but requires two full cycles of the driver before repeating.

---

## Page 9

3. **Step 3 (Further Doubling):** Carefully increase the control parameter further to $A = 0.545\text{ Nm}$. You can observe a Period-4 oscillation. The system requires four driver cycles to return to its exact starting coordinates in the phase plane.
4. **Step 4 (Deterministic Chaos):** Now change the parameter to $A = 0.550\text{ Nm}$.

![Figure 2.5.4: Chaotic phase portrait of a forced pendulum showing an intricate, non-repeating web of trajectories that fill a region of phase space.]

> **Figure 2.5.4: Chaotic phase portrait.** > *Description:* A continuous two-dimensional phase space plot ($\phi$ vs $\Omega$) displaying a complex, dense, and irregular web of overlapping trajectories. The curve does not settle into a single closed loop, but spans an intricate geometric shape over time, demonstrating a chaotic trajectory.

##### Task:

Describe the graph in Figure 2.5.4. Does the motion look periodic? Switch the display to **Stroboskop (Poincaré Map)**. Instead of a continuous line, you will see discrete points plotted at intervals of $t = k \cdot T_A$. Note how these points form a highly structured, fractal geometry.

---

## Page 10

### Chapter III: Mathematical Background

#### 1. Phase Space and Phase Flow

A fundamental method for analyzing nonlinear dynamics is transforming a single high-order differential equation into a system of coupled first-order differential equations.

For the driven damped pendulum, the second-order equation:

$$\ddot{\phi} + \frac{b}{I}\dot{\phi} + \frac{mgl}{I}\sin\phi = \frac{A}{I}\cos(\omega_A t)$$

is rewritten by defining the angular velocity $\Omega = \dot{\phi}$ as a separate state variable:

$$\begin{aligned}
\dot{\phi} &= \Omega \\
\dot{\Omega} &= -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi + \frac{A}{I}\cos(\omega_A t)
\end{aligned}$$

This state vector $\vec{x}(t) = (\phi(t), \Omega(t))$ defines a point in the phase plane. As time progresses, this point moves along a path called a trajectory.

Because the system is non-autonomous (explicitly dependent on the time $t$ via the cosine term), two trajectories could cross in the two-dimensional $(\phi, \Omega)$ plane if they pass through the same point at different times. To restore uniqueness and prevent intersections, time is introduced as a third independent coordinate by defining a phase angle $\psi = \omega_A t \pmod{2\pi}$. This creates a three-dimensional autonomous phase space $(\phi, \Omega, \psi)$.
