import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    t=np.array(x)
    temp=1/(1+np.exp(-t))
    return t*temp