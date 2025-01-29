# config/venus_config.py
from .base_config import BaseConfig

class VenusConfig(BaseConfig):
    """Venus-specific configuration"""
    def __init__(self):
        super().__init__(
            nu=3.2e-7,    # kinematic viscosity
            rho=65.0,     # atmospheric density
            g=8.87,       # gravity
            D=0.05,       # diffusion coefficient
            kappa=0.41,   # von Karman constant
            z0=0.005,     # roughness length
            dt=0.1,
            dx=0.1
        )
        self.pressure_base = 9.2e6  # Pa
        self.temperature_base = 737  # K
        self.humidity_base = 0.003