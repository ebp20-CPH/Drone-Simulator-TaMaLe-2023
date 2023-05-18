from scripts.classes.dsim_configurer import Configuration


# Loops input updating settings object for tool
def init_input_loop():
    config = Configuration(0, 0, 0, 0, 0)

    text = ""
    while text != "run":
        text = input()
        params = text.split(' ')

        if len(params) == 2:
            config.change_config(params[0], params[1])
        elif len(params) == 1:
            config.change_config(params[0], 0)
        else:
            print()

    return config
