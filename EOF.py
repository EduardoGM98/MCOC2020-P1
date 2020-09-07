from matplotlib.pylab import *
from scipy.integrate import odeint
from leer_eof import leer_eof
from time import perf_counter

G=6.674*10**-11 #(N*m^2)/kg^2
G1=6.674*10**-17 #(N*km^2)/kg^2
Mt=5.972*10**24 #kg
r=7071000 #m
O=7.27*10**-5 #rad/s
J2=1.75553*(10**10) #km5⋅s−2
J3=-2.61913*(10**11) #km6⋅s−2

t5=perf_counter()
def zp(z,t):
    c=cos(O*t)
    s=sin(O*t)
    R=array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    Rp=O*array([[-s, -c, 0], [c, -s, 0], [0, 0, 0]])
    Rpp=(O**2)*array([[-c, s, 0], [-s, -c, 0], [0, 0, 0]])
    zp=zeros(6)
    z1=z[0:3]
    z2=z[3:6] 
    r2=dot(z1,z1)
    r=sqrt(r2) 
    Fg=(-G*Mt/r**2)*(R@(z1/r))
    zp[0:3]=z2
    zp[3:6]=R.T@(Fg-(2*Rp@z2)+(Rpp@z1))
    return zp

def zpJ2J3(z,t):
    c=cos(O*t)
    s=sin(O*t)
    R=array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    Rp=O*array([[-s, -c, 0], [c, -s, 0], [0, 0, 0]])
    Rpp=(O**2)*array([[-c, s, 0], [-s, -c, 0], [0, 0, 0]])
    zp=zeros(6)
    z1=z[0:3]
    z2=z[3:6] 
    r2=dot(z1,z1)
    r=sqrt(r2) 
    Fg=(-G1*Mt/r**2)*(R@(z1/r))
    fj2=[J2*(z[0]/(r**7))*(6*(z[2]**2)-(3/2)*((z[0]**2)+(z[1]**2))), J2*(z[1]/(r**7))*(6*(z[2]**2)-(3/2)*((z[0]**2)+(z[1]**2))), J2*(z[2]/(r**7))*(3*(z[2]**2)-(9/2)*((z[0]**2)+(z[1]**2)))]
    fj3=[J3*((z[0]*z[2])/(r**9))*(10*(z[2]**2)-(15/2)*((z[0]**2)+(z[1]**2))), J3*((z[1]*z[2])/(r**9))*(10*(z[2]**2)-(15/2)*((z[0]**2)+(z[1]**2))), J3*(1/(r**9))*(4*(z[2]**2)-3*((z[0]**2)+(z[1]**2))+(3/2)*((z[0]**2)+(z[1]**2))**2)]
    zp[0:3]=z2
    zp[3:6]=R.T@(Fg-(2*Rp@z2)+(Rpp@z1))+fj2+fj3
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

sat_t, sat_x, sat_y, sat_z, sat_vx, sat_vy, sat_vz=leer_eof("S1B_OPER_AUX_POEORB_OPOD_20200822T111200_V20200801T225942_20200803T005942.EOF")

z0=[sat_x[0], sat_y[0], sat_z[0], sat_vx[0], sat_vy[0], sat_vz[0]]


t1=perf_counter()
sol_odeint= odeint(zp, z0, sat_t)
t2=perf_counter()
t_odeint=(t2-t1)
print(f"tiempo de solución odeint={t_odeint} s.")

t3=perf_counter()
sol_euler1= eulerint(zp, z0, sat_t, Nsubdivisiones=1)
t4=perf_counter()
t_eulerint=(t4-t3)
print(f"tiempo de solución eulerint={t_eulerint} s.")

x=sol_odeint[:,0]
y=sol_odeint[:,1]
z=sol_odeint[:,2]

x1=sol_euler1[:,0]
y1=sol_euler1[:,1]
z1=sol_euler1[:,2]

delta=sqrt((x-x1)**2 + (y-y1)**2 + (z-z1)**2)
der=delta[-1]/1000
print(f"deriva eulerint de odeint={der} km")

plot(t/3600, delta/1000, label="odeint/eulerint")
legend()
xlabel("Tiempo, t (horas)")
ylabel("Deriva (km)")
title(f"Distancia posición odeint y eulerint, {der} (Km)")
show()


sol_odeint= odeint(zpJ2J3, z0, sat_t)
sol_euler1= eulerint(zpJ2J3, z0, sat_t, Nsubdivisiones=1)


x2=sol_odeint[:,0]
y2=sol_odeint[:,1]
z2=sol_odeint[:,2]

x3=sol_euler1[:,0]
y3=sol_euler1[:,1]
z3=sol_euler1[:,2]

delta1=sqrt((x2-x3)**2 + (y2-y3)**2 + (z2-z3)**2)
der1=delta1[-1]/1000
print(f"deriva eulerintJ2J3 de odeintJ2J3={der1} km")

plot(t/3600, delta1/1000, label="odeint/eulerint")
legend()
xlabel("Tiempo, t (horas)")
ylabel("Deriva (km)")
title(f"Distancia posición odeint y eulerint, J2 y J3, {der1} (Km)")
show()


#graficos posición
figure()
subplot(3,1,1)
plot(sat_t/3600,sat_x/1000, color="b")
plot(sat_t/3600,x/1000,color="y")
plot(sat_t/3600,x1/1000,color="r")
ylabel("X (km)")
title("Posición")

subplot(3,1,2)
plot(sat_t/3600,sat_y/1000,color="b")
plot(sat_t/3600,y/1000,color="y")
plot(sat_t/3600,y1/1000,color="r")
ylabel("Y (km)")

subplot(3,1,3)
plot(sat_t/3600,sat_z/1000,color="b")
plot(sat_t/3600,z/1000,color="y")
plot(sat_t/3600,z1/1000,color="r")
xlabel("Tiempo, t (horas)")
ylabel("Z (km)")
show()

#implementando J2 y J3
figure()
subplot(3,1,1)
plot(sat_t/3600,sat_x/1000, color="b")
plot(sat_t/3600,x2/1000,color="y")
plot(sat_t/3600,x3/1000,color="r")
ylabel("X (km)")
title("Posición implementando J2 y J3")

subplot(3,1,2)
plot(sat_t/3600,sat_y/1000,color="b")
plot(sat_t/3600,y2/1000,color="y")
plot(sat_t/3600,y3/1000,color="r")
ylabel("Y (km)")

subplot(3,1,3)
plot(sat_t/3600,sat_z/1000,color="b")
plot(sat_t/3600,z2/1000,color="y")
plot(sat_t/3600,z3/1000,color="r")
xlabel("Tiempo, t (horas)")
ylabel("Z (km)")
show()
  
t6=perf_counter()
tiempo_total=t6-t5
print(tiempo_total)