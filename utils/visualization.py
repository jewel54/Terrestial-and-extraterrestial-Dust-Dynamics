# utils/visualization.py
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from typing import Dict

class DustVisualizer:
    """Visualization tools for dust dynamics"""
    
    @staticmethod
    def plot_velocity_field(results: Dict):
        """Plot 3D velocity field"""
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot velocity vectors
        ax.quiver(results['x'], results['y'], results['z'],
                 results['v_x'], results['v_y'], results['v_z'])
        
        plt.show()
    
    @staticmethod
    def create_interactive_plot(results: Dict):
        """Create interactive plotly visualization"""
        fig = go.Figure(data=[go.Scatter3d(
            x=results['x'],
            y=results['y'],
            z=results['z'],
            mode='markers',
            marker=dict(
                size=results['concentration'] * 50,
                color=results['temperature'],
                colorscale='Viridis',
            )
        )])
        
        fig.show()
