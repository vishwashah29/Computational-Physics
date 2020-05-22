import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import symbols
import math
from scipy.misc import derivative

A= 0.03
B= 3*(10**(-12))
def f(x):
    function=A*x - (B*(x**2))
    return function

def f_2(x):
    function=A-2*b*x
    return function

def f_3(x):
    function=-2*B
    

delta_t=0.01

x_euler=[3*(10**9)]
x_second=[3*(10**9)]
x_third=[3*(10**9)]

x_analytical_function=[3*(10**9)]

xe=3*10**9
xs=3*10**9
xt=3*10**9

n=1

diff_e=[0]
diff_s=[0]
diff_t=[0]

steps=np.arange(0,100,delta_t)
for i in steps:

    x_e=xe + f(xe)*delta_t     #Euler
    x_euler.append(x_e)
    xe=x_e
   # print(x_e, "x_e")
   

    x_s = xs + f(xs)*delta_t + (f(xs)*(A-2*B*xs)*delta_t**2)/2     #Second_der
    x_second.append(x_s)
    xs=x_s
   # print(x_s, "x_s")
       
    x_t = xt + f(xt)*delta_t  + (f(xt)*(A-2*B*xt)*delta_t**2)/2  + ((f(xt)*((A-2*B*xt)**2)) + (f(xt)**2)*(-2*B))/6  #Third_der
    x_third.append(x_t)
    xt=x_t
  #  print(x_t, "x_t")
   


    x_f= (0.42857*(math.exp(0.03*n*delta_t))/(1+0.42857*math.exp(0.03*n*delta_t)))*(10**10)
    x_analytical_function.append(x_f)
    n+=1
   # print(x_f, "x_f")

    diff_e.append(x_f-x_e)
    diff_s.append(x_f-x_s)
    diff_t.append(x_f-x_t)
   # print(x_f - x_e, "diff e")
   # print(x_f - x_s, "diff s")
   # print(x_f - x_t, "diff t")
   



steps=np.append(steps,100)

plt.plot(steps,diff_e,'r',label='euler')
plt.plot(steps,diff_s,'b',label='second der')
plt.plot(steps,diff_t,'g',label='third order')
plt.title("3.Difference- Euler and Taylor")
plt.xlabel("t")
plt.ylabel("Difference")
plt.legend(("Euler", "Second Order Der", "Third Order Der"))
plt.show()



plt.plot(steps,x_analytical_function,'r',label='Analytical solution')
plt.plot(steps,x_euler,'g',label='Euler')
plt.plot(steps,x_second,'b',label='Second Der')
plt.plot(steps, x_third,'y',label='Third der')
plt.title("3.Function values- Analytical, Euler and Taylor")
plt.xlabel("t")
plt.ylabel("Function Value")
plt.legend(("Analytical function","Euler", "Second Order Der", "Third Order Der"))
plt.show()
