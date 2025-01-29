# data/loader.py
import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional
from pathlib import Path

class DataLoader:
    """Data loading and validation utilities"""
    
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
    
    def load_measurement_data(self, 
                            filename: str, 
                            date_range: Optional[Tuple[str, str]] = None) -> pd.DataFrame:
        """Load and validate measurement data"""
        filepath = self.data_dir / filename
        
        if filepath.suffix == '.csv':
            data = pd.read_csv(filepath, parse_dates=['timestamp'])
        elif filepath.suffix in ['.xlsx', '.xls']:
            data = pd.read_excel(filepath, parse_dates=['timestamp'])
        else:
            raise ValueError(f"Unsupported file format: {filepath.suffix}")
        
        # Filter by date range if provided
        if date_range:
            start_date, end_date = pd.to_datetime(date_range)
            data = data[(data['timestamp'] >= start_date) & 
                       (data['timestamp'] <= end_date)]
        
        return data
    
    def load_configuration(self, planet: str) -> Dict:
        """Load planet-specific configuration"""
        config_path = self.data_dir / 'configs' / f'{planet.lower()}_config.json'
        
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration not found for planet: {planet}")
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        return config