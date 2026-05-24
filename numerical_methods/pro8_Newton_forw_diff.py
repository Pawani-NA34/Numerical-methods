# DATE: 24-09-2025
# Newton's Forward Difference Interpolation
import numpy as np
X= np.array([-1,0,1,2])
Y= np.array([5,1,1,11])
n=len(Y)
y=np.zeros((n,n))
y[:,0]=Y
for j in range(1,n):    # column
    for i in range (n-j): # row 
        y[i][j]= y[i+1][j-1]-y[i][j-1]
print(y)
poly= np.poly1d([y[0][0]])
h= X[1]-X[0]     # assuming equispaced data
p= np.poly1d([1/h,-X[0]/h])
f=1
pro=np.poly1d([1])
#print("p: ", p,"pro: ",pro)
for i in range(1,n):
    pro=pro * (p-(i-1))
    f= f*i                  # factorial
    poly= poly + ( y[0][i] * pro)/f
print(poly)
print("P(1.5)= ",poly(1.5))