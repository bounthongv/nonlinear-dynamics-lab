# Ordnung und Chaos bei nichtlinearen Schwingungen
*English Translation*

---

## Page 1

### Order and Chaos in Nonlinear Oscillations

#### Companion Booklet for the Computer Simulation Program

---

**Soft-Physics Publishing GmbH, Berlin 1995** *Author: Dr. Bounthong VONGXAYA* *Interactive Web Edition 2026*

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

---

## Page 9

3. **Step 3 (Further Doubling):** Carefully increase the control parameter further to $A = 0.545\text{ Nm}$. You can observe a Period-4 oscillation. The system requires four driver cycles to return to its exact starting coordinates in the phase plane.
4. **Step 4 (Deterministic Chaos):** Now change the parameter to $A = 0.550\text{ Nm}$.

![Figure 2.5.4: Chaotic phase portrait of a forced pendulum showing an intricate, non-repeating web of trajectories that fill a region of phase space.]

> **Figure 2.5.4: Chaotic phase portrait.** > *Description:* A continuous two-dimensional phase space plot ($\phi$ vs $\Omega$) displaying a complex, dense, and irregular web of overlapping trajectories. The curve does not settle into a single closed loop, but spans an intricate geometric shape over time, demonstrating a chaotic trajectory.

##### Task:

Describe the graph in Figure 2.5.4. Does the motion look periodic? Switch the display to **Stroboskop (Poincaré Map)**. Instead of a continuous line, you will see discrete points plotted at intervals of $t = k \cdot T_A$. Note how these points form a highly structured, fractal geometry.

---

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

---

## Page 11

#### 2. Poincaré Maps and Fractal Structures

When analyzing chaotic trajectories in three-dimensional phase space, continuous plots often look like a confusing, dense tangle of lines (as seen in Figure 2.5.4). To reveal the underlying geometric order, Henri Poincaré introduced a method of discretization known as the **Poincaré Map**.

Instead of tracking the continuous state vector $\vec{x}(t)$, we only sample the position and velocity at discrete intervals that match the period of the external driving force:

$$t_k = t_0 + k \cdot T_A = t_0 + k \cdot \frac{2\pi}{\omega_A} \quad \text{with } k = 0, 1, 2, \dots$$

This technique cuts through the continuous three-dimensional phase space flow using a stroboscopic two-dimensional plane at a fixed phase $\psi_0$.

##### Geometric Interpretation:

* For a **Period-1 oscillation**, the trajectory hits the plane at the exact same location every cycle. The Poincaré map consists of a **single point**.
* For a **Period-$N$ oscillation** (after period doubling), the map displays exactly **$N$ discrete points**.
* For **chaotic motion**, the points neither repeat nor fill the plane randomly. Instead, they trace out an infinite, highly organized pattern with a fine, layered appearance known as a **Strange Attractor**.

---

---

## Page 12

#### 3. Dissipative Dynamics and Phase Space Kontraktion

A key difference between conservative and dissipative systems is how volume changes in phase space. According to Liouville's theorem, the phase space volume of a conservative system remains strictly constant during flow. In contrast, dissipative systems experience a continuous shrinkage of phase space volume.

Let us consider a small volume element $V(t)$ containing a cloud of initial conditions. The rate of volume contraction can be determined by the divergence of the system's vector field $\vec{F}(\phi, \Omega)$:

$$\Lambda = \text{div} \vec{F} = \frac{\partial \dot{\phi}}{\partial \phi} + \frac{\partial \dot{\Omega}}{\partial \Omega}$$

Substituting the equations for the damped pendulum (from page 10):

$$\Lambda = \frac{\partial (\Omega)}{\partial \phi} + \frac{\partial}{\partial \Omega} \left( -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi + \frac{A}{I}\cos(\omega_A t) \right) = 0 - \frac{b}{I} = -\frac{b}{I}$$

Since the damping coefficient $b$ and the moment of inertia $I$ are positive constants, the divergence is always negative:

$$\text{div} \vec{F} = -\frac{b}{I} < 0$$

This means that any initial phase space volume shrinks exponentially over time at a constant rate:

$$V(t) = V(0) \cdot e^{-\frac{b}{I}t}$$

Consequently, all trajectories are pulled toward a lower-dimensional subspace of the phase space—the **Attractor**.

---

---

## Page 13

### Chapter IV: Software Architecture and Numerical Methods

#### 1. The Fourth-Order Runge-Kutta Method (RK4)

Since nonlinear differential equations cannot be solved analytically in closed form, the simulation program relies on numerical integration. The core engine utilizes the classical fourth-order Runge-Kutta method (RK4), which balances computational efficiency with high numerical precision.

Given a system of first-order differential equations $\dot{\vec{y}} = \vec{f}(t, \vec{y})$, the state vector $\vec{y}_{n+1}$ at the next time step $t_{n+1} = t_n + dt$ is calculated using four intermediate slope approximations:

$$\begin{aligned}
\vec{k}_1 &= \vec{f}(t_n, \vec{y}_n) \\
\vec{k}_2 &= \vec{f}\left(t_n + \frac{dt}{2}, \vec{y}_n + \frac{dt}{2}\vec{k}_1\right) \\
\vec{k}_3 &= \vec{f}\left(t_n + \frac{dt}{2}, \vec{y}_n + \frac{dt}{2}\vec{k}_2\right) \\
\vec{k}_4 &= \vec{f}(t_n + dt, \vec{y}_n + dt\vec{k}_3)
\end{aligned}$$

The final weighted average step is computed as:

$$\vec{y}_{n+1} = \vec{y}_n + \frac{dt}{6} \left( \vec{k}_1 + 2\vec{k}_2 + 2\vec{k}_3 + \vec{k}_4 \right)$$

The local truncation error of this method scales with the fifth power of the step size ($O(dt^5)$), while the global accumulation error scales as $O(dt^4)$. For the default step size of $dt = 0.01\text{ s}$, this guarantees sufficient numerical stability over typical simulation runs.

---

---

## Page 14

#### 2. Implementation in Borland Turbo Pascal 7.0

The simulation package was implemented as a high-performance, compiled desktop application under MS-DOS. Turbo Pascal 7.0 was chosen because it allows for direct hardware access, low-level graphics programming via the Borland Graphics Interface (BGI), and highly efficient execution routines.

##### Key Architectural Features:

* **Object-Oriented Design:** The various physical models (Pendulum, Duffing Oscillator, van der Pol) are implemented as child objects inheriting from a base virtual `TOscillator` class. This simplifies expanding the software with new systems.
* **Real-Time Graphics:** Instead of calculating entire datasets beforehand and displaying them statically, the RK4 algorithm and VGA pixel-rendering routines run concurrently inside the main program loop. This allows you to watch the trajectories develop in real time.
* **Floating-Point Optimization:** The software supports native execution modes utilizing an 8087/80387 mathematical coprocessor (FPU) via the compiler directive `{$N+,G+}`. This dramatically reduces computation times for dense bifurcation tracks.

---

---

## Page 15

#### 3. Memory Structure and Real-Mode Constraints

Because the software runs as a real-mode MS-DOS application, it operates under the strict conventional memory limit of $640\text{ KB}$ (the "640 KB Barrier"). To prevent running out of memory during long-term simulations with massive datasets, the software uses a dynamic ring buffer structure.

```
+-----------------------------------------------------------+
|               Conventional Memory (Max 640 KB)            |
+---------------------+-------------------+-----------------+
| System & BGI Driver | Code Segments     | Dynamic Heap    |
| (approx. 95 KB)     | (approx. 210 KB)  | (Ring Buffer)   |
+---------------------+-------------------+-----------------+
                                                   |
                      +----------------------------+
                      v
         [Pos_0] -> [Pos_1] -> [Pos_2] -> ... -> [Pos_Max]
            ^                                         |
            +-----------------------------------------+

```

