import scipy as sp
from scipy.integrate import odeint
import matplotlib.pylab as plt
import numpy as np
import math


G=6.674*10**-11 #(N*m^2)/kg^2
Mt=5.972*10**24 #kg
r=7071000 #m
O=7.27*10**-5 #rad/s


def satelite(z,t):
    R=[[math.cos(O*t), -math.sin(O*t), 0], [math.sin(O*t), math.cos(O*t), 0], [0, 0, 1]]
    Rp=np.dot([[-math.sin(O*t), -math.cos(O*t), 0], [math.cos(O*t), -math.sin(O*t), 0], [0, 0, 0]],O)
    Rpp=np.dot([[-math.cos(O*t), math.sin(O*t), 0], [-math.sin(O*t), -math.cos(O*t), 0], [0, 0, 0]],O**2)
    zp=sp.zeros(6)
    zp[0:3]=z[3:6]
    zp[3:6]=((-G*Mt*z[0:3])/(r**3))-np.dot(np.transpose(R),(np.dot(Rpp,z[0:3])+2*np.dot(Rp,z[3:6])))
    return zp

t=sp.linspace(0, 14400, 14401)
z0=[7071000,0,0,0,6345,0]
sol=odeint(satelite, z0, t)

plt.figure(1)
x= sol[:,0]
y= sol[:,1]
plt.plot(x,y)
num_segmentos = 14401
rad = 6451000
cx = 0
cy = 0

angulo = np.linspace(0, 2*np.pi, num_segmentos+1)
xx = rad * np.cos(angulo) + cx
yy = rad * np.sin(angulo) + cy

plt.plot(xx, yy, color="red", markersize=1)
plt.plot(xx, yy)
plt.gca().set_aspect('equal')
plt.title("Trayectoria satélite")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)
plt.show()

plt.figure(2)
x= sol[:,0]
y= sol[:,1]
plt.plot(t,x)
plt.title("Gráfico x(t)")
plt.show()

plt.figure(3)
x= sol[:,0]
y= sol[:,1]
plt.plot(t,y)
plt.title("Gráfico y(t)")
plt.show()

plt.figure(4)
x= sol[:,0]
y= sol[:,1]
plt.plot(t,sol[:,2])
plt.title("Gráfico z(t)")
plt.show()

plt.figure(5)
x= sol[:,0]
y= sol[:,1]
plt.plot(t,np.sqrt(x**2+y**2+(sol[:,2])**2))
t1=[0, 14401]
t2=[0, 14401]
y1=[6451000, 6451000]
y2=[6371000, 6371000]
plt.plot(t1, y1, color="g")
plt.plot(t2, y2, color="r")
plt.title("Gráfico r(t)")
plt.show()
