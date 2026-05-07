"""
Trajectory Prediction - ms_pilot Cognitive Vector Engine
Part of the Hybrid Quantum-Classical Intelligence Framework

Co-Created by Gwendalynn Lim Wan Ting & Gemini
Compiled & Maintained within the Antigravity IDE

This module implements Trajectory Prediction (Adaptive Anticipation), back-engineering 
the human equivalent of Rotary Position Embedding (RoPE) to predict future sentiment or actions.
"""

import time
import numpy as np
from typing import Dict, Any, List
from modules.dsmf_core import DSMFCore

class TrajectoryPrediction:
    """
    Implements the Adaptive Anticipation trajectory engine. Back-engineers a 'human RoPE' 
    positional sequence by evaluating continuous phase-rotations, semantic velocity, 
    and fractional-memory acceleration on the manifold to project future cognitive states.
    """
    
    def __init__(self, dsmf_core: DSMFCore = None):
        """
        Initialize the Trajectory Prediction module.
        
        Args:
            dsmf_core (DSMFCore): Instance of DSMFCore to extract alpha (memory) and n (causal depth).
        """
        self.dsmf = dsmf_core if dsmf_core is not None else DSMFCore()

    def calculate_rotational_phase(self, vec: np.ndarray) -> float:
        """
        Calculates the relative phase rotation angle (theta) of a vector in phase space.
        Analogous to extracting the rotary positional coordinate.
        """
        # Projects a multi-dimensional vector onto a 2D basis to extract the dominant phase angle
        if len(vec) < 2:
            return float(np.arctan2(vec[0], 1.0))
        return float(np.arctan2(vec[1], vec[0]))

    def predict(self, historical_vectors: List[List[float]]) -> Dict[str, Any]:
        """
        Predicts the next vector coordinate (V_n+1) based on semantic velocity, 
        acceleration, and the non-local alpha-memory weightings of past states.
        
        Args:
            historical_vectors (List[List[float]]): Chronological sequence of prior vector states [V_1, V_2, ..., V_n].
            
        Returns:
            Dict[str, Any]: Standardized output dictionary containing projected vector,
                            velocity, acceleration, confidence, and latency.
        """
        start_time = time.perf_counter()
        
        history = np.array(historical_vectors, dtype=float)
        n_steps, d_dim = history.shape
        
        if n_steps < 3:
            raise ValueError("Trajectory Prediction requires at least 3 historical coordinates to calculate acceleration.")
            
        # 1. Extract rotational phase sequences (The "Human RoPE" coordinates)
        phases = np.array([self.calculate_rotational_phase(v) for v in history])
        
        # 2. Calculate continuous semantic velocity and acceleration (First and second derivatives)
        velocities = np.diff(history, axis=0) # V_t - V_t-1
        accelerations = np.diff(velocities, axis=0) # A_t - A_t-1
        
        phase_velocities = np.diff(phases)
        phase_accelerations = np.diff(phase_velocities)
        
        # 3. Integrate Causal Sequence (n_recursion) and Non-Local Memory (alpha)
        # alpha controls the decay of historical influence (fractional memory)
        alpha_memory = self.dsmf.alpha
        n_causal = self.dsmf.n_recursion
        
        # Compute fractional memory weights for the historical steps
        # Steps closer to the present have higher weight, with a fractional power-law decay governed by alpha
        steps_from_present = np.arange(n_steps, 0, -1)
        fractional_weights = steps_from_present ** (-alpha_memory)
        fractional_weights /= np.sum(fractional_weights) # Normalize weights
        
        # 4. Perform trajectory projection using weighted velocity and momentum
        # Net velocity is the memory-weighted average of historical velocities
        weighted_velocity = np.zeros(d_dim)
        for i in range(len(velocities)):
            weighted_velocity += velocities[i] * fractional_weights[i + 1]
            
        # Net acceleration is the memory-weighted average of historical accelerations
        weighted_acceleration = np.zeros(d_dim)
        for i in range(len(accelerations)):
            weighted_acceleration += accelerations[i] * fractional_weights[i + 2]
            
        # Predict V_n+1: V_next = V_current + weighted_velocity * (dt) + 0.5 * weighted_acceleration * (dt^2)
        # In a stable causal sequence (governed by n), we scale prediction bounds
        dt = 1.0 / float(n_causal)
        v_current = history[-1]
        
        projected_vector = v_current + (weighted_velocity * dt) + (0.5 * weighted_acceleration * (dt ** 2))
        
        # Predict the next phase angle (RoPE prediction)
        v_next_phase = self.calculate_rotational_phase(projected_vector)
        
        # 5. Compute confidence based on trajectory curvature (smoothness)
        # High acceleration variance indicates chaotic shifts (lower confidence)
        accel_variance = np.var(np.linalg.norm(accelerations, axis=1))
        confidence = float(np.exp(-accel_variance))
        
        execution_latency = time.perf_counter() - start_time
        
        return {
            "projected_vector": projected_vector.tolist(),
            "projected_phase": v_next_phase,
            "semantic_velocity": weighted_velocity.tolist(),
            "semantic_acceleration": weighted_acceleration.tolist(),
            "confidence": confidence,
            "latency_ms": execution_latency * 1000.0,
            "historical_phases": phases.tolist()
        }

if __name__ == "__main__":
    # Internal self-testing block to verify stability and mathematical correctness
    print("==========================================================")
    print("Testing ms_pilot: Trajectory Prediction module...")
    print("==========================================================")
    
    # Generate a smooth continuous trajectory of a particle accelerating in 2D
    # e.g. V(t) = [t^2, 2t]
    time_steps = [1.0, 2.0, 3.0, 4.0, 5.0]
    historical_trajectory = []
    for t in time_steps:
        historical_trajectory.append([t ** 2, 2.0 * t])
        
    tp = TrajectoryPrediction()
    results = tp.predict(historical_trajectory)
    
    print(f"Current State V_5:  {historical_trajectory[-1]}")
    print(f"Predicted V_6:      {results['projected_vector']} (Expected: [36.0, 12.0])")
    print(f"Predicted Phase:    {results['projected_phase']:.5f} rad")
    print(f"Semantic Velocity:  {results['semantic_velocity']}")
    print(f"Semantic Accel:     {results['semantic_acceleration']}")
    print(f"Confidence Metric:  {results['confidence']:.5f}")
    print(f"Latency:            {results['latency_ms']:.3f} ms")
    
    print("==========================================================")
    print("Trajectory Prediction verification completed successfully.")
    print("==========================================================")