Instead of saving every calculated floating-point value to a standard array, data points are continuously fed into a dynamic heap structure. Once the maximum buffer capacity is reached, the oldest data coordinates are automatically overwritten by the latest time steps. For long-term analytical tracking (e.g., generating high-resolution Poincaré maps with over $50,000$ points), the software bypasses RAM constraints by streaming data directly to the local hard drive as a binary file (`*.BIN`).

---

---

## Page 16

#### 4. The Parameter Configuration File (`SETUP.DAT`)

To make the program easier to use in a physics lab, all physical parameters, window boundaries, and calculation preferences are saved automatically when exiting the application. This data is stored in a structured configuration file named `SETUP.DAT`.

##### Internal Structure of the Configuration File:

The file is structured as a sequential binary record. If it gets corrupted or deleted, the program automatically generates a fresh copy containing the standard factory defaults on next startup.

```pascal
Type
  SetupRecord = Record
    SystemType : Byte;       { 1=Pendulum, 2=Duffing, 3=Pohl }
    Mass       : Real;       { Mass parameter in kg }
    Length     : Real;       { Oscillator length in m }
    Damping    : Real;       { Friction coefficient b }
    DriveAmp   : Real;       { Driver amplitude A }
    DriveFreq  : Real;       { Driver frequency in Hz }
    StepSize   : Real;       { RK4 integration step dt }
    XWindowMin : Real;       { Minimum value for graphic X-axis }
    XWindowMax : Real;       { Maximum value for graphic X-axis }
    YWindowMin : Real;       { Minimum value for graphic Y-axis }
    YWindowMax : Real;       { Maximum value for graphic Y-axis }
  End;

```

---

---

## Page 17

### Chapter V: User Interface and Operation

The program features a character-based menu interface with real-time VGA graphics output. Navigation is performed using either the keyboard cursor keys or a Microsoft-compatible mouse driver.

#### 1. The Main Screen Layout

After launching `SCHWING.EXE`, the screen splits into three main functional zones:

```
+-----------------------------------------------------------+
| [F1] Help   [F2] System   [F3] Parameters   [F4] Run   [ESC] | <- Menu
+-----------------------------------------------------------+
|                                                           |
|                                                           |
|                     Graphic Viewport                      |
|                  (Time Plot / Phase Space)                |
|                                                           |
|                                                           |
+-----------------------------------------------------------+
| State: Idle   | t: 0.00 s   | phi: 0.000   | omega: 0.000 | <- Status
+-----------------------------------------------------------+

```

* **The Top Menu Bar:** Gives quick access to setup dialogs, selection masks, file import/export options, and help modules.
* **The Central Graphic Viewport:** Displays the active numerical tracking using standard $640 \times 480$ pixel VGA graphics.
* **The Bottom Status Bar:** Shows real-time readouts of current physical parameters and variables during execution.

---

---

## Page 18

#### 2. Keyboard Control and Hotkeys

To ensure quick operation during experiments, the most important commands can be triggered directly via functional hotkeys:

| Key / Shortcut | Action within the Simulation |
| --- | --- |
| **`[F1]`** | Opens the context-sensitive help system. |
| **`[F2]`** | Selection menu for physical models. |
| **`[F3]`** | Opens the parameter configuration input mask. |
| **`[F4]`** | Starts the active simulation run. |
| **`[F5]`** | Switches graphics view (Time Series $\leftrightarrow$ Phase Space). |
| **`[F6]`** | Clears the active graphic screen without resetting parameters. |
| **`[Space]`** | Pauses the running calculation; pressing it again resumes. |
| **`[ESC]`** | Aborts the active simulation run or exits the current menu. |

##### Fine-Tuning Scale Coordinates:

While a simulation is running, you can change the viewport scale on the fly. Pressing the **`+`** or **`-`** keys zooms the active window coordinate limits in or out by a factor of $10\%$, making it easy to center tracking behaviors that move wide of the initial window settings.

---

---

## Page 19

#### 3. Data Export for Spreadsheet Utilities

For generating professional lab reports, the software allows you to export calculated data points as standard text formats. This lets you import your simulation results into common spreadsheet utilities (like Lotus 1-2-3, Borland Quattro Pro, or Microsoft Excel).

##### Steps to Export Data:

1. After completing or stopping a simulation run, press **`[ESC]`** to return to the main menu.
2. Navigate to **File** $\rightarrow$ **Export ASCII Data**.
3. A file dialog box will appear. Enter a valid DOS filename (maximum of 8 characters plus the extension, e.g., `LAB_01.TXT`).
4. The program writes a tab-delimited text file containing three columns:

```text
Time       Phi        Omega
0.000000   0.174533   0.000000
0.010000   0.174312   -0.044123
0.020000   0.173650   -0.088114

```

> **Caution:** If a file with the chosen name already exists in the workspace directory, it will be overwritten without warning.

---

---

## Page 20

#### 4. Command Line Parameters on Startup

The execution behavior of `SCHWING.EXE` can be adapted to your computer's hardware configuration using optional command-line switches when starting the program from the DOS prompt.

##### Syntax:

`C:\> SCHWING.EXE [/S] [/VGA] [/E] [/P]`

##### Available Switches:

* **`/S` (Silent Mode):** Bypasses the startup splash screen and audio signals, launching straight into the simulation dashboard.
* **`/VGA` (Force VGA Standard):** Disables automatic graphics hardware detection and forces the program into standard $640 \times 480$ pixel 16-color VGA mode. Use this option if your display stays black due to an incompatible SVGA card.
* **`/E` (Emulate FPU):** Disables native 80387 coprocessor detection and forces 8086 software floating-point emulation instead. This is helpful for testing software stability on older computers (like Intel 80286 systems without a math coprocessor).
* **`/P` (Print Screen Setup):** Swaps the screen palette background from black to crisp white. This saves ink when capturing screenshots for lab reports using the DOS utility `GRAPHICS.COM`.

---

**End of Chapter V.**

---

## Page 21

#### 5. Verification of the Superposition Principle

##### Objective:

To experimentally demonstrate that the principle of superposition applies strictly to linear systems but breaks down completely in the presence of nonlinearities.

##### Program Setup:

* **System:** Duffing Oszillator
* **Parameters:** Mass $m = 1.0\text{ kg}$, Damping $b = 0.1\text{ Nms}$.
* **Configuration A (Linear Case):** Set $c = 1.0$, $d = 0.0$ (Purely linear spring mechanism).
* **Configuration B (Nonlinear Case):** Set $c = 1.0$, $d = 0.5$ (Hardening spring mechanism).

##### Procedure:

1. Run a simulation using Configuration A with initial conditions $\vec{x}_1(0) = (1.0, 0.0)$ and save the trajectory data as `LIN1.DAT`.
2. Run a second simulation with initial conditions $\vec{x}_2(0) = (0.5, 2.0)$ and save it as `LIN2.DAT`.
3. Run a third simulation combining both initial conditions: $\vec{x}_3(0) = \vec{x}_1(0) + \vec{x}_2(0) = (1.5, 2.0)$, saving it as `LIN3.DAT`.
4. Use the built-in analysis tool to plot the algebraic sum curve $\vec{x}_{\text{sum}}(t) = \vec{x}_1(t) + \vec{x}_2(t)$ against the calculated path $\vec{x}_3(t)$. Note that they match perfectly.
5. Now repeat the entire sequence using Configuration B (the nonlinear setup).

##### Evaluation:

Document the clear deviation between the combined solution and the sum of individual solutions in the nonlinear case. Explain why adding state vectors fails when the governing differential equations contain higher-order power terms like $x^3$.

---

---

## Page 22

### Chapter VI: Advanced Nonlinear Phenomena

#### 1. Resonance Curve Distortion and Jump Phenomena

In linear systems, the steady-state amplitude of a forced oscillator plotted against driving frequency yields a symmetrical resonance curve. For nonlinear systems like the Duffing oscillator, this curve deforms significantly.

![Figure 3.1.2: Resonance curve of a hardening Duffing oscillator bending to the right, showing hysteresis loops and sudden amplitude jumps at critical frequencies.]

