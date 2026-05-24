import numpy as np
import math as mt
def f(x):
    return x*x
print("Integral of x^2 from -1 to 1 using Legendre Polynomials")
n= int(input("Give n: "))
if n%2 ==0:
    M= int(n/2)
else:
    M= int((n-1)/2)

coeff=np.zeros(n+1, dtype= float)
print(M)
for m in range(M+1):
    c= (-1)**m *mt.factorial(2*n-2*m)/(2**n*mt.factorial(m)*mt.factorial(n-m)*mt.factorial(n-2*m))
    coeff[n-(2*m)]= c
coeff=coeff[::-1]  # reversing the array
p= np.poly1d(coeff)
print("Legendre\n",p)
optim= p.roots
print("Roots:\n", optim)

A= np.zeros((n,n),dtype='double')
A[0,:]=1  # first column all 1s
for i in range (1,n):
    for j in range (n):
        A[i][j]=optim[i]**(j)

B_legen= np.zeros(n, dtype='double')
for i in range (n):
    if i%2==0:
        B_legen[i]= 2/(i+1)
    else:
        B_legen[i]=0
print("A:\n",A,"\nB:\n", B_legen)

if np.linalg.det(A)==0:
    print("Matrix is singular, cannot solve")
else:
    w1= np.linalg.solve(A, B_legen)
    print("Weights ",w1,"\nSum of weights= ", sum(w1))
    fixi=0
    for i in range (n):
        fixi+= w1[i]*f(optim[i])
    print("Approximate Integral= ", fixi)