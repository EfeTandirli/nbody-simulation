from config import G
from nbody import Body,rk4_step,update_force
import numpy as np


def calculate_energy(bodies):
    kinetic=0
    potential=0
    n= len(bodies)

    for i in range(n):
        v=np.linalg.norm(bodies[i].velocity)
        kinetic= 1/2*v**2*bodies[i].mass
        for j in range(n):
            diff= bodies[i].position - bodies[j].position
            r=np.linalg.norm(diff)
            potential -= G* bodies[i].mass* r
    return kinetic+potential  


def center_of_mass(bodies):
    total_mass = sum(b.mass for b in bodies)
    return sum(b.mass * b.position for b in bodies) / total_mass


def simulate(initial_conditions,dt,total_time):
    bodies=[Body(**params) for params in initial_conditions]
    traj =[[] for _ in bodies]
    energies=[]

    steps= int(total_time/dt)

    for _ in range(steps):
        rk4_step(bodies,dt)
        com=center_of_mass(bodies)
        for i,b in enumerate(bodies):
            traj[i].append((b.position-com).copy())
        energies.append(calculate_energy(bodies))
    return np.array(traj), np.array(energies)