import yaml


def read_config_file(path: str) -> dict:
    with open(path, "r") as file:
        return yaml.safe_load(file)
