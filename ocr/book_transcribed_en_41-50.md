

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