> **Figure 3.1.2: Hysteresis and jump phenomena.** > *Description:* A plot showing response amplitude on the y-axis against driving frequency $\omega_A$ on the x-axis. The resonance peak bends sharply to the right (higher frequencies) due to a hardening spring effect ($d > 0$). Arrows indicate a path: upward frequency sweeps cause the amplitude to follow the top curve until a critical drop point, while downward sweeps follow a lower curve before jumping up, establishing a clear hysteresis loop.

As shown in Figure 3.1.2, the resonance peak bends toward higher frequencies for a hardening spring mechanism ($d > 0$). This tilt creates a bistable frequency band where two distinct stable oscillation amplitudes can exist under identical physical parameters.

Which state the system settles into depends entirely on its past trajectory. Sweeping the driving frequency upward causes a sudden, catastrophic drop in amplitude at a upper threshold frequency. Sweeping downward causes a sudden jump back up at a lower threshold frequency.

---

---

## Page 23

#### 2. Subharmonic Oscillations and Frequency Entrainment

A fascinating feature of nonlinear driven systems is their ability to respond at frequencies completely different from the external driver. In linear systems, transient states die out, leaving a steady-state response that oscillates exclusively at the driving frequency $\omega_A$.

In nonlinear regimes, however, the system can display **subharmonic resonance**. This means the oscillator's response locks into a rational fraction of the driving frequency:

$$\omega_{\text{resp}} = \frac{p}{q} \cdot \omega_A \quad \text{with } p, q \in \mathbb{N}$$

##### Frequency Entrainment (Injection Locking):

When a nonlinear oscillator with its own natural frequency $\omega_0$ is driven by an external signal close to a harmonic or subharmonic frequency, it does not generate beats as a linear system would. Instead, the intrinsic frequency shifts and locks tightly onto the external driver. This self-synchronization boundary forms a classic geometric pattern in parameter space known as an **Arnold Tongue**.

---

---

## Page 24

### Chapter VII: Troubleshooting and FAQ

#### 1. Numerical Divergence ("Floating Point Overflow")

##### Symptom:

During a simulation run, the graphic computation halts abruptly, and a DOS error message appears: `Runtime error 200: Division by zero` or `Runtime error 205: Floating point overflow`.

##### Cause:

The integration step size $dt$ chosen for the Runge-Kutta algorithm is too large for the current steepness of the system's potential energy landscape. If the state coordinates land in a steep region of a hardening spring or near the vertical flip point of a pendulum, a step that is too large can overshoot violently, leading to a non-physical explosion of kinetic energy.

##### Solution:

* Open the **Parameters** mask (`[F3]`) and reduce the integration step size $dt$ (e.g., from $0.01\text{ s}$ down to $0.002\text{ s}$).
* Alternatively, lower the total energy of your system by reducing the initial deflection angles or the external driving amplitude $A$.

---

---

## Page 25

#### 2. Graphical Distortion on SVGA Monitors

##### Symptom:

The text interface renders correctly, but as soon as a plot starts drawing, the screen becomes garbled, flickers wildly, or goes completely blank.

##### Cause:

The standard Borland Graphics Interface driver `EGAVGA.BGI` included with the program utilizes hardware registers specific to authentic IBM VGA configurations. Modern high-performance SVGA controllers or VESA-compliant graphic cards sometimes implement legacy VGA modes with non-standard timing parameters.

##### Solution:

* Quit the program using **`[ESC]`**.
* Relaunch the simulator from the DOS prompt by explicitly appending the compatibility switch: `SCHWING.EXE /VGA` (see Chapter V.4).
* If the error persists, ensure that your DOS environment configuration file `AUTOEXEC.BAT` initializes a VESA BIOS Extension helper utility (such as `UNIVBE.EXE`) prior to starting the software.

---

---

## Page 26

### Appendix A: Derivation of the Jacobian Matrix

For a comprehensive mathematical stability analysis of the fixed points found within our physical systems, we evaluate local behaviors using a linear expansion represented by the **Jacobian Matrix** $J$.

Let us define a general two-dimensional autonomous system:

$$\begin{aligned}
\dot{x} &= f(x, y) \\
\dot{y} &= g(x, y)
\end{aligned}$$

The Jacobian matrix is defined as the array of partial derivatives relative to each state variable:

$$J = \begin{pmatrix} 
\frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} \\ 
\frac{\partial g}{\partial x} & \frac{\partial g}{\partial y} 
\end{pmatrix}$$

For the unforced mathematical pendulum with viscous damping, our system functions are $f(\phi, \Omega) = \Omega$ and $g(\phi, \Omega) = -\frac{b}{I}\Omega - \frac{mgl}{I}\sin\phi$. Calculating the derivatives yields:

$$J(\phi, \Omega) = \begin{pmatrix} 
0 & 1 \\ 
-\frac{mgl}{I}\cos\phi & -\frac{b}{I} \end{pmatrix}$$

Evaluating this matrix at specific equilibrium points allows us to compute local eigenvalues, which define whether a fixed point acts as a stable node, unstable saddle, or spiral focus.

---

---

## Page 27

### Appendix B: Bibliography and Suggested Reading

For readers wishing to deepen their theoretical understanding of nonlinear mechanics, chaos theory, and fractal geometry, the following literature is highly recommended:

1. **Berge, P., Pomeau, Y., Vidal, C. (1984):** *Order within Chaos: Towards a Deterministic Approach to Turbulence.* John Wiley & Sons.
2. **Devaney, R. L. (1989):** *An Introduction to Chaotic Dynamical Systems.* Addison-Wesley.
3. **Feigenbaum, M. J. (1978):** *Quantitative Universality for a Class of Nonlinear Transformations.* Journal of Statistical Physics, Vol. 19, pp. 25-52.
4. **Guckenheimer, J., Holmes, P. (1983):** *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields.* Springer-Verlag.
5. **Moon, F. C. (1992):** *Chaotic and Fractal Dynamics: An Introduction for Applied Scientists and Engineers.* Wiley-VCH.
6. **Peitgen, H.-O., Richter, P. H. (1986):** *The Beauty of Fractals.* Springer-Verlag.
7. **Schuster, H. G. (1988):** *Deterministic Chaos: An Introduction.* VCH Verlagsgesellschaft.
8. **Strogatz, S. H. (1994):** *Nonlinear Dynamics and Chaos.* Addison-Wesley.

---

---

## Page 28

### Appendix C: Laboratory Worksheets (Templates)

#### Experiment Protocol Form

**Date:** ______________

**Experimenter Name(s):** __________________________________________

**Selected Physical Model:** [ ] Mathematical Pendulum  [ ] Duffing Oszillator

##### Fixed Parameters Setup:

* Mass $m = $ _________ $\text{kg}$
* Length $l = $ _________ $\text{m}$
* Damping coefficient $b = $ _________ $\text{Nms}$

##### Variable Parameter / Measurement Series:

| Run No. | Initial $\phi_0$ / $x_0$ | Initial $\Omega_0$ / $\dot{x}_0$ | Driver Amp $A$ | Observed State / Periodicity |
| --- | --- | --- | --- | --- |
| **1** |  |  |  |  |
| **2** |  |  |  |  |
| **3** |  |  |  |  |
| **4** |  |  |  |  |
| **5** |  |  |  |  |

---

---

## Page 29

### Appendix D: Quick Reference Guide (Menu Tree)

The following diagram maps out the complete structure of the character-based menu tree inside the software to help you locate advanced parameters quickly.

```text
[Main Menu]
 │
 ├───[File]
 │    ├─── Load Parameters (*.PAR)
 │    ├─── Save Parameters (*.PAR)
 │    ├─── Export ASCII Data (*.TXT)
 │    └─── Exit Program (ESC)
 │
 ├───[System Mode]
 │    ├─── Mathematical Pendulum (free/forced)
 │    └─── Duffing Oscillator (Double-Well setup)
 │
 ├───[Parameters Input]
 │    ├─── Mechanical Properties (m, l, c, d)
 │    ├─── Dissipation / Damping (b)
 │    └─── Driving Force Configuration (A, omega)
 │
 └───[View Windows]
      ├─── Time Domain Graph (x vs t)
      ├─── Phase Space Portrait (dx/dt vs x)
      └─── Stroboscopic Poincaré Grid

```

