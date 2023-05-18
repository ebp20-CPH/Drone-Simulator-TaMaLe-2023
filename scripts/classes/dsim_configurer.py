# dsim_configurer.py
# Last updated: 5/17/2023

class Configuration:
    def __init__(self, width, length, height, num_drones, num_affectors):
        self.width = width
        self.length = length
        self.height = height

        self.num_drones = num_drones
        self.num_affectors = num_affectors

    def __str__(self):
        stringified = ""

        stringified += "width: " + str(self.width) + "\n"
        stringified += "length: " + str(self.length) + "\n"
        stringified += "height: " + str(self.height) + "\n"

        stringified += "num_drones: " + str(self.num_drones) + "\n"
        stringified += "num_affectors: " + str(self.num_affectors) + "\n"

        return stringified

    def change_config(self, verb, param0, param1):
        match verb:
            case "width":
                print("setting width to ...")
            case _:
                print("Unknown command... type help for a list of commands")