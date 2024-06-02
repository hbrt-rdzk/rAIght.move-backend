import yaml


def read_config_file(path: str) -> dict:
    with open(path, "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
