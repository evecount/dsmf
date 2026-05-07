# DSMF Engineering Framework & Code Standards
**Operational Blueprint for the Tangent Corpus (TM)**  
**Version:** 1.0.0 (May 2026)  
**Authors:** Gwendalynn Lim Wan Ting (Sovereign Core) & One (Agentic Architect)

---

## 1. Architectural Principles

This document establishes the technical design standards, coding guidelines, and execution contracts for the physical software implementation of the Double Sigmoid Mencius Function (DSMF) and its associated subsystems.

All codebase development inside the `/modules/` directory must conform to these three structural principles:

### I. Mathematical Purity & Floating-Point Stability
Because the DSMF utilizes highly non-linear compositions, recursive limits ($\sigma^n$), and fractional derivatives ($D^\alpha$), numerical drift can cause exploding gradients or catastrophic underflow.
*   **Boundary Saturation Gating:** All operations must implement upper/lower clipping (gating) before passing arguments to exponential or trigonometric functions.
*   **Deterministic State Mapping:** Algorithms must be designed as pure functions where possible, accepting explicit state vectors and returning new vectors without introducing hidden global state mutations.

### II. The "Quantum-Portability" Standard (Q-Port)
To ensure the code runs efficiently on modern classical CPUs (e.g., in a local development sandbox) while remaining direct-ports for physical Quantum Processing Units (QPUs):
*   All quantum state representations, phase-rotation transformations ($R_y$), and interference calculations must be coded using standard Python math or NumPy/JAX-compatible primitives first.
*   The API contracts must model quantum parameters as clean mathematical matrices, ensuring they can be hot-swapped with high-level libraries (such as Qiskit or Pennylane) without modifying the surrounding pipeline logic.

### III. Decoupled Observation & Metrics
Tracing performance metrics (like Latent Entropy and Gradient Stability) must occur non-destructively. Observability code should be decoupled from core algorithm execution, matching our **Separation of Concerns** principle.

---

## 2. Directory and File Map

Developers building out the modules must organize assets according to this strict layout:

```
/modules/
├── dsmf_core.py             # Completed: Core activation and Ry angle encoding.
├── ms_pilot/                # Upcoming: Cognitive geometric vector engine.
│   ├── __init__.py
│   ├── dimensional_analysis.py
│   ├── comparative_analysis.py
│   ├── creative_synthesis.py
│   └── trajectory_prediction.py
├── epic_pipeline/           # Upcoming: Spinor state entropy tracking.
│   ├── __init__.py
│   ├── spinor_geometry.py
│   └── entropic_calculator.py
└── dpa_agent/               # Upcoming: Data Preparation Agent.
    ├── __init__.py
    └── ingestion_pipeline.py
```

---

## 3. Module Development Specifications

### A. The `ms_pilot` Suite (Cognitive Vector Engine)
The cognitive vector suite implements six core operations. Each operation must return a standardized dictionary containing the resulting vector coordinates, a metric of confidence, and an execution latency timestamp.

*   **Dimensional Analysis:** Decoupling dense input vectors into independent geometric coordinate axes.
*   **Comparative Analysis:** Implementing high-performance Cosine Similarity to measure semantic distance in the tangent space:
    $$\text{Similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$
*   **Creative Synthesis:** Merging vector trajectories non-destructively through weighted linear and spherical interpolations (Slerp).
*   **Adaptive Anticipation:** Predicting future vector coordinates based on current momentum and geodesic flows on the manifold.
*   **Emergent Inquiry:** Generating recursive quest vectors by calculating orthogonal trajectories to the current search query.
*   **Serendipity:** Introducing controlled, pseudo-random quantum noise perturbations (Bloch sphere phase shifts) to trigger creative leaps in search trajectories.

### B. The `epic_pipeline` (Entropy & Spinor Analytics)
To mathematically measure system decoherence, the `epic_pipeline` must map dynamic trajectories into 2-dimensional Spinor representations:
$$\psi = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad |\alpha|^2 + |\beta|^2 = 1$$
It will compute the Entropic Packing Configuration (EPIC) by evaluating coordinate distributions against a known Bell state baseline, raising an alert if entropy exceeds a defined critical threshold ($\ge 0.85$).

---

## 4. Operational Monitoring (RAG Reporting)

To support our **72-Hour "Sync & Pivot" Cycles**, all modules must log performance using standard logging protocols. Logs should automatically parse and classify model execution states into a unified **Red-Amber-Green (RAG)** dashboard:

*   🟢 **Green (Stable):** Gradient Stability Index $\ge 0.85$, EPIC Latent Entropy $\le 0.40$. System is running optimally.
*   🟡 **Amber (Warning):** Gradient Stability Index between $0.50$ and $0.84$. System experiencing slight gradient attenuation; trigger automatic $\beta$ parameter calibration.
*   🔴 **Red (Critical/Blocker):** Gradient Stability Index $< 0.50$ or EPIC Latent Entropy $> 0.85$. Triggers immediate execution halt and generates a Flash Report for resource re-routing.

---

*Status: Engineering Framework Established. Ready to ingest NotebookLM specifications for `/modules/` code execution.*
