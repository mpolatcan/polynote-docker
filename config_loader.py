import yaml
from os import environ

config = yaml.safe_load(open("config_template.yml", "r"))


def fill_config_from_env(config):
    for item in config.keys():
        if isinstance(config[item], dict):
            fill_config_from_env(config[item])
        else:
            config[item] = environ[config[item].replace("$", "").replace("{", "").replace("}", "")]

    return config


yaml.dump(fill_config_from_env(config), open("${polynote_home}/config.yml".format(polynote_home=environ["POLYNOTE_HOME"]), "w"))