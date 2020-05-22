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

delta=0.1
x=1
steps1=np.arange(1,50,delta)

x_dot=[function1(1)]
for i in steps1:
	xdot=function1(x) 
	x_dot.append(xdot)
	x=x+delta
steps1=np.append(steps1,50)


plt.plot(steps1,x_dot,'b',label="v-vdot")
plt.title("Plot of v vs. vdot")
plt.xlabel("Values of v")
plt.ylabel("Values of vdot")
plt.show()

x0=15

x_euler=[x0]
x_second=[x0]
x_third=[x0]


xe=x0
xs=x0
xt=x0
delta_t=1
n=1
steps=np.arange(0,50,delta_t)

for i in steps:
    
    x_e=xe+function1(xe)*delta_t						     #Euler	
    x_euler.append(x_e)
    xe=x_e
#    print(x_e)
    
    x_s = xs + (function1(xs)*delta_t) + (derivative(function1,xs)*function1(xs)*(delta_t**2))/2 		     #Second_der
    x_second.append(x_s)
    xs=x_s
#    print(x_s)

    x_t = xt + function1(xt)*delta_t + (derivative(function1,xt)*function1(xt)*(delta_t**2))/2 + ((derivative(function1,xt)*derivative(function1,xt)*function1(xt) + function1(xt)*function1(xt)*derivative(function1,xt,n=2))*(delta_t**3))/6 	     #Third_der
    x_third.append(x_t)
    xt=x_t
#    print(x_t)
    
   
	

steps=np.append(steps,50)



plt.plot(steps,x_euler,'g',label='Euler')
plt.plot(steps,x_second,'b',label='Second Der')
plt.plot(steps, x_third,'y',label='Third der')
plt.title("Function values- Euler and Taylor")
plt.xlabel("Values of t")
plt.ylabel("Function Value-v")
plt.legend(("Euler", "Second Order Derivative", "Third Order Derivative"))
plt.show()

