# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:20:11 2020

@author: VISHWA
"""

import numpy as np
import math
import matplotlib.pyplot as plt

def function1(a):
    function=-9.8
    return function
   


delta_t1=0.1
delta_t2=0.01
delta_t3=0.001

x_euler1=[0]
x_euler2=[0]
x_euler3=[0]

x_analytical_function1=[0]
x_analytical_function2=[0]
x_analytical_function3=[0]

xe1=0
xe2=0
xe3=0

n=1

diff_e1=[0]
diff_e2=[0]
diff_e3=[0]

steps1=np.arange(0,10,delta_t1)                       #Step_1
for i in steps1:
   
    x_e1=xe1+function1(-9.8)*delta_t1                                
    x_euler1.append(x_e1)
    xe1=x_e1
    #print(xe1)

    x_f1=-9.8*n*delta_t1
    x_analytical_function1.append(x_f1)
    n+=1
   
    diff_e1.append((x_f1-x_e1))
   

steps1=np.append(steps1,10)


n=1                                #Step_2   
steps2=np.arange(0,10,delta_t2)
for i in steps2:
   
    x_e2=xe2+function1(-9.8)*delta_t2                            
    x_euler2.append(x_e2)
    xe2=x_e2
   # print(xe2)
    x_f2=-9.8*n*delta_t2
    x_analytical_function2.append(x_f2)
    n+=1
   
    diff_e2.append((x_f2-x_e2))
   

steps2=np.append(steps2,10)

n=1                                 #Step_3
steps3=np.arange(0,10,delta_t3)
for i in steps3:
   
    x_e3=xe3+function1(-9.8)*delta_t3                               
    x_euler3.append(x_e3)
    xe3=x_e3
   # print(xe3)
    x_f3=-9.8*n*delta_t3
    x_analytical_function3.append(x_f3)
    n+=1
   
    diff_e3.append((x_f3-x_e3))
   

steps3=np.append(steps3,10)


plt.plot(steps1,diff_e1,'r',label='Euler-1')
plt.plot(steps2,diff_e2,'g',label='Euler-2')
plt.plot(steps3,diff_e3,'b',label='Euler-3')

plt.title("Difference between the exact result and the approximate results using three different step sizes")
plt.xlabel("Values of t")
plt.ylabel("Difference")
plt.legend(("Step size = 0.1", "Step size = 0.01", "Step size = 0.001"))
plt.show()




plt.plot(steps3,x_analytical_function3,'y',label='Analytical solution')
plt.plot(steps1,x_euler1,'r',label='Euler-1')
plt.plot(steps2,x_euler2,'g',label='Euler-2')
plt.plot(steps3,x_euler3,'b',label='Euler-3')

plt.title("Function values- Analytical and Euler ")
plt.xlabel("Values of t")
plt.ylabel("Function Value-v")
plt.legend(("Analytical", "Euler-1", "Euler-2", "Euler-3"))
plt.show()