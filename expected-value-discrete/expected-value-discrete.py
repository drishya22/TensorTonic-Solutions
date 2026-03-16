import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code her
    if sum(p)!=1:
        raise ValueError("Incorrect probability distribution")
    expected=0
    for i in range(len(x)):
        expected+=x[i]*p[i]
    return expected
