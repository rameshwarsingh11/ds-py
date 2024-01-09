#Matplot lib usages in Python
import numpy as np
import matplotlib.pyplot as plt

plt.show()

x = np.linspace(0,5,11)
y = x ** 2
print(x)
print(y)

# Functional Method
plt.plot(x,y)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Sample Graph')
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()

# Object Oriented Method
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X values')
axes.set_ylabel('Y values')
axes.set_title('Sample Graph')
fig.show()


#Embedded graph styles
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes2.plot(y,x)

axes2.set_title('Smaller Plot')
axes1.set_title('Larger Plot')
fig.show()
