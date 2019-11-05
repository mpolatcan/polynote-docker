# Written by Mutlu Polatcan
# 21.10.2019

import yaml
import sys


class Constants:
    KEY_CONFIG_FILES = "config_files"
    KEY_BASE_DOCKERFILE_TEMPLATE = "base_dockerfile_template"
    KEY_CONFIG_LOADER_SH_TEMPLATE = "config_loader_sh_template"
    KEY_OUTPUT_DIR = "output_dir"
    KEY_PATH = "path"
    KEY_FILENAME = "filename"
    DOCKER_ENV_VAR_FMT = "\t{env_var_name}=\"{env_var_value}\" \\"


class BaseSetupGenerator:
    def __init__(self, config_filename):
        self.__config = yaml.safe_load(open(config_filename, "r"))

    def __get_infos(self, data, prefix=None):
        docker_env_vars = []

        for property, value in data.items():
            property_name = prefix + "." + property if prefix else property

            if isinstance(value, dict):
                _docker_env_vars, _data = self.__get_infos(value, property_name)
                docker_env_vars.extend(_docker_env_vars)
            else:
                property_name = property_name[:-1] if property_name[-1] == "." else property_name

                env_var_name = property_name.upper().replace(".", "_").replace("-", "_")

                docker_env_vars.append(Constants.DOCKER_ENV_VAR_FMT.format(env_var_name=env_var_name, env_var_value=value))
                
                data[property] = "${{{env_var_name}}}".format(env_var_name=env_var_name)

        return docker_env_vars, data

    def generate(self):
        docker_env_vars = []

        for config_info in self.__config[Constants.KEY_CONFIG_FILES]:
            config_file_path = config_info[Constants.KEY_PATH]
            config_filename = config_info[Constants.KEY_FILENAME]

            _docker_env_vars, config_template_yml = self.__get_infos(yaml.safe_load(open(config_file_path, "r")))
            docker_env_vars.extend(_docker_env_vars)

            yaml.safe_dump(config_template_yml, open("{loc}/{filename}".format(
                loc=self.__config[Constants.KEY_OUTPUT_DIR], filename=config_filename), "w"))

        docker_env_vars.append(docker_env_vars.pop(len(docker_env_vars)-1).replace(" \\", ""))

        open("{loc}/Dockerfile".format(loc=self.__config[Constants.KEY_OUTPUT_DIR]), "w").write(self.__config[Constants.KEY_BASE_DOCKERFILE_TEMPLATE].format(
            env_vars="\n".join(docker_env_vars)
        ))


if __name__ == "__main__":
    BaseSetupGenerator(sys.argv[1]).generate()
