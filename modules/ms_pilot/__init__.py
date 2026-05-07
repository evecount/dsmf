"""
ms_pilot Cognitive Vector Engine - Module Initializer
Part of the Hybrid Quantum-Classical Intelligence Framework

Co-Created by Gwendalynn Lim Wan Ting & Gemini
Compiled & Maintained within the Antigravity IDE

This package exposes the core components of the ms_pilot suite:
- DimensionalAnalysis: Decoupling dense vectors into independent coordinate axes.
- ComparativeAnalysis: High-performance state-aware Cosine Similarity with DSMF gating.
- CreativeSynthesis: Smooth vector blending using Lerp and Slerp.
- TrajectoryPrediction: Adaptive Anticipation back-engineering human positional sequence (RoPE).
"""

from modules.ms_pilot.dimensional_analysis import DimensionalAnalysis
from modules.ms_pilot.comparative_analysis import ComparativeAnalysis
from modules.ms_pilot.creative_synthesis import CreativeSynthesis
from modules.ms_pilot.trajectory_prediction import TrajectoryPrediction

__all__ = [
    "DimensionalAnalysis",
    "ComparativeAnalysis",
    "CreativeSynthesis",
    "TrajectoryPrediction"
]
