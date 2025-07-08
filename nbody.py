import numpy as np
from config import G

class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.force = np.zeros(2)

    def update_force(self, bodies):
        self.force = np.zeros(2)
        for other in bodies:
            if other is self:
                continue
            diff = other.position - self.position
            distance = np.linalg.norm(diff) + 1e-10  
            force_mag = G * self.mass * other.mass / (distance**2)
            self.force += force_mag * diff / distance

    def euler_step(self, dt):
        acc = self.force / self.mass
        self.velocity += acc * dt
        self.position += self.velocity * dt