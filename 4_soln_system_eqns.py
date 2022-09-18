'''
*  Assignment 4 : Python Program to find Solutions for Systems of Linear Equations
*  Regd No.     : 22-27-04
*  Name         : Chandra Prakash
*  Date         : 17-09-2022
''' 
import numpy as np
a = np.array([[0,-1,-2],
             [1,0,3],
             [7,1,1]], float)
b = np.array([-8,2,0], float)
aug=np.column_stack((a,b))
b2 = np.array([b])
print("Given coefficient Matrix A is :")
print(a)
print("Given constant Matrix B is :")
print(b2.T)
n = len(b)
u = a.shape[1]
rnka= np.linalg.matrix_rank(a)
rnkag= np.linalg.matrix_rank(aug)
if rnka!=rnkag:
    print("No solutions exist for given system of linear equations!")
    print("Closing the program.....")
else:
    if rnka< u:
        print("Infinite solutions exist for given system of linear equations!")
        print("Closing the program.....")
    else:
        x = np.zeros(n, float)
        #Elimination
        for k in range(n-1):
            if a[k, k] == 0:
                for j in range (n):
                    a[k,j], a[k+1, j] = a[k+1, j], a[k,j]
                b[k], b[k+1] = b[k+1], b[k]
            for i in range(k+1, n):
                if a[i, k] == 0: continue
                fctr = a[i, k]/a[k, k]
                b[i] -= fctr*b[k]
                for j in range(k, n):
                    a[i, j] -= fctr*a[k, j]
                
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





