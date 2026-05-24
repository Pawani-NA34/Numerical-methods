# DATE: 01-10-2025
# AIM: To find optimal points of a function using Chebyshev polynomial
import numpy as np
n=int(input("To make nth degree polynomial, give n: "))
a=float(input("Give the interval [a,b] of the function y= sin(pi*x)\na:"))
b=float(input("b: "))
X=[]
p=(b-a)/2
q=(a+b)/2
X= np.array( [((p* np.cos(np.pi*(((2*i)+1)/(2*(n+1))))) +q ) for i in range (n+1)])
# for i in range (n+1):
#     xi= (p* np.cos(np.pi*(((2*i)+1)/(2*(n+1))))) +q
#     X.append(xi)
# X=np.array(X)
print(f"The {n+1} optimal points for y=sin(pi*x) :\n",X,"\nRespective y values are:")
Y= np.sin(X* np.pi)
print(Y)

a=np.zeros(len(X))
n=len(Y)
y=np.zeros((n,n))
y[:,0]=Y
for j in range (1,n):
    for i in range (n-j):
        y[i][j]= (y[i+1][j-1]-y[i][j-1])/(X[i+j]-X[i])
#print(y)
a=y[0,:]
poly=np.poly1d([a[0]])
pro=1
for i in range(1,n):
    pro= pro* np.poly1d([1,-X[i-1]])
    poly= poly+ a[i]*pro
print("\n--- Results ---")
print(f"Interpolating polynomial of degree {n-1}:")
print(poly)

print("\nEvaluation:")
print(f"P(1.5) = {poly(1.5)}")

print("\nRoots of the interpolating polynomial (approx zeros of P(x)):")
print(poly.roots)