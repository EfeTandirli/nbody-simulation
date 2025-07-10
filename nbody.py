import numpy as np
from config import G

class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
    def euler_step(self, dt):
        acc = self.force / self.mass
        self.velocity += acc * dt
        self.position += self.velocity * dt

def update_force(bodies):
        acc=[]
        for i,body in enumerate(bodies):
            net_force=np.zeros()
            for j,other in enumerate(bodies):
                if i==j:
                    continue
                diff=other.position-body.position
                distance=np.linalg.norm(diff)+1e-10
                g_force=G*body.mass*other.mass/(distance**2)
                net_force+=g_force*diff/distance
            acc=net_force/body.mass
            acc.append(acc)
        return acc
        
def rk4_step(bodies,dt):
    x0=[b.position.copy() for b in bodies]
    v0=[b.velocity.copy() for b in bodies]

    a1=update_force(bodies)
    t1_x=[v.copy() for v in v0]
    t1_v=a1

    temp_bodies=[Body(b.mass,
                      x0[i]+ 0.5*dt*t1_x[i],
                      v0[i]+ 0.5*dt*t1_v[i])for i,b in enumerate(bodies)]
    
    a2=update_force(temp_bodies)
    t2_x=[b.velocity for b in temp_bodies]
    t2_v=a2

    temp_bodies=[Body(b.mass,
                      x0[i]+ 0.5*dt*t2_x[i],
                      v0[i]+ 0.5*dt*t2_v[i])for i,b in enumerate(bodies)]

    a3=update_force(temp_bodies)
    t3_x=[b.velocity for b in temp_bodies]
    t3_v=a3

    temp_bodies=[Body(b.mass,
                      x0[i]+ dt*t3_x[i],
                      v0[i]+ dt*t3_v[i])for i,b in enumerate(bodies)]
    
    a4=update_force(temp_bodies)
    t4_x=[b.velocity for b in temp_bodies]
    t4_v=a4

    for i,b in enumerate(bodies):
        b.position= x0[i] + (dt/6)*(t1_x[i]+2*t2_x[i]+2*t3_x[i]+t4_x[i])
        b.velocity= v0[i] + (dt/6)*(t1_v[i]+2*t2_v[i]+2*t3_v[i]+t4_v[i])