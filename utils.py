from nbody import Body,rk4_step,update_force
import numpy as np

def center_of_mass(bodies):
    total_mass = sum(b.mass for b in bodies)
    return sum(b.mass * b.position for b in bodies) / total_mass


def simulate(initial_conditions,dt,total_time):
    bodies=[Body(**params) for params in initial_conditions]
    traj =[[] for _ in bodies]

    steps= int(total_time/dt)

    for _ in range(steps):
        rk4_step(bodies,dt)
        com=center_of_mass(bodies)
        for i,b in enumerate(bodies):
            traj[i].append((b.position-com).copy())
    return np.array(traj)