import scipy.integrate as inte
import numpy as np
def f1(x):
    return (np.cos(x)**2) #cos^2(x)
def f2(x):
    return 1/(1+(x**2))   # 1/(1+(x**2))
def f3(x):
    return np.exp(-x*x)    # e^(-x^2)
a1,b1= 0, np.pi/4
a2,b2 = -1,1
a3,b3= -100,100
n=999
def integrate(f,a,b,n):
    h=(b-a)/n
    t=0
    od, ev= 0, 0
    xi=a
    for i in range (1,n):
        xi+= h
        t+= f(xi)
        if (i%2==0):
            ev+= f(xi)
        else:
            od+= f(xi)
    if n%3 !=0:
        simp38= "Simpson's 3/8 rule not applicable for n not multiple of 3"
    else:
        s1,s2,xi=0,0,a
        for i in range (1,n):
            xi= a+ i*h
            if i%3==0:
                s2+= f(xi)
            else:
                s1+= f(xi)
        simp38= (3*h/8)*(f(a)+f(b)+ (3*s1)+(2*s2))
    trap=(h/2)*(f(a)+ f(b)+ (2*t) )
    simp=(h/3)*(f(a)+ f(b) + (2*ev)+(4*od))   
    print("Trapezoidal ",trap,"\nSimpson 1/3: ", simp,"\nSimpson's 3/8: ",simp38,"\nActual: ", inte.quad(f,a,b)[0])  # inbuilt integrate.quad(func, start, stop)
print(f"Integral of function cos^2(x) from {a1} to {b1} for n={n}:")
integrate(f1,a1,b1,n)
print(f"\nIntegral of function 1/(1+x^2) from {a2} to {b2} for n={n}:")
integrate(f2,a2,b2,n)
print(f"\nIntegral of function e^(-x^2) from {a3} to {b3} for n={n}:")
integrate(f3,a3,b3,n)
# absc=np.array(np.linspace(a,b,100))
# ord= f(absc)
# print(type(absc), type(ord))
# plt.title("Function plot")
# plt.plot(absc,ord )
# plt.show()