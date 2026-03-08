import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    def val(a):
        y=np.exp(a)
        v=np.exp(-a)
        z=(y-v)/(y+v)
        return z
    arr=np.array(x)
    return val(arr)