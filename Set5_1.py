import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative

p=400
m=70
v0=2
row=1.25
b=0.5
A=0.33
def function1(v):
    function=((p/(m*v)) - (b*row*A*(v**2))/m)
    return function
   


delta_t=0.1

x_euler=[v0]
x_second=[v0]
x_third=[v0]

x_analytical_function=[v0]

xe=v0
xs=v0
xt=v0

n=1



steps=np.arange(0,50,delta_t)
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

   
    x_f=math.sqrt((v0**2)+((2*p*n*delta_t)/m))   #analytical without air drag
    x_analytical_function.append(x_f)
    n+=1
   
 


   

steps=np.append(steps,50)



plt.plot(steps,x_analytical_function,'r',label='Analytical solution ')
plt.plot(steps,x_euler,'g',label='Euler ')
plt.plot(steps,x_second,'b',label='Second Der')
plt.plot(steps, x_third,'y',label='Third der')
plt.title("Function values- Analytical, Euler and Taylor")
plt.xlabel("Values of t")
plt.ylabel("Function Value-v")
plt.legend(("Analytical without drag", "Euler with drag", "Second Order Der with drag", "Third Order Der with drag"))
plt.show()

