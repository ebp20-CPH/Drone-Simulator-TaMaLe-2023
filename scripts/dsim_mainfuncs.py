from scripts.classes.dsim_configurer import Configuration

# Loops input updating settings object for tool
def init_input_loop():
    config = Configuration()

    text = ""
    while text != "run":
        text = input()
        print("Your input is: " + text)

    return config


def py():
    return None