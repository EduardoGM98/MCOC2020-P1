from datetime import datetime
import scipy as sp
from scipy.integrate import odeint
import numpy as np
import math


G=6.674*10**-11 #(N*m^2)/kg^2
Mt=5.972*10**24 #kg
r=7071000 #m
O=7.27*10**-5 #rad/s


def satelite(z,t):
    c=math.cos(O*t)
    s=math.sin(O*t)
    R=sp.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    Rp=O*sp.array([[-s, -c, 0], [c, -s, 0], [0, 0, 0]])
    Rpp=(O**2)*sp.array([[-c, s, 0], [-s, -c, 0], [0, 0, 0]])
    zp=sp.zeros(6)
    z1=z[0:3]
    z2=z[3:6]
    r2=np.dot(z1,z2)
    r=np.sqrt(r2)
    Fg=(-G*Mt/r**2)*(R@(z1/r))
    zp[0:3]=z2
    zp[3:6]=R.T@(Fg-(2*Rp@z2)+(Rpp@z1))
    return zp


ti="2020-08-01T22:59:42.000000"
ti=ti.split("T")
ti="{} {}".format(ti[0], ti[1])
ti=datetime.strptime(ti, "%Y-%m-%d %H:%M:%S.%f")

tf="2020-08-03T00:59:42.000000"
tf=tf.split("T")
tf="{} {}".format(tf[0], tf[1])
tf=datetime.strptime(tf, "%Y-%m-%d %H:%M:%S.%f")

deltaT=(tf - ti).seconds

x_i=-1369245.647547
y_i=1304968.215334
z_i=6807978.973946
vx_i=-1584.899371
vy_i=7218.741096
vz_i=-1698.932834

x_f=-2050981.739876
y_f=-5754406.922127
z_f=3562317.410720
vx_f=-328.456294
vy_f=4087.891408
vz_f=6393.359266

t=sp.linspace(0, deltaT, 9361)
z0=sp.array([x_i, y_i, z_i, vx_i, vy_i, vz_i])

sol=odeint(satelite, z0, t)

pos_final=sp.array([x_f, y_f, z_f, vx_f, vy_f, vz_f]) - sol[-1]

print(np.linalg.norm(pos_final[0:3]))





