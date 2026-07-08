

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

## Page 59

### Notes and Experimental Observations

*(This page has been intentionally left blank for lab notes, parameter records, and sketching trajectories during experiments.)*

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
