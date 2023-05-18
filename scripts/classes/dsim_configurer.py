# dsim_configurer.py
# Last updated: 5/18/2023

class Configuration:
    help_file = open('dsim_help.txt')
    help_text = help_file.read()

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

    def change_config(self, verb, value):
        match verb:
            case "width":
                self.width = value
            case "height":
                self.height = value
            case "length":
                self.length = value

            case "num_drones":
                self.num_drones = value
            case "num_affectors":
                self.num_affectors = value

            case "help":
                print(self.help_text)
            case _:
                print("Unknown command... type help for a list of commands")
