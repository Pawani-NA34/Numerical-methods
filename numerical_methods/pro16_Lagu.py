import numpy as np
import math as mt
def f(x):
    return x*x
print("Integral of x^2 exp[-x] from 0 to +inf using Lagurre Polynomials")
n= int(input("Give n: "))
if n%2 ==0:
    M= int(n/2)
else:
    M= int((n-1)/2)

lcoeff=np.zeros(n+1, dtype= float)
for m in range(n+1):
    c= (-1)**m *mt.factorial(n)/((mt.factorial(m))**2*mt.factorial(n-m))
    lcoeff[m]= c
print(lcoeff)
lcoeff=lcoeff[::-1]  # reversing the array
l= np.poly1d(lcoeff)

print("Lagurre\n",l)
optim= l.roots
print("Roots:\n", optim)

A= np.zeros((n,n),dtype='double')
A[0,:]=1  # first column all 1s
for i in range (1,n):
    for j in range (n):
        A[i][j]=optim[j]**(i)

B_lag= np.zeros(n, dtype='double')
for i in range (n):
    B_lag[i]= mt.gamma(i+1)
print("A:\n",A,"\nB:\n", B_lag)

if np.linalg.det(A)==0:
    print("Matrix is singular, cannot solve")
else:
    w2= np.linalg.solve(A, B_lag)
    print("Weights ",w2,"\nSum of weights= ", sum(w2))
    fixi=0
    for i in range (n):
        fixi+= w2[i]*f(optim[i])
    print("Approximate Integral= ", fixi)