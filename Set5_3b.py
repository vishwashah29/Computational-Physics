import numpy as np 
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative

v0=700
g=9.8
b=4*(10**(-5))
i=30
theta=i*math.pi/180


x0=0
x_euler=[x0]
xe=x0

y0=0
y_euler=[y0]
ye=y0

vx=v0*math.cos(theta)
#v_eulerx=[v0*math.cos(theta)]

vy=v0*math.sin(theta)
#v_eulery=[v0*math.sin(theta)]

x_analytical_function=[y0]

delta_theta=5
delta_t=0.1

n=1

#steps=np.arange(30,55,delta_theta)
steps2=np.arange(0,70,delta_t) 

#for i in steps:
for j in steps2:
    v_x=v0*math.cos((i*math.pi)/180) - (b*vx*math.sqrt(vx**2+vy**2))*j
    vx=v_x
    
    v_y=v0*math.sin(i*math.pi/180) - (b*vy*math.sqrt(vx**2+vy**2))*j - g*j
    vy=v_y
    
    
    
    x_e=v0*math.cos(i*math.pi/180)*j - (b*vx*math.sqrt(vx**2+vy**2))*(j**2)/2					     #Euler	
    x_euler.append(x_e)
    xe=x_e
    
    y_e=v0*math.sin(i*math.pi/180)*j - (b*vy*math.sqrt(vx**2+vy**2))*(j**2)/2	- g*(j**2)/2	
    y_euler.append(y_e)
    ye=y_e	

    x_f=math.tan((i*math.pi)/180)*j - (g*(j**2)*(1/(math.cos(i*(math.pi)/180)**2)))/(2*v0**2)   #analytical without air drag
    x_analytical_function.append(x_f)
    n+=1

steps2=np.append(steps2,70)
    
   
	
#steps=np.append(steps,55)



plt.plot(x_euler,y_euler,'g',label='Euler')
plt.plot(steps2,x_analytical_function,'r',label='Analytical Function')
plt.title("Function values- Euler and Analytical")
plt.xlabel("Values of x")
plt.ylabel("Function Value-y")
plt.legend(("Euler", "Analytical"))
plt.show()

