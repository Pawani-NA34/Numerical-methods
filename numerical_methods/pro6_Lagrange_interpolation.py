# DATE: 17-09-2025
# Lagrange Polynomial Interpolation
import numpy as np

# given x values
x= [11,12,13,14,15]
# function values at given x values
fx= [np.sin(np.radians(i)) for i in x]
# initializing the polynomial to zero
p=0
# number of data points
n=len(x)

x0=float(input("Enter the value of x0: "))

for i in range (n):
    L=1     # Lagrange basis polynomial
    for j in range (n):
        if j!=i:
            L=L*(np.poly1d([1, -x[j]])/(x[i]-x[j]))
    # adding the contribution of the i-th term to the polynomial
    p= p+ (L)*fx[i]
    
print("The polynomial is: \n",p)
# evaluating the polynomial at x0
print("The value of f(",x0,") is: ",p(x0))