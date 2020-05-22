import numpy as np 
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative

v0=700
g=9.8
b=4*(10**(-5))
i=30



x_euler1 = [[0] for y in range(6)]
y_euler1 = [[0] for y in range(6)]


delta_theta=5
delta_t=0.01


steps=np.arange(30,55,delta_theta)
steps2=np.arange(0,100,delta_t) 
N=0
for i in steps:
    theta=i*math.pi/180
    vx=v0*math.cos(theta)
    vy=v0*math.sin(theta)
    x_e=0
    y_e=0
    x_euler=[0]
    y_euler=[0]
    xe=0
    ye=0
    for j in steps2:
        v_x=vx - (b*vx*math.sqrt(vx**2+vy**2))*delta_t
        vx=v_x
        
        v_y=vy - (b*vy*math.sqrt(vx**2+vy**2))*delta_t - g*delta_t
        vy=v_y
        
        
        x_e= xe + vx*delta_t					     #Euler	
        x_euler1[N].append(x_e)
        xe=x_e
      
        
        y_e= ye + vy*delta_t	
        y_euler1[N].append(y_e)
        ye=y_e
      

        
    N+=1
    
    





    
plt.plot(x_euler1[0], y_euler1[0], 'b', label = '30')
plt.plot(x_euler1[1],y_euler1[1],'g',label='35')
plt.plot(x_euler1[2], y_euler1[2], 'y', label = '40')
plt.plot(x_euler1[3],y_euler1[3],'k',label='45')    
plt.plot(x_euler1[4], y_euler1[4], 'c', label = '50')
plt.plot(x_euler1[5],y_euler1[5],'m',label='55')
plt.title("Function values - Euler")
plt.xlabel("x")
plt.ylabel("Function Value-y")
plt.legend(("30", "35", "40", "45", "50", "55"))
plt.show()


steps2=np.append(steps2,100)
steps=np.append(steps,55)