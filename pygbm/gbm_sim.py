from typing import Callable

import numpy as np

from .simulator import Simulator

class GBMSimulator(Simulator):
    
    def __init__(self, mu: float, sigma: float) -> None:
        """
        Coefficients for Geometric Brownian Motion

        Args:
            mu (float): Mean
            sigma (float): Standard Deviation
        """
        self.mu = mu
        self.sigma = sigma
        self.eom = self._gbm
        
        
        
    @staticmethod
    def _gbm(dt: float, y_prev, mu, sigma) -> float:
        dB = np.random.normal(0, np.sqrt(dt))
        return y_prev * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * dB)