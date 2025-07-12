import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_traj(traj,interval=20,save_path=None):
    fig,ax =plt.subplots()
    n_bodies= len(traj)
    lines = [ax.plot([],[],"o")[0] for _ in range(n_bodies)]


    all_x = traj[:,:,0].flatten()
    all_y = traj[:,:,1].flatten()
    margin= 0.1* max(all_x.max()-all_x.min(),all_y.max()-all_y.min())

    ax.set_ylim(all_x.min()-margin,all_x.max()+margin)
    ax.set_xlim(all_y.min()-margin,all_y.max()+margin)

    ax.set_aspect("equal")
    ax.set_title("N-body sim")
    ax.set_ylabel("y")
    ax.set_xlabel("x")

    def update(frame):
        for i in range(n_bodies):
            lines[i].set_data(traj[i,frame,0],traj[i,frame,1])
        return lines
    anim= FuncAnimation(fig,update,frames=traj.shape[1], interval=interval, blit=True)
    if save_path:
        anim.save(save_path,writer="pillow")
    else:
        plt.show()
