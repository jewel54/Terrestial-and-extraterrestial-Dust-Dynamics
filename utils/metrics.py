# utils/metrics.py
import numpy as np
from typing import Dict, List
from sklearn.metrics import mean_squared_error, r2_score

class ModelMetrics:
    """Evaluation metrics for dust dynamics model"""
    
    @staticmethod
    def calculate_metrics(predictions: Dict[str, np.ndarray],
                        ground_truth: Dict[str, np.ndarray]) -> Dict[str, float]:
        """Calculate model performance metrics"""
        metrics = {}
        
        # Calculate RMSE for each variable
        for var in predictions.keys():
            metrics[f'{var}_rmse'] = np.sqrt(
                mean_squared_error(ground_truth[var], predictions[var])
            )
            metrics[f'{var}_r2'] = r2_score(
                ground_truth[var], predictions[var]
            )
        
        # Calculate conservation metrics
        metrics['mass_conservation_error'] = np.abs(
            np.sum(predictions['concentration']) - 
            np.sum(ground_truth['concentration'])
        ) / np.sum(ground_truth['concentration'])
        
        return metrics
    
    @staticmethod
    def generate_report(metrics: Dict[str, float]) -> str:
        """Generate human-readable performance report"""
        report = "Model Performance Report\n"
        report += "=" * 30 + "\n\n"
        
        for metric, value in metrics.items():
            report += f"{metric}: {value:.4f}\n"
        
        return report