import numpy as np
from typing import String

class Distribution:
    def __init__(self, type : String, **kwargs):
        
        self.type = type.lower()
        self.args = kwargs

        if self.type == "normal":
            self.dist = np.random.normal(**kwargs)
        else:
            raise ValueError("Unknown distribution type: " + type)

    def sample(self, n=1):
        return self.dist(self.args, n)