import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(212) #to plot in a single figure , one in the top and other on the bottom
plt.plot(t1,f(t1),'bo') #bo is blue 'o'=circle are plotted
plt.subplot(211)
plt.plot(t2,np.cos(2*np.pi*t2),'r--') #r-- is red '-'=lines will get printed
plt.show()

    