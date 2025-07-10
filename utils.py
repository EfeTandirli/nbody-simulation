from nbody import Body,rk4_step,update_force
import numpy as np

def simulate(initial_conditions,dt,total_time):
    bodies=[Body(**params) for params in initial_conditions]
    traj =[[] for _ in bodies]

    steps= int(total_time/dt)

    for _ in range(steps):
        rk4_step(bodies,dt)
        for i,b in enumerate(bodies):
            traj[i].append(b.position.copy())
    return np.array[traj]