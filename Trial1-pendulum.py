from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np
from matplotlib.animation import FuncAnimation

def f(s,t):
    return(s[1],-9.81*np.sin(s[0])/2)

theeta0=[0,1]

t = np.linspace(0,30,600)

theeta=odeint(f,theeta0,t)

fig = plt.figure()

point, = plt.plot([0],[0],"o")
line, = plt.plot([0,0],[0,0])
trace, = plt.plot([0,0],[0,0])

plt.axis("scaled")
plt.xlim(-3,3)
plt.ylim(-3,3)
x=2*np.sin(theeta[:,0])
y=-2*np.cos(theeta[:,0])
def animate(time):
    time=time-1
    point.set_data(2*np.sin(theeta[time,0]),-2*np.cos(theeta[time,0]))
    line.set_data([0 , 2*np.sin(theeta[time,0])],[0 ,-2*np.cos(theeta[time,0])])
    trace.set_data(x[0:time],y[0:time])
    return point, line, trace,
anim = FuncAnimation(fig,animate,frames=len(t),interval=0.05*1000)
anim.save("Simplependulum_trace.mp4",fps=20)
plt.show()
