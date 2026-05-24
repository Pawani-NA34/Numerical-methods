# DATE: 27/08/2025
# AIM: Gauss Seidel Iteration Method
import numpy as np
A= np.array([[10,3,1],
             [3,10,2],
             [1,2,10]], dtype= float)
b= np.array([19,29,35], dtype= float)
A= np.array([[4,3,-1],
             [3,7,3],
             [1,1,4]], dtype= float)
# A= np.array([[3,1,2],
#             [1,3,2],
#             [1,2,1] ], dtype= float)
# b= np.array([8,2,3], dtype=float)
n= np.size(A,0)
tol= 1e-5
X= np.zeros(n, dtype=float)
# for i in range(n):
#     for (A[i,i]< sum(abs(A[i,j]) for j in range(n) if j!=i)):
#         A[[i,i+1]]= A[[0,i]]
print(X)
for k in range(150):
    y= X.copy()
    for i in range (n):    # range(n)
        X[i]= ((b[i]) - np.dot(A[i, :i], X[:i]) - np.dot(A[i, i+1:], X[i+1:])) / A[i,i]
    # if max(abs( X[i] - y[i]) for i in range (n) )< tol:
    if np.linalg.norm(y - X, ord=np.inf)< tol:
        print(f"Converged in {k+1}th iteration")
        break
print("X: \n",X)
print("Direct solution:\n", np.linalg.solve(A,b))