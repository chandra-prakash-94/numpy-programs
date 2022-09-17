'''
*  Assignment 4 : Python Program to find Solutions for Systems of Linear Equations
*  Regd No.     : 22-27-04
*  Name         : Chandra Prakash
*  Date         : 17-09-2022
''' 
import numpy as np
a = np.array([[3,-2,5,0],
             [4,5,8,1],
             [1,1,2,1],
             [2,7,6,5]], float)
b = np.array([2,4,5,7], float)
c = np.array([b])
print("Given coefficient Matrix A is :")
print(a)
print("Given constant Matrix B is :")
print(c.T)
n = len(b)
x = np.zeros(n, float)

#Elimination
for k in range(n-1):
    if a[k, k] == 0:
        for j in range (n):
            a[k,j], a[k+1, j] = a[k+1, j], a[k,j]
        b[k], b[k+1] = b[k+1], b[k]
    for i in range(k+1, n):
        if a[i, k] == 0: continue
        fctr = a[k, k] / a[i, k]
        b[i] = b[k] - fctr*b[i]
        for j in range(k, n):
            a[i, j] = a[k, j] - fctr*a[i, j]
        
#Back-substitution
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    terms = 0
    for j in range(i+1, n):
        terms += a[i, j]*x[j]
    x[i] = (b[i] - terms)/a[i, i]

y=np.array([x])
print('The solution for the system of equations:')
print(y.T)





