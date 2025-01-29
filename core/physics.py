# core/physics.py
import numpy as np
from typing import Dict, Tuple
from dataclasses import dataclass

@dataclass
class PhysicalConstants:
    """Physical constants for dust dynamics"""
    k_boltzmann: float = 1.380649e-23  # Boltzmann constant
    r_gas: float = 8.31446  # Gas constant
    stefan_boltzmann: float = 5.670374419e-8  # Stefan-Boltzmann constant

class PhysicsEngine:
    """Core physics calculations"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.constants = PhysicalConstants()
    
    def calculate_reynolds_number(self, velocity: float, length: float) -> float:
        """Calculate Reynolds number"""
        return (velocity * length) / self.config.nu
    
    def calculate_particle_settling_velocity(self, 
                                          particle_diameter: float, 
                                          particle_density: float) -> float:
        """Calculate particle settling velocity using Stokes law"""
        g = self.config.g
        mu = self.config.nu * self.config.rho
        return (particle_density * g * particle_diameter**2) / (18 * mu)
    
    def calculate_threshold_friction_velocity(self, 
                                           particle_diameter: float,
                                           particle_density: float) -> float:
        """Calculate threshold friction velocity for particle uplift"""
        a = 0.1  # empirical constant
        return np.sqrt(
            (particle_density - self.config.rho) * 
            self.config.g * particle_diameter / 
            (self.config.rho * a)
        )