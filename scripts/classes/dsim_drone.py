# dsim_drone.py
# Last updated : 5/17/2023
# Simple drone container class

class Drone:
    # Constructor
    def __init__(self, x, y, z, battery):
        self.x = x
        self.y = y
        self.z = z
        self.battery = battery

    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
