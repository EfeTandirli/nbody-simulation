from config import INITIAL_CONDITIONS,DT,TOTAL_TIME
from utils import simulate
from visualise import animate_traj
import matplotlib.pyplot as plt


trajectories = simulate(INITIAL_CONDITIONS,DT,TOTAL_TIME)
animate_traj(trajectories)

"""

for traj in trajectories:
    plt.plot(traj[:,0],traj[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("N-body Model")
plt.grid()
plt.show()


"""


