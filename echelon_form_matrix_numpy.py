""" Python program to return Row Echelon Form of given matrix A """

import numpy as np

def row_echelon(A):

    r, c = A.shape                # store no. of rows and columns of the Matrix in the variables r and c resp. 
    
    if r == 0 or c == 0:          # if the matrix A has no columns or rows, it is already in REF, so we return the matrix itself
        return A

    # Now, we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        B = row_echelon(A[:,1:])   # if all elements in the first column is zero, we perform REF on matrix from second column

        # And then adding the first zero-column back
        return np.hstack([A[:,:1], B])

    # if non-zero element is not in the first row, we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # We divide first row by the first element in it
    A[0] = A[0] / A[0,0]
    # And then, we subtract all subsequent rows with first row (it has 1 now as first element), multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # Now, we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # Finally, we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])

""" Example """

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

row_echelon(A)
print(A)