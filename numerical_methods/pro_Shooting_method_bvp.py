# DATE: 22-09-2025
# AIM: Shooting Method for BVP
import numpy as np
import matplotlib.pyplot as plt

# y'' + (4x/(1+x^2)) y' + (2/(1+x^2)) y = 0
# Let y1 = y, y2 = y'
# Then: y1' = y2, y2' = -(4x/(1+x^2)) y2 - (2/(1+x^2)) y1

def f(x, Y):
    y, z = Y
    dydx = z
    #dzdx = -(4*x/(1+x**2))*z - (2/(1+x**2))*y
    dzdx = (np.pi**2)*y - (2*(np.pi**2)*np.sin(np.pi*x))
    return np.array([dydx, dzdx])

def rk4(x0, Y0, xn, n, f):
    h = (xn - x0)/n
    x = np.zeros(n+1)
    Y = np.zeros((n+1, len(Y0)))
    x[0] = x0
    Y[0] = Y0
    for i in range(n):
        k1 = h * f(x[i], Y[i])
        k2 = h * f(x[i]+h/2, Y[i]+k1/2)
        k3 = h * f(x[i]+h/2, Y[i]+k2/2)
        k4 = h * f(x[i]+h, Y[i]+k3)
        Y[i+1] = Y[i] + (k1+2*k2+2*k3+k4)/6
        x[i+1] = x[i] + h
    return x, Y   # return x and y (not y') OR Y[:,1] for y'
# Input values
x0 = float(input("Enter starting x0: "))
y0 = float(input("Enter initial y(x0): "))
xn = float(input("Enter ending xn: "))
yn = float(input(f"Enter y({xn}): "))
aprox1 = float(input(f"Enter initial guess for y'({x0}): "))
aprox2 = float(input(f"Enter second guess for y'({x0}): "))
n = 100
tol = 1e-6
# Shooting iteration
iter=0
while (iter<50):
    # Solve with first guess
    _, y1 = rk4(x0, [y0, aprox1], xn, n, f)
    err1 = y1[-1][0] - yn
    # Solve with second guess
    _, y2 = rk4(x0, [y0, aprox2], xn, n, f)
    err2 = y2[-1][0] - yn
    # Check tolerance
    if abs(err1) < tol:
        slope = aprox1
        ysol = y1
        break
    if abs(err2) < tol:
        slope = aprox2
        ysol = y2
        break
    # Secant method update
    new_approx = aprox2 - err2*(aprox2 - aprox1)/(err2 - err1)
    aprox1, aprox2 = aprox2, new_approx
    iter += 1
print(f"Initial slope that satisfies BC: {slope:.6f}")
x, y_final = rk4(x0, [y0, slope], xn, n, f)
print("iter. ", iter)
plt.plot(x, y_final[:,0], label="y(x) Shooting Method")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Solution of BVP using Shooting Method with RK4")
plt.legend()
plt.grid()
plt.show()