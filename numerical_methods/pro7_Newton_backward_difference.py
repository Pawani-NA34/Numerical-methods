#DATE: 17-09-2025
# Newton's Backward Difference Interpolation
import numpy as np
X= np.array([-1,0,1,2])
Y= np.array([5,1,1,11])
n=len(Y)
y=np.zeros((n,n))
for i in range(n):
    y[i][0]=Y[i]
for i in range(1,n):
    for j in range(i,n):
            y[j][i]=y[j][i-1]-y[j-1][i-1]
print(y)          # y is nxn matrix

h= X[1]-X[0]     # assuming equispaced data
p= np.poly1d([1,-X[-1]])/h 
poly=np.poly1d([y[n-1,0]])
f=1
pro=np.poly1d([1])
#print("p: ", p,"pro: ",pro)
for i in range (1, n):
    f= f*i                  # factorial
    pro= pro* (p+(i-1))     # p(p+1)(p+2) for i=3 & so on
    poly= poly+ pro*(y[n-1,i]/f)
print (poly)
print("P(1.5)= ",poly(1.5))
 