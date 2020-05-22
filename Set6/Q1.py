import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative

   


delta_t=0.1

A=100
B=0

ta=1   #lambda=1/Ta
tb=1

x_euler_A=[100]
x_euler_B=[0]


n=1



steps=np.arange(0,5,delta_t)
for i in steps:
   
    x_A= A + ta*(B-A)*delta_t
    x_euler_A.append(x_A)
    
    
    x_B = B + (A - B)*delta_t*tb                             #Euler   
    x_euler_B.append(x_B)
    
    A=x_A
    B=x_B
    
  
steps=np.append(steps,5)



plt.plot(steps,x_euler_A,'r',label='Amount of x_A')
#plt.plot(steps,x_euler_B,'g',label='Amount of x_B ')
plt.title("Function values x_A with respect to time")
plt.xlabel("Time ")
plt.ylabel("Function Value")
plt.legend(("Amount of x_A"))
plt.show()



plt.plot(steps,x_euler_B,'b',label='Amount of x_B')
#plt.plot(steps,x_euler_B,'g',label='Amount of x_B ')
plt.title("Function value x_B with respect to time")
plt.xlabel("Time ")
plt.ylabel("Function Value")
plt.legend(("Amount of x_B"))
plt.show()


plt.plot(steps,x_euler_A,'r',label='Amount of x_A')
plt.plot(steps,x_euler_B,'g',label='Amount of x_B ')
plt.title("Function values- x_A and x_B with respect to time")
plt.xlabel("Time")
plt.ylabel("Function Value")
plt.legend(("Amount of x_A","Amount of x_B"))
plt.show()


plt.plot(x_euler_A,x_euler_B,'r',label='Amount of x_A w.r.t x_B')
plt.title("Function values- x_A w.r.t x_B")
plt.xlabel("x_A")
plt.ylabel("x_B")
plt.show()
