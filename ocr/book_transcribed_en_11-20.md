
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

## Page 14

#### 2. Implementation in Borland Turbo Pascal 7.0

The simulation package was implemented as a high-performance, compiled desktop application under MS-DOS. Turbo Pascal 7.0 was chosen because it allows for direct hardware access, low-level graphics programming via the Borland Graphics Interface (BGI), and highly efficient execution routines.

##### Key Architectural Features:

* **Object-Oriented Design:** The various physical models (Pendulum, Duffing Oscillator, van der Pol) are implemented as child objects inheriting from a base virtual `TOscillator` class. This simplifies expanding the software with new systems.
* **Real-Time Graphics:** Instead of calculating entire datasets beforehand and displaying them statically, the RK4 algorithm and VGA pixel-rendering routines run concurrently inside the main program loop. This allows you to watch the trajectories develop in real time.
* **Floating-Point Optimization:** The software supports native execution modes utilizing an 8087/80387 mathematical coprocessor (FPU) via the compiler directive `{$N+,G+}`. This dramatically reduces computation times for dense bifurcation tracks.

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
