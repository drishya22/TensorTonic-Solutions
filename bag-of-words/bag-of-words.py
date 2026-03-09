import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    result=[]
    for i in vocab:
        result.append(tokens.count(i))
    return np.array(result,dtype="int")