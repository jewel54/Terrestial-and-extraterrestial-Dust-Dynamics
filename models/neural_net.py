# models/neural_net.py
import torch
import torch.nn as nn
from typing import List, Optional

class DustFeedbackNetwork(nn.Module):
    """Neural network for modeling dust feedback mechanisms"""
    
    def __init__(self, 
                 input_size: int,
                 hidden_sizes: List[int],
                 output_size: int,
                 dropout: float = 0.1):
        super().__init__()
        
        layers = []
        prev_size = input_size
        
        # Build hidden layers
        for hidden_size in hidden_sizes:
            layers.extend([
                nn.Linear(prev_size, hidden_size),
                nn.ReLU(),
                nn.BatchNorm1d(hidden_size),
                nn.Dropout(dropout)
            ])
            prev_size = hidden_size
        
        # Output layer
        layers.append(nn.Linear(prev_size, output_size))
        
        self.network = nn.Sequential(*layers)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)