# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:18:00 2020

@author: VISHWA
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative


def function1(x):
    function= -(0.0315) *x
    return function
   


delta_t=0.10

x_euler=[1]
x_second=[1]
x_third=[1]

x_analytical_function=[1]

xe=1
xs=1
xt=1

n=1



steps=np.arange(0,2,delta_t)
for i in steps:
   
    x_e=xe+function1(xe)*delta_t                             #Euler   
    x_euler.append(x_e)
    xe=x_e
  
   
    x_s = xs + (function1(xs)*delta_t) + (derivative(function1,xs)*function1(xs)*(delta_t**2))/2         #Second_der
    x_second.append(x_s)
    xs=x_s


    x_t = xt + function1(xt)*delta_t + (derivative(function1,xt)*function1(xt)*(delta_t**2))/2 + ((derivative(function1,xt)*derivative(function1,xt)*function1(xt) + function1(xt)*function1(xt)*derivative(function1,xt,n=2))*(delta_t**3))/6          #Third_der
    x_third.append(x_t)
    xt=x_t

   
    x_f=math.exp(-(0.0315)*n*delta_t)
    x_analytical_function.append(x_f)
    n+=1
   
 


   

steps=np.append(steps,2)



plt.plot(steps,x_analytical_function,'r',label='Analytical solution')
plt.plot(steps,x_euler,'g',label='Euler')
plt.plot(steps,x_second,'b',label='Second Der')
plt.plot(steps, x_third,'y',label='Third der')
plt.title("Function values- Analytical, Euler and Taylor")
plt.xlabel("Values of t")
plt.ylabel("Function Value-x")
plt.legend(("Analytical", "Euler", "Second Order Der", "Third Order Der"))
plt.show()

