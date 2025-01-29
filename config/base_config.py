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

# config/earth_config.py
from .base_config import BaseConfig

class EarthConfig(BaseConfig):
    """Earth-specific configuration"""
    def __init__(self):
        super().__init__(
            nu=1.5e-5,
            rho=1.225,
            g=9.81,
            D=0.1,
            kappa=0.41,
            z0=0.01,
            dt=0.1,
            dx=0.1
        )
        self.pressure_base = 101325  # Pa
        self.temperature_base = 288  # K
        self.humidity_base = 0.5