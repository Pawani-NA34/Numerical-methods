# DATE 20/08/2025
# AIM: LU Decomposition Method
import numpy as np
A= np.array([[1,4,3],
            [2,7,9],
            [5,8,-2]], dtype=float)
b= np.array([7,13,-3], dtype=float)
n= np.size(A,0)
L= np.zeros((n,n), dtype=float)
U= np.zeros((n,n), dtype=float)
# Decomposition into L and U using Crout's method
for i in range(n):
    L[i,0]= A[i,0]
for j in range(n):
    U[0,j]= A[0,j]/L[0,0]
for k in range(1, n):
    for i in range(k-1, n):  # i=k-1 to n-1
        L[i,k]= A[i,k] - np.dot(L[i,:k], U[:k,k])
    for j in range(k, n):    # j=k to n-1; 
        U[k,j]= (1/L[k,k]) * (A[k,j]- np.dot(L[k, :k], U[:k,j]))
print("L matrix:")
print(L)
print("U matrix:")
print(U)
# verification A=LU
P= np.zeros((n,n), dtype=float)
for i in range(n):
    for j in range(n):
        P[i,j]= np.dot(L[i,:], U[:,j])

Y= np.zeros(n, dtype=float)
# forward substitution (LY=b)
for r in range(0, n):
    s=0
    for c in range(0, r):
        s+= L[r, c] * Y[c]
    Y[r]= (b[r] -s) / L[r, r]   
print("Y \n",Y)

# back substitution  (UX=Y)
X= np.zeros(n, dtype=float)
for r in range (n-1, -1, -1):
    s=0
    for c in range(r+1, n):
        s+= U[r, c] * X[c]
    X[r]= (Y[r] -s) / U[r, r]
print("X \n", X)
print("Solution of the system:")
print(np.linalg.solve(A, b))
