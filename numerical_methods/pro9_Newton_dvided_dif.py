# DATE: 24-09-2025
# Newton's Divided Difference Interpolation
import numpy as np
X= np.array([-1,0,1,2])
Y= np.array([5,1,1,11])
a=np.zeros(len(X))
n=len(Y)
y=np.zeros((n,n))
y[:,0]=Y
for j in range (1,n):
    for i in range (n-j):  # Rows decrease as j increases
        y[i][j]= (y[i+1][j-1]-y[i][j-1])/(X[i+j]-X[i])
print(y)
a=y[0,:]
poly=np.poly1d([a[0]])
pro=1
for i in range(1,n):
    pro= pro* np.poly1d([1,-X[i-1]])
    poly= poly+ a[i]*pro
print(poly)
print("P(1.5)= ",poly(1.5))