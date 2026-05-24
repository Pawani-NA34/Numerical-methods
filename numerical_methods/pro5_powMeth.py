# DATE: 03/09/2025
import numpy as np
A= np.array([[6,1,1],
             [1,4,-1],
            [1,-1,5]], dtype=float)
x0= np.array([1,1,0], dtype=float)    # Don't take it as zero vector
x2= np.array([0,1,0], dtype= float)

def powMeth(A, x0):
    x= A @ x0       # @ is matrix multiplication operator
    n= np.size(A,0)
    tol= 1e-5
    for i in range(75):   # Randomly large enough number of iterations
        x= A @ x0         # x_{k+1}= A x_k 
        x_old= x0.copy()  # To check convergence
        #max = np.linalg.norm(x, ord=np.inf)
        maxval, index=0, 0
        for j in range (n):
            if (abs(x[j])>maxval):
                maxval= abs(x[j])
                index= j
        x0= x/x[index]  
        if np.linalg.norm(x0 - x_old, ord=np.inf)<tol:
            #print(f"Converged in {i+1}th iteration")
            break
    return maxval, x0
maxv, x0= powMeth(A, x0)
print("Max eigenvalue/ spectral radius: ", maxv,"\nEigenvector: ", x0/np.linalg.norm(x0))
print("By inverse power method: " )
if (np.linalg.det(A) !=0):
    Ainv= np.linalg.inv(A)
    minv, x2= powMeth(Ainv, x2) # minv = largest eigenvalue of A^{-1}
    print("Min eigenvalue: ", 1/minv, "\nEigenvector: ", x2/np.linalg.norm(x2))
print("Direct solution:--")
print(np.linalg.eig(A))  # To verify the result

l2A, v= powMeth( (A.T @ A), np.array([0,1,0], dtype= float))
print("L2 norm of A: ", np.sqrt(l2A),"\nDominant eigenvector, normalised: ", v/np.linalg.norm(v))