---

---

## Page 30

### Appendix E: Hardware Requirements and Installation Guide

#### E.1 Minimum Configuration

To run the simulation program successfully, your computer system must meet the following minimum requirements:

* **Processor:** Intel 8086 / 8088 CPU or higher (an Intel 80386 DX or 80486 is recommended for smooth real-time rendering).
* **Operating System:** MS-DOS version 3.3 or higher, or a compatible DOS environment (e.g., DR-DOS, Novell DOS).
* **Memory:** At least $512\text{ KB}$ of available conventional RAM.
* **Graphics Card:** IBM-compatible VGA or EGA card with dedicated video memory.
* **Disk Drive:** A $3.5\text{-inch}$ high-density floppy disk drive (`1.44 MB`) for installation.

#### E.2 Installation Procedure

1. Insert the original software diskette into your floppy drive (usually drive `A:` or `B:`).
2. Switch to that drive path by typing: `A:` (and hitting `[Enter]`).
3. Create a dedicated folder on your local hard drive: `MD C:\SCHWING`.
4. Copy all program files into that location: `COPY *.* C:\SCHWING /V`.
5. Switch to your hard drive folder: `CD C:\SCHWING`.
6. Start the simulation environment by typing: `SCHWING.EXE`.

---

**End of Appendix E.**

---

## Page 31

### Appendix F: Advanced Laboratory Assignments (Project Phase)

#### 1. Project 1: Exploring the Sensitive Dependence on Initial Conditions

##### Objective:

To quantitatively measure the butterfly effect (sensitive dependence on initial conditions) by observing how two trajectories with an extremely small initial separation diverge exponentially over time.

##### Program Setup:

* **System:** Forced Mathematical Pendulum with Damping.
* **Parameters:** $l = 0.25\text{ m}$, $m = 0.2\text{ kg}$, Damping $b = 0.04\text{ Nms}$, Driver Amplitude $A = 0.550\text{ Nm}$ (Chaotic regime, see Experiment 3).

##### Procedure:

1. Start a simulation run with initial conditions $\vec{x}_A(0) = (1.000000, 0.0)$ and let it calculate up to $t = 50\text{ s}$. Save this reference trajectory.
2. Start a second simulation run with a tiny change to the initial angle: $\vec{x}_B(0) = (1.000001, 0.0)$. The initial separation distance is only $\Delta\phi(0) = 10^{-6}\text{ rad}$.
3. Use the dual-plot function to overlay both trajectories on the **Zeitverlauf (Time History)** screen.

##### Observations:

Note that for the first few seconds, both curves overlap perfectly. However, around $t \approx 20\text{ s}$ to $25\text{ s}$, the two curves separate completely and follow entirely different paths. Measure the exact time at which the visual overlap breaks down and discuss how this limits long-term predictability.

---

---

## Page 32

#### 2. Project 2: Measuring the Lyapunov Exponent

##### Objective:

To estimate the largest Lyapunov exponent $\lambda$ of a chaotic attractor from the divergence rate measured in Project 1.

##### Mathematical Foundation:

The average exponential divergence of two nearby trajectories in phase space is described by the relation:

$$d(t) \approx d(0) \cdot e^{\lambda \cdot t}$$

where $d(t) = \|\vec{x}_A(t) - \vec{x}_B(t)\|$ represents the distance at time $t$. Taking the natural logarithm yields a linear equation:

$$\ln\left(\frac{d(t)}{d(0)}\right) = \lambda \cdot t$$

##### Evaluation Procedure:

1. Export the time-series data from both simulation runs in Project 1 into a spreadsheet utility.
2. For each time step, calculate the distance $d(t) = \sqrt{(\phi_A - \phi_B)^2 + (\Omega_A - \Omega_B)^2}$.
3. Plot $\ln(d(t))$ against the time $t$.

![Figure 4.2.2: Semi-logarithmic plot of trajectory separation versus time, showing a linear upward trend indicating exponential divergence with an estimated slope lambda of 0.45.]

> **Figure 4.2.2: Semilogarithmic plot of trajectory divergence.** > *Description:* A coordinate plot with a linear time axis $t$ on the horizontal axis and a logarithmic distance axis $\ln(d(t))$ on the vertical axis. The data points form a noisy but clearly linear upward slope during the early phase ($t = 0$ to $t = 25\text{ s}$), representing exponential divergence. A straight line of best fit shows a slope of $\lambda \approx 0.45$, confirming a positive Lyapunov exponent before saturation occurs.

---

---

## Page 33

#### 3. Project 3: Analysis of the Poincaré Section at Different Driving Phases

##### Objective:

To observe how the geometric structure of a strange attractor changes in phase space depending on the choice of the stroboscopic sampling phase angle $\psi_0$.

##### Program Setup:

Use the exact same parameters for the chaotic pendulum as in Project 1 ($A = 0.550\text{ Nm}$).

##### Procedure:

The program allows you to adjust the stroboscopic sampling time by shifting the phase parameter `PhaseShift` in the options menu.

1. Generate a Poincaré section using a phase shift of $\psi_0 = 0^\circ$. This samples states exactly at the cosine peaks of the driving force ($t_k = k \cdot T_A$).
2. Clear the viewport without resetting the simulation loop (`[F6]`) and change the parameter to $\psi_0 = 90^\circ$ ($t_k = (k + 0.25) \cdot T_A$).
3. Repeat this process for $\psi_0 = 180^\circ$ and $\psi_0 = 270^\circ$.

##### Tasks:

Print out or sketch all four resulting geometric structures. Describe the continuous deformation of the attractor. Note that while the outer shape stretches and folds like dough, its underlying topological properties and its non-integer fractal dimension remain constant throughout the cycle.

---

---

## Page 34

### Appendix G: Analytical Solution for the Linearized Pendulum

To better understand why nonlinear systems behave so uniquely, it helps to review the analytical solution of the linearized pendulum with damping, which serves as a baseline.

Assuming very small angles ($\sin\phi \approx \phi$), the equation of motion from page 3 simplifies to:

$$\ddot{\phi} + 2\gamma\dot{\phi} + \omega_0^2\phi = 0$$

where $\gamma = \frac{b}{2I}$ is the damping constant and $\omega_0 = \sqrt{\frac{mgl}{I}}$ is the natural frequency.

The characteristic equation for this linear differential equation is:

$$\lambda^2 + 2\gamma\lambda + \omega_0^2 = 0$$

The roots of this polynomial determine the behavior of the system:

$$\lambda_{1,2} = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$$

#### The Three Classical Linear Regimes:

1. **Underdamped Case ($\gamma < \omega_0$):** The roots are complex conjugates. The system performs damped harmonic oscillations with a shifting frequency $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$. Trajectories spiral into a stable focus at the origin.
2. **Overdamped Case ($\gamma > \omega_0$):** The roots are purely real and negative. The system returns to equilibrium without oscillating.
3. **Critical Damping ($\gamma = \omega_0$):** The system returns to its rest position in the shortest possible time.

---

---

## Page 35

### Appendix H: Structural Overview of the Program Modules

The executable application `SCHWING.EXE` is built from several source code units compiled together. Below is a map of these modules to guide you if you choose to modify the code.

```
                  +-----------------------+
                  |      SCHWING.PAS      | (Main Program Loop & Menu)
                  +-----------+-----------+
                              |
       +----------------------+----------------------+
       |                      |                      |
v      v                      v                      v
+--------------+      +--------------+      +--------------+
|   VGA_GRAF   |      |   NUM_INT    |      |  MODELL_OBJ  |
+--------------+      +--------------+      +--------------+
| Handles VGA  |      | Implements   |      | Object       |
| 640x480 pixel|      | the standard |      | definitions  |
| graphics and |      | fourth-order |      | for equations|
| page-flipping|      | Runge-Kutta  |      | of motion    |
+--------------+      +--------------+      +--------------+

```

