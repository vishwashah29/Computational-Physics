# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:42:26 2020

@author: VISHWA
"""

import numpy as np 
import math
import matplotlib.pyplot as plt
import sympy as sym
from sympy import symbols
from scipy.misc import derivative
x=symbols('x')

def function1(x,t):
    function = -x + math.sin(4*math.pi*t)
    return function
    
def function2(x,t):
    function= 4*math.pi*math.cos(4*math.pi*t) - (-x + math.sin(4*math.pi*t))
    return function


#def function2_secondderivative(x):
#    functionder=sym.diff(-(x**2))#0.25*x*(1 - (0.05*x)))
#    return functionder
#
#def function3_thirdderivative(x):
#    functionder=sym.diff(sym.diff(-(x**2)))#0.25*x*(1 - (0.05*x))))
#    return functionder

delta_t=0.01

x_euler=[0.5]
x_second=[0.5]
#x_third=[1]

x_analytical_function=[0.5]

xe=0.5
te=0
xs=0.5
ts=0
#xt=2

n=1

diff_e=[0]
diff_s=[0]
#diff_t=[0]

steps=np.arange(0,1,delta_t)
for i in steps:
    
    x_e=xe+function1(xe,te)*delta_t						     #Euler	
    x_euler.append(x_e)
    xe=x_e
    te=te+delta_t
    print(x_e)
    
    x_s = xs + (function1(xs,ts)*delta_t) + ((function2(xs,ts))*(delta_t**2))/2 #((function2_secondderivative(xs)*(delta_t**2))/2) 		     #Second_der
    x_second.append(x_s)
    xs=x_s
    ts=ts+delta_t
    print(x_s)

#    x_t = xt + function1(xt)*delta_t + (derivative(function1,xt)*function1(xt)*(delta_t**2))/2 + ((derivative(function1,xt)*derivative(function1,xt)*function1(xt) + function1(xt)*function1(xt)*derivative(function1,xt,n=2))*(delta_t**3))/6 # ((function2_secondderivative(xt)*(delta_t**2))/2) + ((function3_thirdderivative(xt)(delta_t**2))/2)	     #Third_der
#    x_third.append(x_t)
#    xt=x_t
##    print(x_t)
#    
    x_f= (math.exp(-n*delta_t)*(0.5+8*((math.pi)**2)+4*math.pi) + (math.sin(4*math.pi*n*delta_t)) - (math.cos(4*math.pi*n*delta_t)*4*math.pi))/(1 + 16*(math.pi**2))
    x_analytical_function.append(x_f)
    n=n+1
    
    
    print(x_f)
    #print(x_f-x_s)
    #print(x_f-x_t)
#    
    diff_e.append((x_f-x_e))
    diff_s.append((x_f-x_s))
#    diff_t.append(abs(x_f-x_t))

	

steps=np.append(steps,1)


plt.plot(steps,diff_e,'r',label='euler')
plt.plot(steps,diff_s,'b',label='second der')
#plt.plot(steps,diff_t,'g',label='third order')
plt.title("Difference between the exact result and the approximate results")
plt.xlabel("values of t")
plt.ylabel("Difference")
plt.legend(("Euler", "Second Order Derivative"))
plt.show()




plt.plot(steps,x_analytical_function,'r',label='Analytical solution')
plt.plot(steps,x_euler,'g',label='Euler')
plt.plot(steps,x_second,'b',label='Second Der')
#plt.plot(steps, x_third,'y',label='Third der')
plt.title("Function values- Analytical, Euler and Taylor")
plt.xlabel("values of t")
plt.ylabel("Function Value-x")
plt.legend(("Analytical", "Euler", "Second Order Derivative"))
plt.show()