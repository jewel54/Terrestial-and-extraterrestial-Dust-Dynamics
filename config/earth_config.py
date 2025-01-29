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
