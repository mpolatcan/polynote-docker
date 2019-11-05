import yaml
from os import environ

config = yaml.safe_load(open("config_template.yml", "r"))


def fill_config_from_env(config):
    for key, val in config.items():
        if isinstance(val, dict):
            fill_config_from_env(val)
        else:
            config[key] = environ[val.replace("$", "").replace("{", "").replace("}", "")]

    return config


yaml.safe_dump(fill_config_from_env(config), open("{polynote_home}/config.yml".format(polynote_home=environ["POLYNOTE_HOME"]), "w"))