#### Detailed Description of the Units:

* **`SCHWING.PAS`:** The main entry point. It handles user inputs, sets up the character-based menus, manages configuration files, and drives the execution loop.
* **`VGA_GRAF.TPU`:** A hardware-optimized graphics wrapper. It bypasses slow standard Pascal routines to draw trajectories directly onto the video memory (VRAM segment `$A000`).
* **`NUM_INT.TPU`:** The math library. It holds the core Runge-Kutta routines and coordinate transformation algorithms that map physical values onto screen pixels.
* **`MODELL_OBJ.TPU`:** Contains the object definitions. This is where the differential equations for the pendulum, the Duffing oscillator, and other models are stored.

---

---

## Page 36

### Appendix I: Advanced Laboratory Worksheet

#### Experiment Protocol: Generating a Bifurcation Diagram

**Date:** ______________

**Name:** _________________________________________

**Selected System:** Driven Damped Pendulum (Feigenbaum Scenario)

##### Fixed Parameters:

* Length $l = 0.25\text{ m}$
* Damping $b = 0.04\text{ Nms}$
* Driver Frequency $\omega_A = 4.176\text{ s}^{-1}$

##### Parameter Sweeping:

Slowly increase the driver amplitude $A$ in small increments. For each step, let transient behaviors settle before recording the stable coordinate points visited on the Poincaré section.

| Step | Driver Amplitude $A$ ($\text{Nm}$) | Number of Unique Points | Classification (e.g., Period 1, 2, 4, Chaos) |
| --- | --- | --- | --- |
| **1** | $0.250$ | $1$ | Period 1 |
| **2** | $0.450$ | $1$ | Period 1 |
| **3** | $0.535$ | $2$ | Period 2 (First Bifurcation) |
| **4** | $0.543$ | $4$ | Period 4 |
| **5** | $0.547$ | $8$ | Period 8 |
| **6** | $0.550$ | $\infty$ | Deterministic Chaos |
| **7** | $0.558$ | $3$ | Periodic Window (Period 3) |

---

---

## Page 37

### Appendix J: Geometric Construction of the Cantor Set

To understand the complex filament structures observed in strange attractors (such as the Poincaré section in Experiment 3), it helps to study the **Cantor Set**, which serves as the classic mathematical model for a fractal.

The Cantor set is constructed through an infinite iterative process known as a middle-third elimination applied to a continuous line segment:

```
Step 0: [=================================================] (Interval [0,1])

Step 1: [===============]               [===============] (Middle third removed)

Step 2: [===]       [===]               [===]       [===]

Step 3: [-]   [-]   [-]   [-]           [-]   [-]   [-]   [-]

```

#### Properties of the Cantor Set:

* **Total Length:** After $n$ iterations, the remaining length of the line segments is $(\frac{2}{3})^n$. In the limit as $n \rightarrow \infty$, the total length shrinks to exactly **zero**.
* **Number of Elements:** Despite having a total length of zero, the remaining set contains uncountably many points.
* **Fractal Dimension:** Since the set is neither a classic zero-dimensional point nor a one-dimensional line, its dimension is fractional. It is computed using its self-similarity ratio:
$$D = \frac{\ln(2)}{\ln(3)} \approx 0.6309$$



Strange attractors are often formed by the product of a continuous manifold along the direction of flow and a Cantor-like fractal set across the direction of stretching and folding.

---

---

## Page 38

### Appendix K: Numerical Estimation of the Basin of Attraction

For non-linear systems that feature multiple stable fixed points or coexisting attractors (such as the double-well Duffing oscillator configuration), determining which final state the system will land in is a key question. This is visualized using a **Basin of Attraction** map.

#### Method of Computation:

The program scans a grid across the phase plane, typically containing $200 \times 200$ coordinate points. Each point on this grid serves as an initial condition $(x_0, \dot{x}_0)$ for a complete simulation run.

```
  Initial Velocity (v)
       ^
       |  B B B B B . . . R R R R R
       |  B B B B . . . . . R R R R
       |  B B B . . . . . . . R R R  <- Grid point analysis
       |  B B . . . . . . . . . R R
       +----------------------------> Initial Displacement (x)

```

The algorithm tracks the trajectory until it settles into a stable state:

* If the trajectory ends up in the **left potential well**, the starting pixel is colored **Blue** (`B`).
* If it settles into the **right potential well**, the starting pixel is colored **Red** (`R`).

##### Fractal Boundaries:

In highly non-linear regimes, these color fields do not split cleanly down the middle. Instead, their boundaries interlace into intricate, non-periodic structures. Near these fractal boundaries, even a microscopic change to your starting conditions can completely flip the final outcome of the experiment.

---

---

## Page 39

### Chapter VIII: Technical Specifications and File Layouts

#### 1. Binary Data Format (`*.BIN`)

When you choose to record continuous trajectories over long periods, the software saves raw data directly to disk as a packed binary stream to optimize performance and save space. Each recorded state is stored as a fixed-length data block.

##### Byte Structure of a Trajectory Entry:

| Byte Offset | Data Type | Internal Variable Name | Description |
| --- | --- | --- | --- |
| `00 - 03` | `Single` (4 Bytes) | `TimeStamp` | Elapsed simulation time in seconds. |
| `04 - 07` | `Single` (4 Bytes) | `PositionX` | Angular deflection or displacement. |
| `08 - 11` | `Single` (4 Bytes) | `VelocityV` | Angular velocity or momentum. |

A file containing $10,000$ computed steps takes up exactly $120,000\text{ Bytes}$ (approx. $117\text{ KB}$) of storage space. This packed structure allows older computers to read and write data files quickly without hitting RAM limits.

---

---

## Page 40

#### 2. Parameter Saving Layout (`*.PAR`)

Unlike configuration files which store system settings behind the scenes (page 16), parameter files (`*.PAR`) are managed directly by the user. They allow you to save and reload specific laboratory configurations for different assignments. These files are stored as plain ASCII text and can be edited using standard tools like DOS `EDIT` or Notepad.

##### Example File Structure (`DUFFING1.PAR`):

```text
[SIMULATION_PARAMETER_FILE]
VERSION=2.1
MODEL_TYPE=2
PARAMETER_M=1.00000000
PARAMETER_B=0.15000000
PARAMETER_C=-1.00000000
PARAMETER_D=1.00000000
DRIVER_AMP=0.35000000
DRIVER_FREQ=1.40000000
INTEGRATION_DT=0.01000000
GRAPHIC_X_MIN=-2.50000000
GRAPHIC_X_MAX=2.50000000
GRAPHIC_Y_MIN=-2.00000000
GRAPHIC_Y_MAX=2.00000000
EOF

```

> **Note:** When editing these parameters manually, keep the exact variable name and use a period (`.`) as the decimal separator. Commas will cause file-parsing errors during loading.

---

**End of Chapter VIII.**

---

## Page 41

#### 3. Structure of the Plot Output Files (`*.DAT`)

When you use the automated "Save Path" function from the file menu, the program writes the screen coordinates of the active graphic window out as raw ASCII numbers. This is ideal if you want to regenerate the plots using external software like Gnuplot or Origin.

##### Layout and Delimiters:

The file splits into a short header indicating the coordinate dimensions, followed by the continuous coordinate pairs separated by a blank space.

```text
[GRAPH_DATA_FILE]
POINTS=2500
X_LABEL=Displacement x
Y_LABEL=Velocity v
X_MIN=-2.00
X_MAX=2.00
Y_MIN=-3.00
Y_MAX=3.00
[DATA_START]
-1.5000 0.0000
-1.4920 0.0340
-1.4780 0.0650
...
1.2300 -1.1200
[DATA_END]

```

---

---

## Page 42

### Appendix L: The Van der Pol Oscillator (Model Extension)

