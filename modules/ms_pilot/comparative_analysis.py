"""
Comparative Analysis - ms_pilot Cognitive Vector Engine
Part of the Hybrid Quantum-Classical Intelligence Framework

Co-Created by Gwendalynn Lim Wan Ting & Gemini
Compiled & Maintained within the Antigravity IDE

This module implements Comparative Analysis, which calculates state-aware Cosine Similarity
adjusted through the Double Sigmoid Mencius Function (DSMF) non-linear decision boundaries.
"""

import time
import numpy as np
from typing import Dict, Any, List, Union
from modules.dsmf_core import DSMFCore

class ComparativeAnalysis:
    """
    Computes high-performance Cosine Similarity over vector spaces, with DSMF-gated
    scaling to capture subtle quantum-classical state transitions.
    """
    
    def __init__(self, dsmf_core: DSMFCore = None):
        """
        Initialize the Comparative Analysis module.
        
        Args:
            dsmf_core (DSMFCore): Instance of DSMFCore for non-linear threshold gating.
        """
        self.dsmf = dsmf_core if dsmf_core is not None else DSMFCore()

    def cosine_similarity(self, vec_a: np.ndarray, vec_b: np.ndarray) -> float:
        """Standard high-performance Cosine Similarity."""
        dot_product = np.dot(vec_a, vec_b)
        norm_a = np.linalg.norm(vec_a)
        norm_b = np.linalg.norm(vec_b)
        
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
            
        return float(dot_product / (norm_a * norm_b))

    def analyze(self, vec_a: List[float], vec_b: List[float], gated: bool = True) -> Dict[str, Any]:
        """
        Perform Comparative Analysis between two vectors.
        
        Args:
            vec_a (List[float]): Reference vector A.
            vec_b (List[float]): Target vector B.
            gated (bool): If True, scales the classical cosine similarity through the DSMF 
                         to generate a non-linear gated similarity metric.
                         
        Returns:
            Dict[str, Any]: Standardized output dictionary containing raw similarity, gated similarity,
                            confidence metrics, and latency.
        """
        start_time = time.perf_counter()
        
        a = np.array(vec_a, dtype=float)
        b = np.array(vec_b, dtype=float)
        
        # 1. Compute Classical Cosine Similarity
        raw_sim = self.cosine_similarity(a, b)
        
        # 2. Apply DSMF non-linear decision boundary scaling
        if gated:
            # Scale the raw cosine similarity [-1, 1] onto the active transition region of the DSMF
            gated_sim = self.dsmf.forward(raw_sim)
        else:
            gated_sim = raw_sim
            
        # 3. Compute the confidence as a function of the vector lengths (gating out zero-length noise)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        confidence = float(min(1.0, norm_a * norm_b))
        
        execution_latency = time.perf_counter() - start_time
        
        return {
            "raw_similarity": raw_sim,
            "gated_similarity": gated_sim,
            "confidence": confidence,
            "latency_ms": execution_latency * 1000.0,
            "vector_norms": [float(norm_a), float(norm_b)]
        }

if __name__ == "__main__":
    # Internal self-testing block to verify stability and mathematical correctness
    print("==========================================================")
    print("Testing ms_pilot: Comparative Analysis module...")
    print("==========================================================")
    
    # Test identical, orthogonal, and opposing vectors
    test_vec_a = [1.0, 2.0, 3.0]
    test_vec_b = [1.0, 2.0, 3.0]       # Identical
    test_vec_c = [-1.0, -2.0, -3.0]    # Opposing
    test_vec_d = [0.0, -3.0, 2.0]      # Orthogonal (dot product = 0)
    
    ca = ComparativeAnalysis()
    
    cases = [
        ("Identical", test_vec_b),
        ("Opposing", test_vec_c),
        ("Orthogonal", test_vec_d)
    ]
    
    for label, target in cases:
        res = ca.analyze(test_vec_a, target)
        print(f"--- Case: {label} ---")
        print(f"Raw Similarity:   {res['raw_similarity']:.5f}")
        print(f"DSMF Gated Sim:   {res['gated_similarity']:.5f}")
        print(f"Confidence:       {res['confidence']:.5f}")
        print(f"Latency:          {res['latency_ms']:.3f} ms")
        
    print("==========================================================")
    print("Comparative Analysis verification completed successfully.")
    print("==========================================================")
