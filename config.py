G = 6.67430e-11

DT = 1           # Time step in seconds
TOTAL_TIME = 10000  # Total simulation time in seconds


# Initial conditions 
INITIAL_CONDITIONS = [
    {
        "mass": 5.972e24,  # Earth
        "position": [0.0, 0.0],
        "velocity": [0.0, 0.0],
    },
    {
        "mass": 7.348e22,  # Moon
        "position": [384400000.0, 0.0],  # meters
        "velocity": [0.0, 1022.0],       # m/s
    },
]