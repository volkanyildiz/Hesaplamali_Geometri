
# coding: utf-8

# In[37]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[38]:


point1 = np.array([0,0,0])
#x=1 y=-2 z=1 --> originden geçen normal, meshgrid yapısı oluşturuyoruz
normal1 = np.array([1,-2,1])


# In[39]:


point2 = np.array([0,-4,0])
normal2 = np.array([1,2,-8])
point3 = np.array([0,0,1])
normal3 = np.array([-4,5,9])
d1 = -np.sum(point1*normal1) 
d2 = -np.sum(point2*normal2)
d3 = -np.sum(point3*normal3)


# In[40]:


xx, yy = np.meshgrid(range(5), range(5)) #meshgrid

z1 = (-normal1[0]*xx - normal1[1]*yy -d1)*1./normal1[2]
get_ipython().run_line_magic('matplotlib', 'inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color='blue')


# In[41]:


#Sin(t) ve Cos(t)

n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
x = np.sin(theta)
y =  np.cos(theta)
z =  theta
ax.plot(x, y, z, 'b', lw=2)


# In[42]:


ax.set_axis_off()
plt.show()

