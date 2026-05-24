# RK 4 method for solving ODEs
import numpy as np
def f(x,y):
    return y-x
n= int(input("Number of strips: "))
yrk4=np.zeros(n+1, dtype='float')
yrk2=np.zeros(n+1, dtype='float')
x0= float(input("Give x0: "))
yrk4[0]=yrk2[0]= float(input(f"Give y({x0})= "))
xn= float(input("Give xn: "))
h= (xn-x0)/n
for i in range (n):
    x= x0 + i*h 
    k1= h* f(x, yrk2[i])
    k2= h* f(x+h, yrk2[i]+k1)
    yrk2[i+1]= yrk2[i] + (1/2)*(k1 + k2)
print("y values using RK2 are: ", yrk2)
for i in range(n):
    k1= h* f(x0,yrk4[i])
    k2= h*f(x0+ (h/2), yrk4[i]+(k1/2))
    k3= h*f(x0+(h/2), yrk4[i]+(k2/2))
    k4= h*f(x0+h, yrk4[i]+k3)
    yrk4[i+1]= yrk4[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    x0+= h
print("y values are: ",yrk4)