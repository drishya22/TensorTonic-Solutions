import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows=len(A)
    cols=len(A[0])
    mat=[[0 for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            mat[j][i]=A[i][j]
    return np.array(mat)