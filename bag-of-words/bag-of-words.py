import numpy as np
from collections import Counter

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    freq=Counter(tokens)
    return np.array([freq.get(word,0) for word in vocab],dtype=int)