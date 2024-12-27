# Import Libraries
from typing import Callable
import numpy as np
import matplotlib.pyplot as plt


# Base Simulator Class (for generic simulation purposes)
class Simulator:
    """
    Generic base class for simulations
    """
    
    def __init__(self, eom: Callable, inputs: list, name: str
    ) -> None:
        """All simulations require a total simulation time (T), and a number of time steps(N)

        """
        # Assign the variables
        
        # Set a name for the simulation
        self.name = name
        
        # Simulation must follow a equation of motion (initialise an empty variable)
        self.eom = eom
        
        # Simulations must have input variables (initialise empty variable)
        self.inputs = inputs
        
        return None
    
    
    # A run function
    def simulate(self, T: float, N: int, y0: float) -> tuple:
        # time step
        dt = T / N
        
        # Create the time simulation
        t_vals = np.linspace(0, self.T, self.N + 1)
        
        # Y values and initialise with starting value
        v_vals = [y0]
        
        
        
        