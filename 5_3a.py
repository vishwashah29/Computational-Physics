import numpy as np 
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative

v0=700
g=9.8
b=4*(10**(-5))
i=30



x_euler1 = [[0] for y in range(7)]
y_euler1 = [[0] for y in range(7)]
y_analytical = [[0] for y in range(7)]
x_t=[[0] for y in range(7)]
y_t=[[0] for y in range(7)]


delta_theta=5
delta_t=0.01




steps=np.arange(30,56,delta_theta)
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
    y=0
    n=1
    for j in steps2:
        v_x=vx 
        vx=v_x
    
        v_y=vy - g*delta_t
        vy=v_y
        
        
        x_e= xe + vx*delta_t					     #Euler	
        x_euler1[N].append(x_e)
        xe=x_e
        
        
        y_e= ye + vy*delta_t	
        y_euler1[N].append(y_e)
        ye=y_e
        
        xt=v0*math.cos(theta)*n*delta_t
        yt=v0*math.sin(theta)*n*delta_t - (g*((n*delta_t)**2))/2
        x_t[N].append(xt)
        y_t[N].append(yt)
        n=n+1

        
        
        
    N+=1
    


steps2=np.append(steps2,100)
steps=np.append(steps,55)





    
plt.plot(x_euler1[0], y_euler1[0], 'b', label = '30')
plt.plot(x_t[0] , y_t[0], color='k', linestyle='dashed', label='30-A')
plt.plot(x_euler1[1],y_euler1[1],'g',label='35')
plt.plot(x_t[1] , y_t[1], color='g', linestyle='dashed', label='35-A')
plt.plot(x_euler1[2], y_euler1[2], 'y', label = '40')
plt.plot(x_t[2] , y_t[2], color='y', linestyle='dashed', label='40-A')
plt.plot(x_euler1[3],y_euler1[3],'k',label='45')
plt.plot(x_t[3] , y_t[3], color='k', linestyle='dashed', label='45-A')
plt.plot(x_euler1[4], y_euler1[4], 'c', label = '50')
plt.plot(x_t[4] , y_t[4], color='c', linestyle='dashed', label='50-A')
plt.plot(x_euler1[5],y_euler1[5],'m',label='55')
plt.plot(x_t[5] , y_t[5], color='m', linestyle='dashed', label='55-A')
plt.title("Function values - Euler")
plt.xlabel("x")
plt.ylabel("Function Value-y")
plt.legend(("30","30-A", "35", "35-A",  "40", "40-A","45","45-A", "50","50-A", "55","55-A"))
plt.show()





