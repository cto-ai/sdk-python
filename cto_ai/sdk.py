import os, json, os.path, typing
from os.path import abspath
from . import daemon_request
from requests.exceptions import RequestException


def get_host_os() -> str:
    """Gets the OS of the current host"""
    return os.environ.get("OPS_HOST_PLATFORM", "unknown")


def get_interface_type() -> str:
    """Gets the interface type that the op is currently running through"""
    return os.environ.get("SDK_INTERFACE_TYPE", "terminal")


def home_dir() -> str:
    """Return the location of the user home directory"""
    return os.environ.get("SDK_HOME_DIR", "root")


log = print


def get_state_path() -> str:
    return abspath(os.environ.get("SDK_STATE_DIR", ""))


def get_config_path() -> str:
    return abspath(os.environ.get("SDK_CONFIG_DIR", ""))


class JsonStore:
    def __init__(self, filename: str):
        self.filename = filename

    def get_all(self):
        try:
            with open(self.filename) as infile:
                return json.load(infile)
        except (json.JSONDecodeError, OSError):
            return {}

    def get(self, key: str):
        return self.get_all().get(key)

    def set(self, key: str, value: str):
        state = self.get_all()
        state[key] = value

        with open(self.filename, "w") as outfile:
            json.dump(state, outfile)
        return state


state = JsonStore(os.path.join(get_state_path(), "state.json"))
config = JsonStore(os.path.join(get_config_path(), "config.json"))


def track(
    tags: typing.Iterable[str], event: str, metadata: typing.Mapping[str, typing.Any]
):
    """Track an analytics event with the analytics backend"""
    try:
        daemon_request.track(dict(tags=tags, event=event, **metadata))

    # It remains unclear what to do with these errors
    except RequestException:
        pass


def get_secret(key: str) -> str:
    """Get a secret from the secret store by key"""
    daemon_request.get_secret({"key": key})[key]


def set_secret(key: str, value: str) -> str:
    """Set a secret in the secret store by key"""
    daemon_request.set_secret({"key": key, "value": value})["key"]
