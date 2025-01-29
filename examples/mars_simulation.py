# examples/mars_simulation.py
from dust_dynamics.config import MarsConfig
from dust_dynamics.models import DustModel
from dust_dynamics.utils import DustVisualizer

def run_mars_simulation():
    """Example simulation for Mars conditions"""
    config = MarsConfig()
    model = DustModel(config)
    
    # Load Mars atmospheric data
    model.train('data/mars_measurements.csv')
    
    # Run simulation
    results = model.simulate(
        duration=3600,
        dt=0.1,
        initial_conditions={
            'velocity': [0, 0, 0],
            'pressure': 600,
            'concentration': 0.001,
            'temperature': 210,
            'humidity': 0.0001
        }
    )
    
    # Visualize results
    visualizer = DustVisualizer()
    visualizer.plot_velocity_field(results)
    visualizer.create_interactive_plot(results)
    
    return results