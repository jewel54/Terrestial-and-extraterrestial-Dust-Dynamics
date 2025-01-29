# core/validation.py
from typing import Dict, Any
import numpy as np

class ModelValidator:
    """Validation utilities for dust dynamics model"""
    
    @staticmethod
    def validate_input_data(data: Dict[str, Any]) -> bool:
        """Validate input data structure and values"""
        required_fields = ['velocity', 'pressure', 'temperature', 
                         'humidity', 'concentration']
        
        # Check required fields
        if not all(field in data for field in required_fields):
            raise ValueError(f"Missing required fields: {required_fields}")
        
        # Validate physical constraints
        if data['pressure'] <= 0:
            raise ValueError("Pressure must be positive")
        
        if data['temperature'] <= 0:
            raise ValueError("Temperature must be positive")
        
        if not 0 <= data['humidity'] <= 1:
            raise ValueError("Humidity must be between 0 and 1")
        
        if data['concentration'] < 0:
            raise ValueError("Concentration must be non-negative")
        
        return True
    
    @staticmethod
    def validate_simulation_results(results: Dict[str, Any]) -> bool:
        """Validate simulation results for physical consistency"""
        # Check for NaN values
        if np.any(np.isnan(results['velocity'])):
            raise ValueError("NaN values detected in velocity field")
        
        # Check conservation of mass
        if not np.isclose(np.sum(results['concentration']), 
                         results['initial_concentration'], rtol=1e-3):
            raise ValueError("Mass conservation violated")
        
        return True