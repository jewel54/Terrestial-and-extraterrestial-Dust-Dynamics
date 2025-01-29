# data/preprocessor.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List, Optional

class DataPreprocessor:
    """Data preprocessing pipeline"""
    
    def __init__(self):
        self.scalers = {}
    
    def process_file(self, filepath: str) -> Tuple[pd.DataFrame, Dict]:
        """Process input file (CSV or Excel)"""
        if filepath.endswith('.csv'):
            data = pd.read_csv(filepath)
        else:
            data = pd.read_excel(filepath)
        
        return self.preprocess_data(data)
    
    def preprocess_data(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, Dict]:
        """Main preprocessing pipeline"""
        # Handle missing values
        data = self._handle_missing_values(data)
        
        # Scale features
        scaled_data = self._scale_features(data)
        
        # Calculate derived features
        derived_features = self._calculate_derived_features(data)
        
        # Combine all features
        final_data = pd.concat([scaled_data, derived_features], axis=1)
        
        return final_data, self.scalers