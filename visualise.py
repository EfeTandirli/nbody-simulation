import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_traj(traj, energy=None, interval=20, save_path=None):
    fig, (ax_orbit, ax_energy) = plt.subplots(1, 2, figsize=(12, 5)) if energy is not None else (plt.subplots(), None)

    n_bodies = len(traj)
    lines = [ax_orbit.plot([], [], 'o')[0] for _ in range(n_bodies)]

    all_x = traj[:, :, 0].flatten()
    all_y = traj[:, :, 1].flatten()
    margin = 0.1 * max(all_x.max() - all_x.min(), all_y.max() - all_y.min())
    ax_orbit.set_xlim(all_x.min() - margin, all_x.max() + margin)
    ax_orbit.set_ylim(all_y.min() - margin, all_y.max() + margin)
    ax_orbit.set_aspect('equal')
    ax_orbit.set_title("N-body Simulation")
    ax_orbit.set_xlabel("x")
    ax_orbit.set_ylabel("y")

    if energy is not None:
        energy_line, = ax_energy.plot([], [], 'r-')
        ax_energy.set_xlim(0, traj.shape[1])
        ax_energy.set_ylim(energy.min() * 0.99, energy.max() * 1.01)
        ax_energy.set_title("Total Energy Over Time")
        ax_energy.set_xlabel("Time Step")
        ax_energy.set_ylabel("Energy (Joules)")

    def update(frame):
        for i in range(n_bodies):
            lines[i].set_data(traj[i, frame, 0], traj[i, frame, 1])

        if energy is not None:
            energy_line.set_data(range(frame + 1), energy[:frame + 1])

        return lines + ([energy_line] if energy is not None else [])

    anim = FuncAnimation(fig, update, frames=traj.shape[1], interval=interval, blit=True)

    if save_path:
        anim.save(save_path, writer='pillow')
    else:
        plt.tight_layout()
        plt.show()
