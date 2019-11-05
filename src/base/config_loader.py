# Written by Mutlu Polatcan
# 04.11.2019

import yaml
from os import environ
from sys import argv


def fill_config_from_env(config):
    for key, val in config.items():
        if isinstance(val, dict):
            fill_config_from_env(val)
        else:
            config[key] = environ[val.replace("$", "").replace("{", "").replace("}", "")]

    return config


if __name__ == "__main__":
    config = yaml.safe_load(open(argv[1], "r"))
    yaml.safe_dump(fill_config_from_env(config), open("{polynote_home}/config.yml".format(polynote_home=environ["POLYNOTE_HOME"]), "w"))
