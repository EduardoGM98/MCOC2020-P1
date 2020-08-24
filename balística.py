import scipy as sp
from scipy.integrate import odeint
import matplotlib.pylab as plt

#unidades bases

cm=0.01 #en metros
inch=2.54*cm

#coef de arraste
p=1.225  #kg/m**3
cd=0.47
D=8.5*inch
r=D/2
A=sp.pi*r**2
CD=0.5*p*cd*A
g=9.81 #m/s**2
m=15 #kg
V=[0, 10, 20]

#función a integrar:
#z es vector de estado
#z=[x,y,vx,vy]
#dz/dt=bala(z,t)
        #[z1     ]
#dz/dt=  [       ]
        #[FD/m -g]

#z[0] ->x
#z[1] ->y
#z[2] ->vx
#z[3] ->vy
for i in V:
    
    def bala(z, t):
        zp=sp.zeros(4)
        zp[0]=z[2]
        zp[1]=z[3]
        v=z[2:4]
        v[0]=v[0]- i
        v2=sp.dot(v,v)
        vnorm=sp.sqrt(sp.dot(v,v))
        FD=-CD*v2*(v/vnorm)
        zp[2]=FD[0]/m
        zp[3]=FD[1]/m-g
        return zp
    
    #vector de tiempo
    t=sp.linspace(0, 5.58, 1001)
    
    # parte en el origen y tiene vx y vy =2 m/s
    vi=100*1000/3600
    z0=sp.array([0,0,vi,vi])

    sol=odeint(bala, z0, t)
    x= sol[:,0]
    y= sol[:,1]
    plt.plot(x,y)
    
plt.figure(1)
plt.title("Trayectoria para distintos vientos")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)
plt.ylim(0.0, 50)
plt.xlim(0.0)
plt.legend(("V=0 m/s", "V=10.0 m/s ", "V=20.0 m/s"), prop={"size":10}, loc="upper right")
plt.savefig("balísitca.png")
plt.close(1)
