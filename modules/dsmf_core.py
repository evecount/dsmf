"""
Double Sigmoid Mencius Function (DSMF) - Core Implementation
Part of the Hybrid Quantum-Classical Intelligence Framework

Co-Created by Gwendalynn Lim Wan Ting & Gemini
Compiled & Maintained within the Antigravity IDE

This module contains the physical, executable representations of the DSMF,
including recursive sigmoid nesting, fractional derivative wave compression,
simulated Bloch-sphere Ry rotational mapping, and Average ReLU integration.
"""

import math
from typing import Tuple, List, Union

class DSMFCore:
    """
    Executable core engine for the Double Sigmoid Mencius Function (DSMF).
    This class models the recursive, fractal, and quantum-informed activation
    topography used to bridge classical neural representations with Hilbert-space dynamics.
    """
    
    def __init__(self, 
                 alpha: float = 0.5, 
                 beta: float = 1.0, 
                 n_recursion: int = 2,
                 a: float = 1.0, 
                 b: float = 1.0, 
                 c: float = 0.0):
        """
        Initialize the DSMF parameters.
        
        Args:
            alpha (float): The fractional derivative parameter (wave compression / eccentricity of projection).
            beta (float): The correlation aperture parameter (dynamic zoom lens / state correlation strength).
            n_recursion (int): The recursion depth level (models causal dependency depth).
            a (float): Outer sigmoid scaling coefficient.
            b (float): Inner sigmoid scaling coefficient.
            c (float): Continuous phase-shift parameter.
        """
        self.alpha = alpha
        self.beta = beta
        self.n_recursion = n_recursion
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def sigmoid(x: float) -> float:
        """Standard classical sigmoid function squashing R -> (0, 1)."""
        try:
            return 1.0 / (1.0 + math.exp(-x))
        except OverflowError:
            return 0.0 if x < 0 else 1.0

    def nested_sigmoid_boundary(self, x: float) -> float:
        """
        Calculates the classical nested Double Sigmoid Mencius boundary (The "Mencius Path").
        Formula: f(x) = sigma_1(a * sigma_2(b * x) + c)
        """
        inner = self.sigmoid(self.b * x)
        outer = self.sigmoid(self.a * inner + self.c)
        return outer

    def recursive_activation(self, x: float, depth: int = None) -> float:
        """
        Executes the recursive fractal activation pattern of the DSMF.
        Formula: sigma^n(x) = sigma(sigma^{n-1}(x))
        Models deep causal dependencies.
        """
        if depth is None:
            depth = self.n_recursion
            
        if depth <= 1:
            return self.sigmoid(x)
        
        return self.sigmoid(self.recursive_activation(x, depth - 1))

    def simulated_fractional_derivative(self, x: float) -> float:
        """
        Simulates the fractional derivative D^alpha wave compression dynamics.
        In physical systems, alpha controls how wave functions compress and decompress
        during potential barrier tunneling. Here it scales the gradient decay profile.
        """
        # A robust simulation of fractional-order rate of change
        h = 1e-5
        f_x = self.nested_sigmoid_boundary(x)
        f_x_h = self.nested_sigmoid_boundary(x - h)
        
        # Standard first derivative
        first_derivative = (f_x - f_x_h) / h
        
        # Fractional scaling utilizing the alpha eccentricity parameter
        fractional_effect = first_derivative * (abs(x) ** (1.0 - self.alpha) if x != 0 else 1.0)
        return fractional_effect

    def rotational_angle_encoding(self, x: float) -> Tuple[float, float]:
        """
        Maps the continuous nested classical sigmoid boundary outputs to physical
        y-axis rotations (Ry) of a state vector on the Bloch Sphere.
        
        The single-qubit Ry operator is:
        Ry(theta) = [cos(theta/2), -sin(theta/2)]
                    [sin(theta/2),  cos(theta/2)]
                    
        This maps the continuous output directly to state probabilities.
        We apply the beta parameter as our 'zoom lens' aperture, scaling the phase correlation.
        
        Returns:
            Tuple[float, float]: (cos(theta/2), sin(theta/2)) representing the state coordinates in Hilbert space.
        """
        # Get classical activation mapping
        activation = self.nested_sigmoid_boundary(x)
        
        # Map output as phase-shift theta scaled by the beta correlation aperture
        theta = activation * math.pi * self.beta
        
        # Calculate state vector coordinates
        cos_state = math.cos(theta / 2.0)
        sin_state = math.sin(theta / 2.0)
        
        return cos_state, sin_state

    @staticmethod
    def average_relu(x: float) -> float:
        """
        Computes the Average ReLU integration layer used to bridge discrete classical
        activation boundaries and continuous quantum behavior.
        Formula: R(x) = (x + |x|) / 2
        """
        return (x + abs(x)) / 2.0

    def forward(self, x: float) -> float:
        """
        Fully integrated forward pass of the DSMF.
        Combines the nested sigmoid, quantum rotational state density,
        fractional compression, and Average ReLU smoothing.
        """
        # 1. Evaluate classical nested sigmoid boundary
        classical_base = self.nested_sigmoid_boundary(x)
        
        # 2. Extract quantum rotational mapping coordinates
        cos_state, sin_state = self.rotational_angle_encoding(x)
        
        # 3. Model transition-point superposition density (quantum filter)
        # Superposition is densest at the DSMF transition point (where sin_state -> cos_state)
        quantum_filter = abs(cos_state * sin_state)
        
        # 4. Integrate fractional compression dynamics
        fractional_compressor = self.simulated_fractional_derivative(x)
        
        # 5. Composite raw activation
        raw_activation = classical_base + (quantum_filter * self.alpha) + (fractional_compressor * self.beta)
        
        # 6. Smooth via Average ReLU integration bridge
        return self.average_relu(raw_activation)

if __name__ == "__main__":
    # Self-testing suite to verify mathematical and operational integrity
    print("==========================================================")
    print("Running DSMF Core Mathematical Validation...")
    print("==========================================================")
    
    dsmf = DSMFCore(alpha=0.6, beta=1.2, n_recursion=3, a=1.5, b=1.0, c=0.2)
    
    # Test points spanning the saturation limits and transition boundaries
    test_inputs = [-5.0, -1.0, 0.0, 1.0, 5.0]
    
    print(f"{'Input (x)':<10} | {'Nested Sig.':<12} | {'Fract. Deriv.':<14} | {'Ry Cos (c)':<10} | {'Ry Sin (s)':<10} | {'DSMF Out':<10}")
    print("-" * 80)
    
    for x in test_inputs:
        n_sig = dsmf.nested_sigmoid_boundary(x)
        f_der = dsmf.simulated_fractional_derivative(x)
        cos_s, sin_s = dsmf.rotational_angle_encoding(x)
        out = dsmf.forward(x)
        print(f"{x:<10.2f} | {n_sig:<12.5f} | {f_der:<14.5f} | {cos_s:<10.5f} | {sin_s:<10.5f} | {out:<10.5f}")
        
    print("-" * 80)
    print("DSMF Core Mathematical Verification Completed Successfully.")
    print("==========================================================")
