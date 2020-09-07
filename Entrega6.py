from matplotlib.pylab import *
from scipy.integrate import odeint
from leer_eof import leer_eof
from sys import argv



eofname=argv[1]
t, x, y, z, vx, vy, vz=leer_eof(eofname)

eof_out=eofname.replace(".EOF", ".PRED")

G=6.674*10**-11 #(N*m^2)/kg^2
Mt=5.972*10**24 #kg
O=7.27*10**-5 #rad/s
J2=1.75553*(10**10) #km5⋅s−2
J3=-2.61913*(10**11) #km6⋅s−2

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

z0=[x[0], y[0], z[0], vx[0], vy[0], vz[0]]

sol_odeint= odeint(zp, z0, t)
x=sol_odeint[:,0]
y=sol_odeint[:,1]
z=sol_odeint[:,2]
vx=sol_odeint[:,3]
vy=sol_odeint[:,4]
vz=sol_odeint[:,5]


i=0
archivo=open(eofname, "r")
with open(eof_out, "w") as fout:
    for linea in archivo:
        if linea[0:8] == "      <X":
            linea = f"      <X unit=\"m\">{x[i]}</X>\n"
            
        if linea[0:8] == "      <Y":
            linea = f"      <Y unit=\"m\">{y[i]}</Y>\n"
            
        if linea[0:8] == "      <Z":
            linea = f"      <Z unit=\"m\">{z[i]}</Z>\n"
            
        if linea[0:9] == "      <VX":
            linea = f"      <VX unit=\"m/s\">{vx[i]}</VX>\n"
            
        if linea[0:9] == "      <VY":
            linea = f"      <VY unit=\"m/s\">{vy[i]}</VY>\n"
            
        if linea[0:9] == "      <VZ":
            linea = f"      <VZ unit=\"m/s\">{z[i]}</VZ>\n"
            i+=1
            if i==121725:
                break
        fout.write(linea)
        

        
