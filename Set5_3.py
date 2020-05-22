import numpy as np 
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative

v0=700
g=9.8

def function1(theta,x):
    function=math.tan((theta*math.pi)/180)- ((g*x)/((v0**2)*(math.cos((theta*math.pi)/180)**2)))
    return function

y0=0
x_euler=[y0]
xe=y0
x_analytical_function=[y0]

delta_theta=5
delta_x=0.1

n=1

steps=np.arange(30,55,delta_theta)
steps2=np.arange(0,100,delta_x) 
i=30
#for i in steps:
for j in steps2:
    x_e=xe+function1(i,xe)*n*delta_x						     #Euler	
    x_euler.append(x_e)
    xe=x_e

    x_f=math.tan((i*math.pi)/180)*j - (g*(j**2)*(1/(math.cos(i*(math.pi)/180)**2)))/(2*v0**2)   #analytical without air drag
    x_analytical_function.append(x_f)
    n+=1

steps2=np.append(steps2,100)
    
   
	
#steps=np.append(steps,55)



plt.plot(steps2,x_euler,'g',label='Euler')
plt.plot(steps2,x_analytical_function,'r',label='Analytical Function')
plt.title("Function values- Euler and Analytical")
plt.xlabel("Values of x")
plt.ylabel("Function Value-y")
plt.legend(("Euler", "Analytical"))
plt.show()

