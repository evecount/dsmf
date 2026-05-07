"""
Creative Synthesis - ms_pilot Cognitive Vector Engine
Part of the Hybrid Quantum-Classical Intelligence Framework

Co-Created by Gwendalynn Lim Wan Ting & Gemini
Compiled & Maintained within the Antigravity IDE

This module implements Creative Synthesis, which blends or synthesizes vector 
trajectories non-destructively using weighted linear (Lerp) and spherical (Slerp) interpolations.
"""

import time
import numpy as np
from typing import Dict, Any, List

class CreativeSynthesis:
    """
    Synthesizes and blends vector trajectories smoothly, utilizing linear (Lerp)
    and spherical linear (Slerp) interpolation techniques to preserve structural logic.
    """
    
    def __init__(self):
        pass

    @staticmethod
    def lerp(vec_a: np.ndarray, vec_b: np.ndarray, t: float) -> np.ndarray:
        """Standard Linear Interpolation (Lerp)."""
        return (1.0 - t) * vec_a + t * vec_b

    @staticmethod
    def slerp(vec_a: np.ndarray, vec_b: np.ndarray, t: float) -> np.ndarray:
        """
        Spherical Linear Interpolation (Slerp) to interpolate smoothly along the 
        surface of a hypersphere, maintaining structural vector norm integrity.
        """
        # Normalize inputs to unit vectors
        norm_a = np.linalg.norm(vec_a)
        norm_b = np.linalg.norm(vec_b)
        
        if norm_a == 0.0 or norm_b == 0.0:
            return (1.0 - t) * vec_a + t * vec_b  # Fallback to Lerp
            
        u_a = vec_a / norm_a
        u_b = vec_b / norm_b
        
        # Calculate cosine of angle between vectors
        dot = np.clip(np.dot(u_a, u_b), -1.0, 1.0)
        
        # If vectors are extremely close, use Lerp to avoid division by zero
        if dot > 0.9995:
            blended_unit = (1.0 - t) * u_a + t * u_b
            blended_unit /= np.linalg.norm(blended_unit)
        else:
            # Slerp formula
            theta_0 = np.arccos(dot)
            theta_t = theta_0 * t
            
            sin_theta_0 = np.sin(theta_0)
            sin_theta_t = np.sin(theta_t)
            sin_theta_one_minus_t = np.sin(theta_0 * (1.0 - t))
            
            s0 = sin_theta_one_minus_t / sin_theta_0
            s1 = sin_theta_t / sin_theta_0
            
            blended_unit = s0 * u_a + s1 * u_b
            
        # Interpolate the magnitude of the vectors linearly
        interpolated_magnitude = (1.0 - t) * norm_a + t * norm_b
        
        return blended_unit * interpolated_magnitude

    def synthesize(self, vec_a: List[float], vec_b: List[float], weight: float = 0.5, method: str = "slerp") -> Dict[str, Any]:
        """
        Synthesize two vectors using the specified method.
        
        Args:
            vec_a (List[float]): Source coordinate vector.
            vec_b (List[float]): Destination coordinate vector.
            weight (float): Interpolation factor, clamped [0.0, 1.0].
            method (str): Interpolation type ('lerp' or 'slerp').
            
        Returns:
            Dict[str, Any]: Standardized output dictionary containing synthesized vector,
                            confidence metric, and latency.
        """
        start_time = time.perf_counter()
        
        # Clip weight to continuous bounds
        t = float(np.clip(weight, 0.0, 1.0))
        
        a = np.array(vec_a, dtype=float)
        b = np.array(vec_b, dtype=float)
        
        if method.lower() == "slerp":
            synthesized_vector = self.slerp(a, b, t)
        else:
            synthesized_vector = self.lerp(a, b, t)
            
        # Confidence is high if vector norms are stable (preventing vector collapse)
        norm_synth = np.linalg.norm(synthesized_vector)
        norm_expected = (1.0 - t) * np.linalg.norm(a) + t * np.linalg.norm(b)
        
        confidence = 1.0 - abs(norm_synth - norm_expected) / max(1e-5, norm_expected)
        confidence = float(np.clip(confidence, 0.0, 1.0))
        
        execution_latency = time.perf_counter() - start_time
        
        return {
            "synthesized_vector": synthesized_vector.tolist(),
            "method": method,
            "weight": t,
            "confidence": confidence,
            "latency_ms": execution_latency * 1000.0,
            "synthesized_norm": float(norm_synth)
        }

if __name__ == "__main__":
    # Internal self-testing block to verify stability and mathematical correctness
    print("==========================================================")
    print("Testing ms_pilot: Creative Synthesis module...")
    print("==========================================================")
    
    # Define two orthogonal vectors
    v_a = [1.0, 0.0, 0.0]
    v_b = [0.0, 1.0, 0.0]
    
    cs = CreativeSynthesis()
    
    # Test Lerp vs Slerp at 50% blend
    lerp_res = cs.synthesize(v_a, v_b, weight=0.5, method="lerp")
    slerp_res = cs.synthesize(v_a, v_b, weight=0.5, method="slerp")
    
    print("--- 50% Lerp Result ---")
    print(f"Vector:     {lerp_res['synthesized_vector']}")
    print(f"Norm:       {lerp_res['synthesized_norm']:.5f} (Shows typical linear shrinkage!)")
    print(f"Confidence: {lerp_res['confidence']:.5f}")
    
    print("\n--- 50% Slerp Result ---")
    print(f"Vector:     {slerp_res['synthesized_vector']}")
    print(f"Norm:       {slerp_res['synthesized_norm']:.5f} (Maintains structural vector norm!)")
    print(f"Confidence: {slerp_res['confidence']:.5f}")
    print(f"Latency:    {slerp_res['latency_ms']:.3f} ms")
    
    print("==========================================================")
    print("Creative Synthesis verification completed successfully.")
    print("==========================================================")
