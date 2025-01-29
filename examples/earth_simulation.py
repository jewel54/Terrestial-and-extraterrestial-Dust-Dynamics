# examples/earth_simulation.py
from dust_dynamics.config import EarthConfig
from dust_dynamics.models import DustModel
from dust_dynamics.utils import DustVisualizer

def run_earth_simulation():
    """Example simulation for Earth conditions"""
    # Initialize configuration
    config = EarthConfig()
    
    # Create model
    model = DustModel(config)
    
    # Load and train on Earth data
    model.train('data/earth_measurements.csv')
    
    # Run simulation
    results = model.simulate(
        duration=3600,  # 1 hour simulation
        dt=0.1,
        initial_conditions={
            'velocity': [0, 0, 0],
            'pressure': 101325,
            'concentration': 0.001,
            'temperature': 288,
            'humidity': 0.5
        }
    )
    
    # Visualize results
    visualizer = DustVisualizer()
    visualizer.plot_velocity_field(results)
    visualizer.create_interactive_plot(results)
    
    return results

if __name__ == '__main__':
    results = run_earth_simulation()