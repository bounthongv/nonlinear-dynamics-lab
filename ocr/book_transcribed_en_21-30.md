
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

## Page 22

### Chapter VI: Advanced Nonlinear Phenomena

#### 1. Resonance Curve Distortion and Jump Phenomena

In linear systems, the steady-state amplitude of a forced oscillator plotted against driving frequency yields a symmetrical resonance curve. For nonlinear systems like the Duffing oscillator, this curve deforms significantly.

![Figure 3.1.2: Resonance curve of a hardening Duffing oscillator bending to the right, showing hysteresis loops and sudden amplitude jumps at critical frequencies.]

> **Figure 3.1.2: Hysteresis and jump phenomena.** > *Description:* A plot showing response amplitude on the y-axis against driving frequency $\omega_A$ on the x-axis. The resonance peak bends sharply to the right (higher frequencies) due to a hardening spring effect ($d > 0$). Arrows indicate a path: upward frequency sweeps cause the amplitude to follow the top curve until a critical drop point, while downward sweeps follow a lower curve before jumping up, establishing a clear hysteresis loop.

As shown in Figure 3.1.2, the resonance peak bends toward higher frequencies for a hardening spring mechanism ($d > 0$). This tilt creates a bistable frequency band where two distinct stable oscillation amplitudes can exist under identical physical parameters.

Which state the system settles into depends entirely on its past trajectory. Sweeping the driving frequency upward causes a sudden, catastrophic drop in amplitude at a upper threshold frequency. Sweeping downward causes a sudden jump back up at a lower threshold frequency.

---

## Page 23

#### 2. Subharmonic Oscillations and Frequency Entrainment

A fascinating feature of nonlinear driven systems is their ability to respond at frequencies completely different from the external driver. In linear systems, transient states die out, leaving a steady-state response that oscillates exclusively at the driving frequency $\omega_A$.

In nonlinear regimes, however, the system can display **subharmonic resonance**. This means the oscillator's response locks into a rational fraction of the driving frequency:

$$\omega_{\text{resp}} = \frac{p}{q} \cdot \omega_A \quad \text{with } p, q \in \mathbb{N}$$

##### Frequency Entrainment (Injection Locking):

When a nonlinear oscillator with its own natural frequency $\omega_0$ is driven by an external signal close to a harmonic or subharmonic frequency, it does not generate beats as a linear system would. Instead, the intrinsic frequency shifts and locks tightly onto the external driver. This self-synchronization boundary forms a classic geometric pattern in parameter space known as an **Arnold Tongue**.

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
