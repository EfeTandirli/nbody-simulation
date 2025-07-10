from config import INITIAL_CONDITIONS,DT,TOTAL_TIME
import matplotlib.pyplot as plt
from utils import simulate

trajectories = simulate(INITIAL_CONDITIONS,DT,TOTAL_TIME)

for traj in trajectories:
    plt.plot(traj[:,0],traj[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("N-body Model")
plt.grid()
plt.show()

