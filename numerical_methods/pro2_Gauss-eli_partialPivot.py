# DATE: 13/08/2025
# AIM: Gauss Elimination Method (+ Partial Pivoting)
import numpy as np
A = np.array([[2,1,1], [3,2,3], [1,4,9]], dtype=float)
b= np.array([10,18,16], dtype=float)
n= np.size(A, 0)  # Number of rows (Here n=3)
aug= np.column_stack((A, b))
print("n: ",n)
sol = np.linalg.solve(A, b)
print(f"The solution of the system by inbuilt func: {sol}")
for c in range(0, n):  # i=0,1,...,n-1 (Here i=0,1,2)
    pivot_row = c+ np.argmax(abs(aug[c:n, c]))    # Find pivot row
    print(f"Pivot row for column {c} is {pivot_row}")
    print(aug[pivot_row, :])
    aug[[c,pivot_row]]= aug[[pivot_row, c]]       # Swap row c with pivot row
    for r in range (c+1, n):
        aug[r,:]= aug[r,:] - ((aug[r,c]/aug[c,c]) * aug[c,:])
print("Augmented matrix [A|b]:\n", aug)
print("Solution from Gauss elimination:")
A= aug[:, :-1]          # All rows, all columns except the last
b= aug[:, -1]           # Last column
# Back substitution
X= np.zeros( n, dtype=float)
for r in range(n-1, -1, -1):
    s=0
    for c in range(r+1, len(X)):
        s+= A[r, c] * X[c]
    if A[r, r]==0:
        print("No unique solution exists")
        exit()
    X[r]= (b[r] -s) / A[r, r]    
print("X now= ",X)