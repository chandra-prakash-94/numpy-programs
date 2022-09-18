'''
*  Assignment 1 : Python Program to compute echelon form for given matrix
*  Regd No.     : 22-27-04
*  Name         : Chandra Prakash
*  Date         : 05-09-2022
''' 
import numpy as np
a = np.array([[1,2,-3,-1],[-3,1,-2,-7],[5,3,-4,2]], float)

print("Given Matrix A is :")
print(a)
r,c = a.shape          # store no. of rows and columns of given matrix in r and c resp.

for k in range(r-1):
    if a[k, k] == 0:
        for j in range (c):
            a[k,j], a[k+1, j] = a[k+1, j], a[k,j]
    for i in range(k+1, r):
        if a[i, k] == 0: continue
        fctr = a[i, k]/a[k, k]
        for j in range(k, c):
            a[i, j] -= fctr*a[k, j]
        
print("Echelon Form is : ")
print(a)
