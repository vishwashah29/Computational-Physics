import numpy as np 
import math
import matplotlib.pyplot as plt
import sympy as sym
from sympy import symbols
from scipy.misc import derivative
x=symbols('x')

A = 8.62    #g'=g(1-dl/ds)
B = 349.04  #k/m
    
def function1(v):
    function= (8.62) - ((349.04)*v)
    return function


delta_t=1

x_euler=[0]
x_second=[0]
x_third=[0]

x_analytical_function=[0]

xe=0
xs=0
xt=0

n=1

diff_e=[0]
diff_s=[0]
diff_t=[0]

steps=np.arange(0,100,delta_t)
for i in steps:
    
    x_e=xe+function1(xe)*delta_t						     #Euler	
    x_euler.append(x_e)
    xe=x_e
#    print(x_e)
    
    x_s = xs + (function1(xs)*delta_t) + (derivative(function1,xs)*function1(xs)*(delta_t**2))/2 #((function2_secondderivative(xs)*(delta_t**2))/2) 		     #Second_der
    x_second.append(x_s)
    xs=x_s
#    print(x_s)

    x_t = xt + function1(xt)*delta_t + (derivative(function1,xt)*function1(xt)*(delta_t**2))/2 + ((derivative(function1,xt)*derivative(function1,xt)*function1(xt) + function1(xt)*function1(xt)*derivative(function1,xt,n=2))*(delta_t**3))/6 # ((function2_secondderivative(xt)*(delta_t**2))/2) + ((function3_thirdderivative(xt)(delta_t**2))/2)	     #Third_der
    x_third.append(x_t)
    xt=x_t
#    print(x_t)
    
    x_f= (A*(1-math.exp(-B*n*delta_t)))/B
    x_analytical_function.append(x_f)
    n+=1
    
    #print(x_f-x_e)
    #print(x_f-x_s)
    #print(x_f-x_t)
    
    diff_e.append(x_f-x_e)
    diff_s.append(x_f-x_s)
    diff_t.append(x_f-x_t)

	

steps=np.append(steps,100)


plt.plot(steps,diff_e,'r',label='euler')
plt.plot(steps,diff_s,'b',label='second der')
plt.plot(steps,diff_t,'g',label='third order')
plt.title("Difference between the exact result and the approximate results")
plt.xlabel("values of t")
plt.ylabel("Difference")
plt.legend(("Euler", "Second Order Derivative", "Third Order Derivative"))
plt.show()




plt.plot(steps,x_analytical_function,'r',label='Analytical solution')
plt.plot(steps,x_euler,'g',label='Euler')
plt.plot(steps,x_second,'b',label='Second Der')
plt.plot(steps, x_third,'y',label='Third der')
plt.title("Function values- Analytical, Euler and Taylor")
plt.xlabel("values of t")
plt.ylabel("Function Value-x")
plt.legend(("Analytical", "Euler", "Second Order Derivative", "Third Order Derivative"))
plt.show()