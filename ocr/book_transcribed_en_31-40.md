

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
