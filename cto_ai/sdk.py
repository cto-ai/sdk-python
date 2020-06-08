import os, json, os.path, typing
from os.path import abspath
from requests.exceptions import RequestException
from datetime import datetime
from typing import Optional, List

from . import daemon_request


def get_host_os() -> str:
    """Gets the OS of the current host"""
    return os.environ.get("OPS_HOST_PLATFORM", "unknown")


def get_interface_type() -> str:
    """Gets the interface type that the op is currently running through"""
    return os.environ.get("SDK_INTERFACE_TYPE", "terminal")


def home_dir() -> str:
    """Return the location of the user home directory"""
    return os.environ.get("SDK_HOME_DIR", "/root")


log = print

# DEPRECATED: please use `sdk.home_dir()` instead
def get_state_path() -> str:
    return abspath(os.environ.get("SDK_STATE_DIR", ""))


# DEPRECATED: incompatible with current config API
def get_config_path() -> str:
    return abspath(os.environ.get("SDK_CONFIG_DIR", ""))


class JsonStore:
    def __init__(self, getter, getter_all, setter, deleter=None):
        self.getter = getter
        self.getter_all = getter_all
        self.setter = setter
        self.deleter = deleter

    def get_all(self):
        return self.getter_all({})

    def get(self, key: str):
        return self.getter({"key": key})

    def set(self, key: str, value: str):
        self.setter({"key": key, "value": value})
        return self.getter_all({})

    def delete(self, key: str):
        if self.deleter is None:
            raise RuntimeError("Delete method not implemented.")
        return self.deleter({"key": key})


# DEPRECATED: state is used by deprecated workflows feature
state = JsonStore(
    daemon_request.get_state, daemon_request.get_all_state, daemon_request.set_state
)

config = JsonStore(
    daemon_request.get_config,
    daemon_request.get_all_config,
    daemon_request.set_config,
    daemon_request.delete_config,
)


def track(
    tags: typing.Iterable[str], event: str, metadata: typing.Mapping[str, typing.Any]
):
    """Track an analytics event with the analytics backend"""
    try:
        daemon_request.track(dict(tags=tags, event=event, **metadata))

    # It remains unclear what to do with these errors
    except RequestException:
        pass


def events(start: str, end: Optional[str] = None) -> List[dict]:
    if end is None:
        end = datetime.now().isoformat()
    return daemon_request.events({"start": start, "end": end})


def get_secret(key: str) -> str:
    """Get a secret from the secret store by key"""
    return daemon_request.get_secret({"key": key})[key]


def set_secret(key: str, value: str) -> str:
    """Set a secret in the secret store by key"""
    return daemon_request.set_secret({"key": key, "value": value})["key"]
