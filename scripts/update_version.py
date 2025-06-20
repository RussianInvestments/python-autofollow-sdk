import tomlkit
import yaml
import re


def get_version(file: str) -> str:
    with open(file, "r") as f:
        data = yaml.safe_load(f)
        return data["info"]["version"]


def set_toml_version(file: str, new_value: str) -> None:
    with open(file, "r") as f:
        data = tomlkit.loads(f.read())
        data["project"]["version"] = new_value
    with open(file, "w") as f:
        tomlkit.dump(data, f)


def update_version() -> None:
    version = get_version("openapi/autofollow.yml")
    set_toml_version("pyproject.toml", version)


if __name__ == '__main__':
    update_version()
