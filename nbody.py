import numpy as np
from config import G

class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
    def euler_step(self,acc, dt):
        self.velocity += acc * dt
        self.position += self.velocity * dt

def update_force(bodies):
        accs=[]
        for i,body in enumerate(bodies):
            net_force=np.zeros(2)
            for j,other in enumerate(bodies):
                if i==j:
                    continue
                diff=other.position-body.position
                distance=np.linalg.norm(diff)+1e-10
                g_force=G*body.mass*other.mass/(distance**2)
                net_force+=g_force*diff/distance
            acc=net_force/body.mass
            accs.append(acc)
        return accs
        
def rk4_step(bodies, dt):
    x0 = [b.position.copy() for b in bodies]
    v0 = [b.velocity.copy() for b in bodies]

    a1 = update_force(bodies)
    t1_x = v0
    t1_v = a1

    x1 = [x0[i] + 0.5 * dt * t1_x[i] for i in range(len(bodies))]
    v1 = [v0[i] + 0.5 * dt * t1_v[i] for i in range(len(bodies))]
    temp_bodies = [Body(b.mass, x1[i], v1[i]) for i, b in enumerate(bodies)]
    a2 = update_force(temp_bodies)
    t2_x = v1
    t2_v = a2

    x2 = [x0[i] + 0.5 * dt * t2_x[i] for i in range(len(bodies))]
    v2 = [v0[i] + 0.5 * dt * t2_v[i] for i in range(len(bodies))]
    temp_bodies = [Body(b.mass, x2[i], v2[i]) for i, b in enumerate(bodies)]
    a3 = update_force(temp_bodies)
    t3_x = v2
    t3_v = a3

    x3 = [x0[i] + dt * t3_x[i] for i in range(len(bodies))]
    v3 = [v0[i] + dt * t3_v[i] for i in range(len(bodies))]
    temp_bodies = [Body(b.mass, x3[i], v3[i]) for i, b in enumerate(bodies)]
    a4 = update_force(temp_bodies)
    t4_x = v3
    t4_v = a4

    for i, b in enumerate(bodies):
        b.position = x0[i] + (dt / 6) * (t1_x[i] + 2 * t2_x[i] + 2 * t3_x[i] + t4_x[i])
        b.velocity = v0[i] + (dt / 6) * (t1_v[i] + 2 * t2_v[i] + 2 * t3_v[i] + t4_v[i])
