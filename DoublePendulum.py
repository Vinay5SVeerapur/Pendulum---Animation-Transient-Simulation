from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np
from matplotlib.animation import FuncAnimation
dsdt=[]
def f(s,t):
    l1=1
    l2=1
    m1=2
    m2=2
    dsdt[0] = s[1]
    dsdt[1] = (-(9.81*(m1+m2)*np.sin(s[0]))-(m2*l2*np.sin(s[0]-s[2])*s[3]**2)-(m2*l2*dsdt[3]*np.cos(s[0]-s[2])))/((m1+m2)*l1)
    dsdt[2] = s[3]
    dsdt[3] = (-(m2*9.81*np.sin(s[2]))+(m2*l1*np.sin(s[0]-s[2])*s[1]**2)-(m2*l1*dsdt[1]*np.cos(s[0]-s[1])))/(m2*l2)
    return dsdt

theeta0=[0,0,np.pi/3,0]

t = np.linspace(0,30,600)

theeta=odeint(f,theeta0,t)

fig = plt.figure()

point1, = plt.plot([0],[0],"o")
line1, = plt.plot([0,0],[0,0])

point2, = plt.plot([0],[0],"o")
line2, = plt.plot([0,0],[0,0])

#trace, = plt.plot([0,0],[0,0])

plt.axis("scaled")
plt.xlim(-3,3)
plt.ylim(-3,3)

x1=np.sin(theeta[:,0])
y1=-np.cos(theeta[:,0])

x2=x1[len(x1)-1]+np.sin(theeta[:,2])
y2=y2[len(y2)-1]-np.cos(theeta[:,2])

def animate(time):
    time=time-1
    point1.set_data(1*np.sin(theeta[time,0]),-1*np.cos(theeta[time,0]))
    point2.set_data(x2[time],y[time])
    
    line1.set_data([0 , 2*np.sin(theeta[time,0])],[0 ,-2*np.cos(theeta[time,0])])
    line2.set_data([x1[len(x1)-1],y1[len(y1)-1]],[x1[len(x1)-1]+x2[time],y1[len(y1)-1]+y2[time]])
    
    return point1, line1, point2, line2

anim = FuncAnimation(fig,animate,frames=len(t),interval=0.05*1000)
anim.save("Simplependulum_trace.mp4",fps=20)
plt.show()