Addressed briefly in the version history, the van der Pol oscillator represents a non-linear system with non-conservative self-sustained oscillations. It acts as a baseline model for systems that take energy from their environment when amplitudes are low, but dissipate energy when amplitudes are high.

The differential equation of the unforced van der Pol system is given by:

$$\ddot{x} - \mu(1 - x^2)\dot{x} + x = 0$$

where $\mu > 0$ is the non-linear damping parameter.

#### Behavior of the Friction Term:

* **For small amplitudes ($x < 1$):** The term $\mu(1 - x^2)$ is positive, meaning the overall coefficient $-\mu(1 - x^2)$ in front of $\dot{x}$ is negative. This acts as "negative friction"—the system amplifies itself, drawing energy into the oscillation.
* **For large amplitudes ($x > 1$):** The term becomes negative, creating positive viscous damping that removes energy from the system.

No matter what initial conditions you start with, all trajectories converge toward a unique, stable closed loop in phase space known as a **Limit Cycle**.

---

---

## Page 43

### Appendix M: Derivation of the Feigenbaum Constant

The period-doubling cascade observed in Experiment 3 (pages 8 and 9) follows a strict universal scaling law discovered by Mitchell Feigenbaum in 1975.

Let $A_n$ be the threshold value of the control parameter (such as driver amplitude) where a bifurcation from a period-$2^{n-1}$ cycle to a period-$2^n$ cycle occurs.

$$\begin{aligned}
A_1 &= 0.5350 \quad (\text{Period 1 } \rightarrow \text{ Period 2}) \\
A_2 &= 0.5430 \quad (\text{Period 2 } \rightarrow \text{ Period 4}) \\
A_3 &= 0.5470 \quad (\text{Period 4 } \rightarrow \text{ Period 8})
\end{aligned}$$

The ratio of consecutive parameter intervals converges to a universal mathematical constant:

$$\delta = \lim_{n \rightarrow \infty} \frac{A_n - A_{n-1}}{A_{n+1} - A_n}$$

Using our recorded thresholds from the experiment template on page 36:

$$\delta_1 = \frac{0.5430 - 0.5350}{0.5470 - 0.5430} = \frac{0.0080}{0.0040} = 2.00$$

As $n$ approaches infinity, this ratio approaches the universal value for all one-dimensional quadratic maps:

$$\delta \approx 4.6692016...$$

---

---

## Page 44

### Appendix N: Numerical Calculation of Power Spectra (FFT)

To distinguish between a high-period regular oscillation and true deterministic chaos, looking at the time history alone is often not enough. The program includes a **Fourier Analysis (FFT)** module to convert time-domain data into the frequency domain.

Given $N$ discrete tracking points $x_k$, the discrete Fourier transform computes complex frequency amplitudes $X_n$:

$$X_n = \sum_{k=0}^{N-1} x_k \cdot e^{-i \frac{2\pi}{N} n \cdot k}$$

![Figure 5.4.2: Power spectrum plots comparing a sharp, discrete peak of a periodic system to a broad, continuous noise floor characteristic of a chaotic system.]

> **Figure 5.4.2: Frequency spectrum comparison.** > *Description:* Two separate spectral plots showing intensity on the vertical axis against frequency $f$ on the horizontal axis.
> * **Top Plot (a):** Represents a periodic system, showing sharp, separate vertical spikes at the fundamental driving frequency and its clean subharmonics.
> * **Bottom Plot (b):** Represents a chaotic system, where individual spikes disappear into a broad, continuous noise spectrum across all frequencies, indicating non-periodic behavior.
> 
> 

---

---

## Page 45

### Appendix O: The Double-Well Potential of the Duffing Oscillator

When configuring the Duffing oscillator parameter to $c < 0$ and $d > 0$, you transform the system into a **Double-Well Potential**. This models a physical setup like a flexible steel beam suspended between two permanent magnets.

The potential energy function $V(x)$ is found by integrating the restoring force:

$$V(x) = -\int (c \cdot x + d \cdot x^3) dx = -\frac{c}{2}x^2 + \frac{d}{4}x^4$$

For $c = -1$ and $d = 1$, the potential function simplifies to:

$$V(x) = -\frac{1}{2}x^2 + \frac{1}{4}x^4$$

#### Geometric Shape:

This function describes a classic "W-shape" curve. The system has an unstable local maximum at the center position $x_0 = 0$ (a saddle point) and two stable local potential minima located at:

$$x_{1,2} = \pm \sqrt{\frac{-c}{d}} = \pm 1$$

When driven by an external force, the trajectory can bounce back and forth inside one of the wells or jump across the central barrier into the opposite well, creating highly complex chaotic paths.

---

---

## Page 46

### Appendix P: Fixed Point Classification and Phase Space Flow

To mathematically analyze the behavior near equilibrium points, we evaluate the eigenvalues $\lambda_{1,2}$ derived from the local Jacobian matrix (as discussed on page 26).

The characteristic equation used to find these values is:

$$\det(J - \lambda \cdot I) = 0 \quad \rightarrow \quad \lambda^2 - \text{Sp}(J)\cdot\lambda + \det(J) = 0$$

where $\text{Sp}(J)$ is the trace and $\det(J)$ is the determinant of the matrix.

| Eigenvalue Condition | Geometric Stability Class | Trajectory Behavior |
| --- | --- | --- |
| $\lambda_1, \lambda_2 < 0$ (purely real) | **Stable Node** | Inward paths approach from all directions without looping. |
| $\lambda_1, \lambda_2 > 0$ (purely real) | **Unstable Node** | Paths accelerate outward in all directions. |
| $\lambda_{1,2} = \alpha \pm i\beta$ with $\alpha < 0$ | **Stable Focus** | Paths spiral inward toward the center. |
| $\lambda_1 < 0, \lambda_2 > 0$ (purely real) | **Saddle Point** | Paths approach along one axis but deflect outward along the other. |

---

---

## Page 47

### Appendix Q: Calculating the Correlation Dimension

To assign a clear numerical value to the strange patterns found on a Poincaré section, we calculate its fractal dimension. The program includes an automated utility to compute the **Correlation Dimension** ($D_2$) using the Grassberger-Procaccia algorithm.

#### Computational Process:

1. Extract a set of $N$ points $\vec{x}_i$ from a long chaotic simulation run.
2. Compute the correlation integral $C(r)$, which counts the relative number of coordinate pairs separated by a distance smaller than a choice radius $r$:
$$C(r) = \lim_{N \rightarrow \infty} \frac{2}{N(N-1)} \sum_{i < j} \Theta(r - \|\vec{x}_i - \vec{x}_j\|)$$


where $\Theta$ is the Heaviside step function ($\Theta(s) = 0$ for $s < 0$, $\Theta(s) = 1$ for $s \ge 0$).

If the radius $r$ is varied across a small scale, the correlation integral scales as a power law:

$$C(r) \propto r^{D_2}$$

The dimension is found by measuring the slope of a log-log plot:

$$D_2 = \lim_{r \rightarrow 0} \frac{\ln C(r)}{\ln(r)}$$

For our default chaotic pendulum attractor, this yields a fractional value of $D_2 \approx 1.25$.

---

---

## Page 48

### Appendix R: Mathematical Model of Pohl's Torsion Pendulum

Expanding on the laboratory overview from page 4, we define the complete equation of motion for Pohl's torsion pendulum.

The system features three distinct torques acting on a rotating copper wheel:

1. **Linear Restoring Torque:** Placed by the spiral spring: $M_{\text{spring}} = -D \cdot \phi$.
2. **Dissipative Frictional Torque:** Caused by the eddy current brake. This force scales linearly with the angular velocity: $M_{\text{friction}} = -W \cdot \dot{\phi}$.
3. **Nonlinear Gravitational Torque:** Created by attaching an off-center mass $m_add$ at a radius $r$: $M_{\text{grav}} = +m_{\text{add}} \cdot g \cdot r \cdot \sin\phi$.

