import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """ 
    def s(x):
        t=1/(1+(np.exp(-x)))
        return t
    y=np.array(x)
    return s(y)