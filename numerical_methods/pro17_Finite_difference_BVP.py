# DATE: 06-10-2025
# AIM: Finite Difference Method for Solving ODEs, for BVP
# y'' + (4x/(1+x^2)) y' + (2/(1+x^2)) y = 0 (=r(x))
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 4*x/(1+x**2)
def g(x):
    return 2/(1+x**2)

n=int(input("Enter the value of n: "))
x0=float(input("Enter the value of x0: "))
y0=float(input("Enter the value of y0: "))
xn=float(input("Enter the value of xn: "))
yn=float(input("Enter the value of yn: "))
h=(xn-x0)/n
A= np.zeros((n+1,n+1), dtype=float)
B= np.zeros((n+1), dtype=float)
Y= np.zeros((n+1), dtype=float)
for i in range (n+1):  # loop will run n+1 times
    if i==0:
        A[0][0]=1
        B[0]=y0
    elif i==n:
        A[n][n]=1
        B[n]=yn
    else:
        fi= f(x0+i*h)
        gi = g(x0+i*h)
        A[i][i-1]= (1/h**2)-(fi/(2*h))
        A[i][i]= gi- (2/h**2)
        A[i][i+1]= (1/h**2)+(fi/(2*h))
        B[i]= 0
# Solving AX=B: A=LU; L
n= np.size(A,0)  # new n= n+1
L= np.zeros((n+1,n+1), dtype=float)
U= np.zeros((n+1,n+1), dtype=float)
for i in range(n):  # Decomposition using Crout's method
    L[i,0]= A[i,0]
for j in range(n):
    U[0,j]= A[0,j]/L[0,0]
for k in range(1, n):
    for i in range(k-1, n):
        L[i,k]= A[i,k] - np.dot(L[i,:k], U[:k,k])
    for j in range(k, n):
        U[k,j]= (1/L[k,k]) * (A[k,j]- np.dot(L[k, :k], U[:k,j]))
# forward substitution (LY=B)
for r in range(0, n):
    s=0
    for c in range(0, r):
        s+= L[r, c] * Y[c]
    Y[r]= (B[r] -s) / L[r, r]   
# back substitution  (UX=Y)
X= np.zeros(n, dtype=float)
for r in range (n-1, -1, -1):
    s=0
    for c in range(r+1, n):
        s+= U[r, c] * X[c]
    X[r]= (Y[r] -s) / U[r, r]
print("X \n", X)

plt.plot(np.linspace(x0, xn, n), X, marker='o', label="FDM Solution", markersize=0.5, color='magenta')
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Solution of BVP using Finite Difference Method")
plt.grid()
plt.show()
plt.legend()
plt.grid()