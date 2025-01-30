from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class BaseConfig:
    """Base configuration class with common parameters"""
    nu: float  # kinematic viscosity
    rho: float  # density
    g: float   # gravity
    D: float   # diffusion coefficient
    kappa: float  # von Karman constant
    z0: float  # roughness length
    dt: float  # time step
    dx: float  # spatial step
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'BaseConfig':
        return cls(**config_dict)