Combining these components according to the rotational version of Newton's second law ($I \cdot \ddot{\phi} = \sum M$) yields:

I \cdot \ddot{\phi} + W \cdot \dot{\phi} + D \cdot \phi - m_{\text{add}} \cdot g \cdot r \cdot \sin\phi = M_A \cdot \cos(\omega_A \cdot t)

Dividing through by the moment of inertia $I$ simplifies the equation to the standard format used by our integration code:

$$\ddot{\phi} + 2\gamma\dot{\phi} + \omega_0^2\phi - K\sin\phi = A \cdot \cos(\omega_A t)$$

---

---

## Page 49

### Appendix S: The Concept of the Separatrix

In conservative or weakly damped systems with multiple equilibrium states, the phase plane splits into distinct operational zones. The boundary line separating these different types of motion is called the **Separatrix**.

Let us analyze the phase portrait of the free mathematical pendulum from Experiment 2 (page 6).

```
   Velocity (omega)
         ^
         |       _..---.._     <- Oscillating loops (inside)
         |     .'         '.
   -pi   |    /     (0,0)   \      pi
  -------+---|---------------|--------> Displacement (phi)
         |    \             /  <- Separatrix boundary line
         |     '.         .'
         |       `''---''`     <- Rotating tracks (outside)

```

#### Physical Meaning:

* **Inside the Separatrix loop:** The total energy of the pendulum is less than its maximum potential energy ($E < 2mgl$). The trajectories form closed circles, meaning the pendulum swings back and forth around the bottom equilibrium point $(0,0)$.
* **Outside the Separatrix line:** The total energy is higher ($E > 2mgl$). The trajectories form open, endless wavy tracks, meaning the pendulum has enough energy to continuously loop all the way around its top pivot point.
* **On the Separatrix itself:** The energy is exactly $E = 2mgl$. This critical trajectory connects the unstable top equilibrium points ($\phi = \pm\pi$).

---

---

## Page 50

### Appendix T: Complete Parameter Sets for Reference Demonstrations

If you want to demonstrate classic nonlinear phenomena quickly without searching for parameters yourself, you can load these verified reference configurations from the `\SAMPLES\` directory.

#### 1. Standard Period-1 Limit Cycle (Van der Pol)

* **File:** `VDP_P1.PAR`
* **Parameters:** $\mu = 1.000$, Driver Amplitude $A = 0.000$ (Self-sustained isolation)
* **Window:** $X \in [-3, 3]$, $Y \in [-3, 3]$

#### 2. Feigenbaum Period-4 Track (Forced Pendulum)

* **File:** `PEND_P4.PAR`
* **Parameters:** $m = 0.200$, $l = 0.250$, Damping $b = 0.040$, Driver $A = 0.543$, $\omega_A = 4.176$
* **Window:** $\phi \in [-2, 4]$, $\Omega \in [-4, 4]$

#### 3. Intermittent Chaos Burst (Duffing Oscillator)

* **File:** `DUFF_INT.PAR`
* **Parameters:** $m = 1.000$, $b = 0.100$, $c = -1.000$, $d = 1.000$, Driver $A = 0.382$, $\omega_A = 1.400$
* **Window:** $x \in [-2.5, 2.5]$, $v \in [-2, 2]$

---

**End of Appendix T.**

---

## Page 51

### Appendix U: The Duffing Oscillator under Harmonic Driving

When an external harmonic force is applied to the Duffing oscillator system discussed in Appendix O, the autonomous system transforms into a non-autonomous system with a three-dimensional phase space.

The complete mathematical expression used within the numeric integration routine is:

$$\dot{x} = v$$

$$\dot{v} = -\frac{b}{m}v - \frac{c}{m}x - \frac{d}{m}x^3 + \frac{A}{m}\cos(\omega_A t)$$

#### Structural Changes with Driving:

* **Without External Driving ($A = 0$):** The system's energy strictly decreases due to the damping coefficient $b$. All trajectories eventually terminate at one of the two stable potential wells ($x = \pm 1$).
* **With External Driving ($A > 0$):** The continuous injection of energy counteracts the internal damping dissipation. This balance allows the system to escape localized point attractors, resulting in persistent global non-periodic behaviors, windowed multi-periodic tracks, or strange chaotic attractors depending on the chosen amplitude $A$.

---

---

## Page 52

### Appendix V: Overview of Numerical Instabilities in Euler Integration

To help students appreciate why the software relies on the fourth-order Runge-Kutta method (RK4), this section demonstrates the geometric failure of simpler approaches like the **Euler-Cromer Method** or the **Forward Euler Method**.

Let us consider a simple harmonic oscillator solved via the forward Euler approximation:

$$x_{n+1} = x_n + v_n \cdot dt$$

$$v_{n+1} = v_n - \omega_0^2 x_n \cdot dt$$

#### Energy Analysis of the Discretization Error:

Evaluating the total mechanical energy equation at the next step yields:

$$E_{n+1} = \frac{1}{2}m v_{n+1}^2 + \frac{1}{2}m \omega_0^2 x_{n+1}^2$$

Substituting the Euler equations into this formula reveals an artificial energy increase:

$$E_{n+1} = E_n \cdot (1 + \omega_0^2 dt^2)$$

Because the error factor $(1 + \omega_0^2 dt^2)$ is strictly greater than $1$ for any positive time step $dt$, a forward Euler integration will slowly spiral outward over time. This creates a fake, non-physical energy growth that can easily be mistaken for an actual physical instability.

---

---

## Page 53

### Appendix W: The Concept of Floquet Multipliers

For non-linear systems experiencing periodic driving, the stability of a closed orbit (a limit cycle) can be rigorously analyzed using **Floquet Theory**. This method tracks how small variations change after completing exactly one driving cycle $T_A$.

Let us define a perturbation vector $\vec{\xi}(t)$ relative to a periodic orbit. Over one period, the linear evolution of this perturbation is governed by the Monodromy Matrix $M$:

$$\vec{\xi}(t + T_A) = M \cdot \vec{\xi}(t)$$

The eigenvalues $\mu_j$ of this matrix $M$ are known as the **Floquet Multipliers**. They determine system stability across transitions:

* **Stable Limit Cycle:** All multipliers lie strictly inside the complex unit circle ($\|\mu_j\| < 1$).
* **Period-Doubling Bifurcation (Feigenbaum):** A single real multiplier exits the unit circle exactly through the negative real axis ($\mu_j = -1$).
* **Saddle-Node Bifurcation:** A multiplier exits the unit circle through the positive real axis ($\mu_j = +1$).
* **Hopf Bifurcation:** Two complex conjugate multipliers exit the unit circle concurrently ($\mu_{1,2} = e^{\pm i\theta}$).

---

---

## Page 54

### Appendix X: Data Compression and Bit-Packing for Telemetry Output

When transmitting long-term tracking datasets across old serial port interfaces (such as standard RS-232 networks linking laboratory computers), standard ASCII text files consume too much bandwidth. The software provides an alternative compressed binary mode (`/BIN_COMP`).

```
+-------------------------------------------------------------+
|               Packed 32-Bit Telemetry Frame                 |
+----------------------+--------------------+-----------------+
| Angular Position     | Angular Velocity   | Phase Status    |
| (14 Bits)            | (14 Bits)          | (4 Bits)        |
+----------------------+--------------------+-----------------+

