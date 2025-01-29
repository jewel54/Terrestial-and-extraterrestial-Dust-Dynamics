from .base_config import BaseConfig

class MarsConfig(BaseConfig):
    """Mars-specific configuration"""
    def __init__(self):
        super().__init__(
            nu=6.5e-4,    # kinematic viscosity
            rho=0.020,    # atmospheric density
            g=3.71,       # gravity
            D=0.35,       # diffusion coefficient
            kappa=0.41,   # von Karman constant
            z0=0.03,      # roughness length
            dt=0.1,
            dx=0.1
        )
        self.pressure_base = 600  # Pa
        self.temperature_base = 210  # K
        self.humidity_base = 0.0001