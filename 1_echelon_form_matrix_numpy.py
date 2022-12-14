'''
*  Assignment 1 : Python Program to compute echelon form for given matrix (Alternate method)
*  Regd No.     : 22-27-04
*  Name         : Chandra Prakash
*  Date         : 05-09-2022
''' 

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

    # Now, we add all subsequent rows elements, with first row elements multiplied by the multiplier m, so to make first element of below rows 0
    for j in range(1,len(A)):
        m = (-1)*(A[j,0]/A[0,0])
        A[j] = np.add(A[j],m * A[0])
        
    # Now, we perform REF on matrix from second row and from second column
    B = row_echelon(A[1:,1:])

    # Finally, we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])


""" Example """
A = np.array([[1,2,-3,-1],[-3,1,-2,-7],[5,3,-4,2]], float)

print("Given Matrix A is :")
print(A)
row_echelon(A)
print("Echelon form is: ")
print(A)

