import os

import yaml
from pkg_resources import resource_filename


def __escape_type(type_name: str):
    return type_name.replace("-", "_")


def __get_nodes_from_file(schema):
    return list(map(lambda t: __escape_type(t["name"]), schema["types"]))


def __get_schema_files():
    files = []
    location = __get_schema_location()
    for file in os.listdir(location):  # type: str
        if file.endswith("yaml"):
            files.append((location, file))
    return files


def __get_config():
    env = os.environ["env"] if "env" in os.environ else ""
    config_filename = "config.yaml" if env is "" else "config-{}.yaml".format(env)
    config_file_path = resource_filename(__package__, "config/" + config_filename)
    config_file = open(config_file_path, "r")
    config = yaml.load(config_file, Loader=yaml.Loader)
    config_file.close()
    return config


def __get_schema_location():
    return '../schema'


def get_schemas():
    schemas = []
    schema_files = __get_schema_files()
    for filename in schema_files:
        file = open(filename[0]+"/"+filename[1])
        schema = yaml.load(file, Loader=yaml.Loader)
        schemas.extend([(__escape_type(schema["name"]), filename[1], __get_nodes_from_file(schema))])
    return schemas
