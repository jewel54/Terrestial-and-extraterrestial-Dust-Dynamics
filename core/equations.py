# core/equations.py
import numpy as np
from typing import Tuple, Dict
from dataclasses import dataclass

@dataclass
class State:
    """State variables for the dust dynamics system"""
    velocity: np.ndarray  # 3D velocity field
    pressure: float
    concentration: float
    temperature: float
    humidity: float

class DustEquations:
    """Core equations for dust dynamics"""
    
    @staticmethod
    def navier_stokes(state: State, config: Dict) -> np.ndarray:
        """Calculate Navier-Stokes terms"""
        return (-1/config.rho * np.gradient(state.pressure) +
                config.nu * np.gradient(np.gradient(state.velocity)) +
                config.g)
    
    @staticmethod
    def dust_transport(state: State, config: Dict) -> float:
        """Calculate dust transport equation terms"""
        return (config.D * np.gradient(np.gradient(state.concentration)) -
                np.dot(state.velocity, np.gradient(state.concentration)))
    
    @staticmethod
    def dust_feedback(state: State, config: Dict) -> np.ndarray:
        """Calculate dust feedback force"""
        kappa = config.coupling_coefficient
        v_dust = state.velocity  # Simplified
        alpha = config.thermal_coefficient
        beta = config.humidity_coefficient
        
        return (kappa * (v_dust - state.velocity) +
                alpha * np.gradient(state.temperature) +
                beta * np.gradient(state.humidity))
