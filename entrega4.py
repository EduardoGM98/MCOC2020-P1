from matplotlib.pylab import *
from scipy.integrate import odeint

m=1
f=1
e=0.2
w=2*pi*f
k=m*(w**2)
c=2*e*w*m
A=1.0625/cos(pi)
phi=pi-0.34479

def zp(z,t):
    zp=zeros(2)
    zp[0]=z[1]
    zp[1]=(-c*z[1]/m)+(-k*z[0]/m)
    return zp

def eulerint(zp, z0, t, Nsubdivisiones=1):
    Nt=len(t)
    Ndim= len(z0)
    
    z=zeros((Nt, Ndim))
    z[0,:]=z0
    
    for i in range(1, Nt):
        t_anterior=t[i-1]
        dt = (t[i]-t[i-1])/Nsubdivisiones
        z_temp=z[i-1,:].copy()
        for k in range(Nsubdivisiones):
            z_temp += dt * zp(z_temp, t_anterior + k*dt)
        
        z[i,:] = z_temp
    return z

t=linspace(0 ,4 , 100)
z0=[1, 1]

z_odeint= odeint(zp, z0, t)
z_odeint= z_odeint[:,0]

z_analitica=A*exp((-c*t)/(2*m))*cos(w*t+phi)

z_euler1= eulerint(zp, z0, t, Nsubdivisiones=1)
z_euler1= z_euler1[:,0]

z_euler2= eulerint(zp, z0, t, Nsubdivisiones=10)
z_euler2= z_euler2[:,0]

z_euler3= eulerint(zp, z0, t, Nsubdivisiones=100)
z_euler3= z_euler3[:,0]


plot(t, z_odeint, label="odeint", color="blue")
plot(t, z_euler1, "--", label="eulerint1", color="green" )
plot(t, z_euler2, "--", label="eulerint10", color="red")
plot(t, z_euler3, "--", label="eulerint100", color="orange")
plot(t, z_analitica, label="analítica", color="black", linewidth=2)
legend(loc="upper right")
show()    

