'''
*  Assignment 2 : LU decomposition- Python Program to compute upper triangular matrix for given non-singular matrix
*  Regd No.     : 22-27-04
*  Name         : Chandra Prakash
*  Date         : 10-09-2022
''' 
import numpy as np
a = np.array([[1,2,-3],
             [-3,-4,13],
             [2,1,-5]], float)

print("Given Matrix A is :")
print(a)

try:
    if np.linalg.det(a)==0:        # if the matrix is singular matrix, then we exit the program
        print("Error !! Please enter non-singular matrix")
        print("Closing the program ....")
    if np.linalg.det(a)!=0:        # if the matrix is non-singular matrix, then we compute upper triangular matrix
        n = a.shape[0]             # store order of the square matrix in 'n'

        for k in range(n-1):
            if a[k, k] == 0:
                for j in range (n):
                    a[k,j], a[k+1, j] = a[k+1, j], a[k,j]
            for i in range(k+1, n):
                if a[i, k] == 0: continue
                fctr = a[i, k]/a[k, k]
                for j in range(k, n):
                    a[i, j] -= fctr*a[k, j]
                
        print("Upper triangular Matrix is : ")
        print(a)

except:
    print("Error !! Please enter non-singular square matrix")
    print("Closing the program ....")


