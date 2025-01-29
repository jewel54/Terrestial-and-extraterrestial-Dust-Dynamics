# examples/venus_simulation.py
from dust_dynamics.config import VenusConfig
from dust_dynamics.models import DustModel
from dust_dynamics.utils import DustVisualizer

def run_venus_simulation():
    """Example simulation for Venus conditions"""
    config = VenusConfig()
    model = DustModel(config)
    
    # Load Venus atmospheric data
    model.train('data/venus_measurements.csv')
    
    # Run simulation
    results = model.simulate(
        duration=3600,
        dt=0.1,
        initial_conditions={
            'velocity': [0, 0, 0],
            'pressure': 9.2e6,
            'concentration': 0.001,
            'temperature': 737,
            'humidity': 0.003
        }
    )
    
    # Visualize results
    visualizer = DustVisualizer()
    visualizer.plot_velocity_field(results)
    visualizer.create_interactive_plot(results)
    
    return results