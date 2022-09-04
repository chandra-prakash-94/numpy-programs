""" Python program to return Upper and Lower Triangular matrix for given matrix A """
""" Author: Chandra Prakash, M Tech (Data Science), DIAT Pune- Batch 22-24

import numpy as np
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]], dtype='float')

r, c = A.shape             # store no. of rows and columns of the Matrix in the variables r and c resp.
 
if r!=c:                   # if the matrix is non-square matrix, then we exit the program
    print("Please enter a square Matrix!!")
    print("Now exiting the program....")
    exit()

else:
    print("Given Matrix is: ")
    print(A)

    n= np.shape(A)[0]       #storing no. of rows of given square matrix in variable n
    L = np.identity(n)      #initialising lower triangular matrix, with identity matrix of order n
    for k in range(n-1):
        for i in range(k+1,n,1):
            mult = A[i,k]/A[k,k]
            L[i,k] = mult   #storing the multiplier values in the Lower Triangular Matrix
            for j in range(k,n,1):
                A[i,j] -= mult*A[k,j]

    print("Upper Triangular Matrix is: ")
    print(A)
    print("Lower Triangular Matrix is: ")
    print(L)