```

#### Bit-Allocation Scheme:

* **Bits 00 to 13 (14 Bits):** Encodes the angular position $\phi$. The continuous range $[-\pi, \pi]$ is mapped directly to a discrete integer field from $0$ to $16,383$.
* **Bits 14 to 27 (14 Bits):** Encodes the velocity component $\Omega$, mapping the dynamic range $[-4\pi, 4\pi]$ to an integer scale.
* **Bits 28 to 31 (4 Bits):** Stores status markers (e.g., driver quadrant indicator, zero-crossing flags).

This layout compresses the data down to exactly $4\text{ Bytes}$ per sample step, reducing transmission overhead by more than $60\%$ compared to standard floating-point text streams.

---

---

## Page 55

### Appendix Y: Constructing a Return Map from Peak Values

When a stroboscopic external clock signal is unavailable for generating standard Poincaré sections, you can reconstruct the system's underlying dynamics using a **Peak Return Map** (or $X_{\max}$ map).

#### Execution Steps:

1. Track a continuous trajectory over a long simulation run.
2. Isolate the local maxima of the position coordinate, listing them sequentially: $x_{\max}(1), x_{\max}(2), x_{\max}(3), \dots$
3. Plot each peak value directly against the next one: $x_{\max}(n+1)$ vs $x_{\max}(n)$.

```
   x_max(n+1)
        ^
        |         /\
        |        /  \     <- Unimodal tent-like structure
        |       /    \
        |      /      \
        +-------------------> x_max(n)

```

For systems transitioning to chaos via period-doubling cascades, this peak-to-peak plotting method reduces complex phase trajectories into a simple, one-dimensional unimodal curve. This confirms that the complex physics of a three-dimensional continuous system can be captured by simpler, low-dimensional mathematical maps.

---

---

## Page 56

### Appendix Z: Software Version History and Patch Notes

#### Version 1.0 (March 1993):

* Initial release of the core integration engine.
* Supported basic text outputs and simple CGA graphics modes.
* Included equations of motion exclusively for the unforced mathematical pendulum.

#### Version 1.5 (November 1993):

* Added an upgraded graphic unit supporting standard $640 \times 480$ 16-color VGA modes.
* Introduced file import and export menus for configuration files (`SETUP.DAT`).
* Implemented the forced Duffing oscillator configuration.

#### Version 2.0 (August 1994):

* Full object-oriented rewrite of the core mathematical libraries.
* Added support for math coprocessors (8087/80387 FPUs).
* Added automated modules for computing Poincaré maps and Fourier spectra (FFT).

#### Version 2.1 (Current Release):

* Fixed a memory leak involving array heap overflows during long simulation runs (resolved via the ring buffer structure discussed on page 15).
* Added optional command-line switches (`/S`, `/VGA`, `/E`, `/P`).

---

---

## Page 57

### Index of Important Terms

#### A

* Attractor: 11, 12, 33, 47, 50
* Arnold Tongue: 23

#### B

* Basin of Attraction: 38
* Bifurcation Diagram: 9, 36, 43
* Borland Graphics Interface (BGI): 14, 15, 25

#### C

* Cantor Set: 37
* Chaos: 1, 8, 11, 31, 36, 44
* Conventional Memory Limit: 15

#### D

* Dissipative Systems: 12, 42, 51
* Double-Well Potential: 29, 38, 45, 51
* Duffing Oscillator: 14, 16, 21, 22, 29, 38, 45, 50, 51

#### E

* Eigenvalues: 26, 46, 53
* Euler Integration: 52

#### F

* Feigenbaum Constant: 9, 43
* Floquet Multipliers: 53
* Fourier Analysis (FFT): 44, 56

---

---

## Page 58

### Index of Important Terms (Continued)

#### J

* Jacobian Matrix: 26, 46

#### L

* Limit Cycle: 42, 50, 53
* Linearization: 2, 21, 34
* Liouville's Theorem: 12
* Lyapunov Exponent: 32

#### N

* Non-linear Restoring Force: 3, 21, 45, 48

#### P

* Phase Space: 5, 11, 12, 18, 26, 49
* Pohl's Torsion Pendulum: 4, 16, 48
* Poincaré Map / Section: 11, 15, 33, 36, 37, 55

#### R

* Ring Buffer: 15, 56
* Runge-Kutta Method (RK4): 13, 14, 16, 24, 35, 52

#### S

* Separatrix: 49
* Superposition Principle: 21

#### V

* Van der Pol Oscillator: 14, 42, 50

---

---

## Page 59

### Notes and Experimental Observations

*(This page has been intentionally left blank for lab notes, parameter records, and sketching trajectories during experiments.)*

---

---

## Page 60

### Quick Start Guide for the Physics Laboratory

1. **Power Up:** Turn on your computer and wait for the DOS prompt to appear (`C:\>`).
2. **Navigate:** Enter the application folder by typing `CD \SCHWING` and hitting `[Enter]`.
3. **Launch:** Start the application by typing `SCHWING.EXE` or `SCHWING.EXE /VGA` if using a modern monitor.
4. **Select Model:** Press **`[F2]`** to open the model choice window. Use the arrow keys to pick between the Pendulum or the Duffing Oscillator.
5. **Adjust Parameters:** Press **`[F3]`** to update parameters like mass, length, damping, or driving amplitude to match your current assignment sheet.
6. **Compute:** Press **`[F4]`** to start the integration loop and draw the trajectories in real time.
7. **Pause/Adjust:** Press the **`[Spacebar]`** to pause your run. Use the **`+`** or **`-`** keys to scale the window axes on the fly.
8. **Export Data:** Press **`[ESC]`** to return to the main window. Go to **File** $\rightarrow$ **Export ASCII Data** to save your run as a spreadsheet-compatible text file.

---

**End of Booklet.**

---

---

## Page 61

### Appendix AA: Troubleshooting Serial Connectivity (RS-232)

When using the packed binary telemetry output described in Appendix X to stream data to an external data logger, communication mismatches may occur due to incorrect timing hardware properties.

##### Standard COM Port Settings:

To successfully establish a link with a terminal program, configure your receiving hardware client to mirror the hardcoded parameters of the application:

* **Baud Rate:** $9600\text{ bps}$
* **Data Bits:** $8$
* **Parity:** None (`N`)
* **Stop Bits:** $1$
* **Flow Control:** None or XON/XOFF software handshaking

##### Common Pinout Misconnections:

If your software dashboard reads "Device Timeout", check your physical connection wire setup. The application expects a standard null-modem configuration mapping:

```text
DB9 Female (PC Side)               DB9 Female (Logger Side)
Pin 2 (RxD)  ---------------------  Pin 3 (TxD)
Pin 3 (TxD)  ---------------------  Pin 2 (RxD)
Pin 5 (GND)  ---------------------  Pin 5 (GND)

```

---

---

## Page 62

### Appendix AB: Acknowledgments and Project Credits

The development of the `SCHWING.EXE` simulation suite and this accompanying laboratory guide was made possible by the support, feedback, and technical contributions of many individuals.

#### Development Team:

* **Software Architecture & Core Numeric Engine:** Dipl.-Phys. Thomas Müller
* **Graphics Unit Design & Assembly Code Tuning:** Dr. rer. nat. Andreas Schmidt
* **Lab Worksheet Evaluation & Field Testing:** Structural Mechanics Research Group

#### Academic Institutional Support:

We express our gratitude to the Department of Physics and Nonlinear Dynamics Laboratory staff for providing the necessary computational testbeds and real-world legacy hardware configurations (including authentic Pohl mechanical pendulum setups) used to calibrate our fourth-order Runge-Kutta numerical tracking parameters.

*Special thanks go to Borland International for developing the Turbo Pascal compiler ecosystem, which remains a benchmark for low-level desktop engineering software stability.*

---

---

## Page 63

### Appendix AC: Colophon and Document Metadata

#### Document Specifications:

* **Title:** Numerical Simulation of Nonlinear Oscillatory Systems: A Guide to `SCHWING.EXE`
* **Document ID:** TechDoc-TP7-NLD-1994-V2.1
* **Publication Date:** November 14, 1994
* **Typography:** Pre-rendered monospace digital matrices and classical mechanical typesetting grids.
* **Production Tooling:** Drafted using local text processing systems under MS-DOS, with vector formatting blocks exported directly via layout utility scripts.

#### Copyright Information:

© 1993–1994 The Nonlinear Dynamics Simulation Project. All rights reserved.

Unauthorized duplication, translation, or binary distribution of the source code segments or documentation layouts without prior written consent from the architecture group is strictly prohibited.

---

---

