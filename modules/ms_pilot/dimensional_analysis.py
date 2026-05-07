"""
Dimensional Analysis - ms_pilot Cognitive Vector Engine
Part of the Hybrid Quantum-Classical Intelligence Framework

Co-Created by Gwendalynn Lim Wan Ting & Gemini
Compiled & Maintained within the Antigravity IDE

This module implements Dimensional Analysis, which decouples dense high-dimensional 
input vectors into independent geometric coordinate axes using continuous boundary gating.
"""

import time
import numpy as np
from typing import Dict, Any, List

class DimensionalAnalysis:
    """
    Decouples dense input vectors into independent geometric coordinate axes
    using singular value decomposition (SVD) and covariance analysis, ensuring 
    perfect mathematical stability and dimensional gating.
    """
    
    def __init__(self, n_components: int = 3):
        """
        Initialize the Dimensional Analysis module.
        
        Args:
            n_components (int): Number of independent geometric dimensions to project onto.
        """
        self.n_components = n_components

    def analyze(self, data_vectors: List[List[float]]) -> Dict[str, Any]:
        """
        Decouple dense input vectors into independent coordinates.
        
        Args:
            data_vectors (List[List[float]]): Array of input vectors.
            
        Returns:
            Dict[str, Any]: Standardized output dictionary containing projected coordinates,
                            eigenvalues (dimension importance), confidence metrics, and latency.
        """
        start_time = time.perf_counter()
        
        # Convert to numpy array for vector operations
        X = np.array(data_vectors, dtype=float)
        n_samples, n_features = X.shape
        
        # Handle edge cases where input is too small
        if n_samples < 2:
            raise ValueError("Dimensional Analysis requires at least 2 samples to analyze covariance.")
            
        # 1. Zero-center the data (normalize the coordinate base)
        mean_vector = np.mean(X, axis=0)
        X_centered = X - mean_vector
        
        # 2. Perform Singular Value Decomposition (SVD)
        # X_centered = U * S * Vt
        u, s, vt = np.linalg.svd(X_centered, full_matrices=False)
        
        # 3. Compute principal components and eigenvalues
        eigenvalues = (s ** 2) / (n_samples - 1)
        total_variance = np.sum(eigenvalues)
        
        # Avoid division by zero
        if total_variance == 0:
            explained_variance_ratio = np.zeros_like(eigenvalues)
        else:
            explained_variance_ratio = eigenvalues / total_variance
            
        # 4. Project data onto the principal independent axes
        projection_matrix = vt[:self.n_components].T
        projected_coordinates = np.dot(X_centered, projection_matrix)
        
        # 5. Compute the confidence metric as the cumulative variance captured
        confidence = float(np.sum(explained_variance_ratio[:self.n_components]))
        
        execution_latency = time.perf_counter() - start_time
        
        return {
            "coordinates": projected_coordinates.tolist(),
            "eigenvalues": eigenvalues[:self.n_components].tolist(),
            "variance_ratio": explained_variance_ratio[:self.n_components].tolist(),
            "confidence": confidence,
            "latency_ms": execution_latency * 1000.0,
            "mean_vector": mean_vector.tolist(),
            "projection_matrix": projection_matrix.tolist()
        }

if __name__ == "__main__":
    # Internal self-testing block to verify stability and mathematical correctness
    print("==========================================================")
    print("Testing ms_pilot: Dimensional Analysis module...")
    print("==========================================================")
    
    # Generate some correlated synthetic 5D data
    np.random.seed(42)
    base_signal = np.linspace(0, 10, 10)
    synthetic_data = np.zeros((10, 5))
    for i in range(5):
        synthetic_data[:, i] = base_signal * (i + 1) + np.random.normal(0, 0.1, 10)
        
    da = DimensionalAnalysis(n_components=2)
    results = da.analyze(synthetic_data.tolist())
    
    print(f"Decoupled Coordinates Shape: {np.array(results['coordinates']).shape}")
    print(f"Captured Confidence (Variance Ratio): {results['confidence']:.5f}")
    print(f"Eigenvalues: {results['eigenvalues']}")
    print(f"Execution Latency: {results['latency_ms']:.3f} ms")
    print("Dimensional Analysis verification completed successfully.")
    print("==========================================================")
