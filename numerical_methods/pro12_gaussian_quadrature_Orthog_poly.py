# DATE: 08-10-2025
# AIM: 
# Gaussian Quadrature using Orthogonal Polynomials

# This program:
# 1. Constructs Legendre, Hermite, and Laguerre polynomials
# 2. Computes their roots
# 3. Calculates quadrature weights
# 4. Demonstrates Gaussian integration techniques
import numpy as np
import math as mt

n= int(input("Give n: "))
if n%2 ==0:
    M= int(n/2)
else:
    M= int((n-1)/2)

# Constructing the Legendre polynomial coefficients
coeff=np.zeros(n+1, dtype= float)
print(M)
for m in range(M+1):
    c= (-1)**m *mt.factorial(2*n-2*m)/(2**n*mt.factorial(m)*mt.factorial(n-m)*mt.factorial(n-2*m))
    coeff[n-(2*m)]= c
coeff=coeff[::-1]  # reversing the array

# Legendre polynomial
p= np.poly1d(coeff)
print("Legendre\n",p)
roots_legen= p.roots

# Constructing the Hermite polynomial coefficients
hcoeff=np.zeros(n+1, dtype= float)
for m in range(int(n/2)+1):
    c= (-1)**m *mt.factorial(n)* 2**(n-2*m)/(mt.factorial(m)*mt.factorial(n-2*m))
    hcoeff[n-(2*m)]= c
hcoeff=hcoeff[::-1]  # reversing the array

# Hermite polynomial
hermite_poly= np.poly1d(hcoeff)
print("Hermite\n",hermite_poly)
roots_herm= hermite_poly.roots

# Constructing the Laguerre polynomial coefficients
lcoeff=np.zeros(n+1, dtype= float)
for m in range(n+1):
    c= (-1)**m *mt.factorial(n)/((mt.factorial(m))**2*mt.factorial(n-m))
    lcoeff[m]= c
lcoeff=lcoeff[::-1]  # reversing the array

# Laguerre polynomial
lagurre_poly= np.poly1d(lcoeff)
print("Laguerre\n",lagurre_poly)
roots_lag= lagurre_poly.roots

# Constructing the Vandermonde matrix for Legendre 
A_legen= np.zeros((n,n),dtype='double')
for i in range (n):
    for j in range (n):
        A_legen[i][j]=roots_legen[i]**j
# Constructing the Vandermonde matrix for Hermite    
A_herm= np.zeros((n,n),dtype='double')
for i in range (n):
    for j in range (n):
        A_herm[i][j]=roots_herm[i]**j
# Constructing the Vandermonde matrix for Laguerre
A_lag= np.zeros((n,n),dtype='double')
for i in range (n):
    for j in range (n):
        A_lag[i][j]=roots_lag[i]**j

# Aw= B
B_legen= np.zeros(n, dtype='double')
B_herm= np.zeros(n, dtype='double')
B_lag= np.zeros(n, dtype='double')


for i in range (n):   # Legendre
    if i%2==0:
        B_legen[i]= 2/(i+1)
    else:
        B_legen[i]=0
for i in range (n):   # Hermite
    if i%2==0:
        B_herm[i]= mt.gamma((i+1)/2)
    else:
        B_herm[i]=0
for i in range (n):  # Laguerre
    B_lag[i]= mt.factorial(i)

# Legendre quadrature weights
print("\n--- Legendre Polynomial ---")
print(np.linalg.cond(A_legen))
w1= np.linalg.solve(A_legen, B_legen)
print("Weights:\n", w1)
print("Sum of weights (should be 2): ", np.sum(w1))

# Hermite quadrature weights
print("\n--- Hermite Polynomial ---")
print(np.linalg.cond(A_herm))
w2= np.linalg.solve(A_herm, B_herm)
print("Weights:\n", w2)
print("Sum of weights (should be sqrt(pi)): ", np.sum(w2))

# Laguerre quadrature weights
print("\n--- Laguerre Polynomial ---")
print(np.linalg.cond(A_lag))
w3= np.linalg.solve(A_lag, B_lag)
print("Weights:\n", w3)
print("Sum of weights (should be 1): ", np.sum(w3))