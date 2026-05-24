import numpy as np
from scipy.integrate import solve_ivp
# from scipy.integrate import 
# Example: y'' + (4x/(1+x^2))y' + (2/(1+x^2))y = 0
def f(x, Y):
    y1, y2 = Y
    dy1dx = y2
    dy2dx = -((4 * x / (1 + x**2)) * y2 + (2 / (1 + x**2)) * y1)
    return np.array([dy1dx, dy2dx])
def rk4(f, x0, y0, n):  
    h=(xn-x0)/n
    y= np.zeros((n+1, 2), dtype='float')
    y[0]=y0
    x= np.linspace(x0, xn, n+1)
    for i in range(n):
        k1= h*f(x0, y[i])
        k2= h*f(x0+(h/2),y[i]+(k1/2))
        k3= h*f(x0+(h/2),y[i]+(k2/2))
        k4= h*f(x0+h, y[i]+k3)
        y[i+1]= y[i]+ (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        x0+= h
    return x,y
def rk2(f, x0, y0, n):
    h=(xn-x0)/n
    y= np.zeros((n+1, 2), dtype='float')
    y[0]=y0
    x= np.linspace(x0, xn, n+1)
    for i in range(n):
        k1= h*f(x0, y[i])
        k2= h*f(x0+h, y[i]+k1)
        y[i+1]= y[i]+ (1/2)*(k1 + k2)
        x0+= h
    return x,y,x0
x0 = float(input("Enter starting x0: "))
y0 = float(input("Enter initial y(x0): "))
yprime = float(input(f"Enter initial y'({x0}): "))
xn = float(input("Enter ending xn (where to stop): "))
n=250
h=(xn-x0)/n
x=np.linspace(x0,xn, n+1)    # n+1 points make n subintervals
X1,Y1= rk4(f, x0, [y0, yprime], n)
X2,Y2,xi= rk2(f, x0, [y0, yprime], n)
print(f"y({x0 +n*h}) value using RK4 is: ",Y1[-1,0])
print(f"y({x0 +n*h}) value using RK2 is: ",Y2[-1,0])
sol= solve_ivp(f, [x0, xn], [y0, yprime], method='RK45', t_eval=x)
#print(f"The value of y at x = 20 is approximately: {sol.y[0, -1]}")
print(f"The value of y at x = 20 is approximately: {sol.y[0, np.argmin(np.abs(sol.t - 20))]}")