# dsim_drone.py
# Last updated : 5/17/2023

class Drone:
    """
    Drone Class

    Attributes
    -----
    DRONE_ID : string
        unique identifier
    x,y,z : int
        positional coords -> [0, inf)
    battery : float
        battery as a percentage -> [0.0, 1.0]
    """

    # Constructor
    def __init__(self, drone_id, x, y, z, battery):
        self.DRONE_ID = drone_id
        self.x = x
        self.y = y
        self.z = z
        self.battery = battery

    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_battery(self, battery):
        self.battery = battery
