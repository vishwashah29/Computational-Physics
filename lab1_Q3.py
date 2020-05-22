# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:32:46 2020

@author: VISHWA
"""

import cmath
import numpy as np 
import matplotlib.pyplot as plt

delt=0.01
xaf=[1]
xas=[1]
xat=[1]
xf=[1]
x1a=1
x2a=1
x3a=1
n=1
diff_e=[0]
diff_s=[0]
diff_t=[0]

steps=np.arange(0,2,delt)
for i in steps:

	x_a=x1a-(((x1a)*x1a)*delt)						     #Euler	
	xaf.append(x_a)
	x1a=x_a
	

	x_as= x2a-(((x2a)*x2a)*delt) + ((2*x2a)*(x2a*x2a)*delt*delt)/2			     #Second_der 
	xas.append(x_as)
	x2a=x_as
	

	x_at= x3a-(((x3a)*x3a)*delt) + ((2*x3a)*(x3a*x3a)*delt*delt)/2 + ((delt*delt*delt)*(((-x3a)*x3a*4*x3a*x3a)+((x3a*x3a*x3a*x3a)*(-2))))/6    #Third_der
	xat.append(x_at)
	x3a=x_at
	
	x_f=1/(1+n*delt)
	xf.append(x_f)
	n+=1

	
	diff_e.append(abs(x_f-x_a))
	diff_s.append(abs(x_f-x_as))
	diff_t.append(abs(x_f-x_at))

	

steps=np.append(steps,2)

#plt.subplot(2,1,1)
plt.plot(steps,diff_e,'r',label='euler')
plt.plot(steps,diff_s,'b',label='first der')
plt.plot(steps,diff_t,'g',label='second order')
plt.title("Difference between the exact result and the approximate results")
plt.xlabel("values of t")
plt.ylabel("Difference")
plt.legend(("Euler", "Second Order Der", "Third Order Der"))
plt.show()


#plt.legend((diff_e,diff_s,diff_t), ('Euler', 'Second Order', 'Third Order'))

#plt.subplot(2,1,2)
plt.plot(steps,xaf,'r',label='Analytical solution')
plt.plot(steps,xas,'g',label='Euler')
plt.plot(steps,xat,'b',label='First Der')
plt.plot(steps, xf,'y',label='second der')
plt.title("Function values- Analytical, Euler and Taylor")
plt.xlabel("values of t")
plt.ylabel("Function Value-x")
plt.legend(("Analytical Function","Euler", "Second Order Der", "Third Order Der"))
plt.show()
