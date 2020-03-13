from . import daemon_request
from typing import Iterable, Optional, Union


def input(
    name: str,
    message: str,
    *,
    default: Optional[str] = None,
    allowEmpty: bool = False,
    flag: Optional[str] = None,
) -> str:
    """Prompt the user for a free-form single-line string"""
    return daemon_request.prompt(dict(type="input", **locals()))[name]


def number(
    name: str,
    message: str,
    *,
    default: Optional[int] = None,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    flag: Optional[str] = None,
):
    """Prompt the user for an integer"""
    return daemon_request.prompt(dict(type="number", **locals()))[name]


def secret(name: str, message: str, *, flag: Optional[str] = None) -> str:
    """Prompt the user for a secret"""
    return daemon_request.prompt(dict(type="secret", **locals()))[name]


def password(
    name: str, message: str, *, confirm: bool = False, flag: Optional[str] = None
) -> str:
    """Prompt the user for a password"""
    return daemon_request.prompt(dict(type="password", **locals()))[name]


def confirm(
    name: str, message: str, *, default: bool = False, flag: Optional[str] = None
):
    """Prompt the user for a yes/no answer"""
    return daemon_request.prompt(dict(type="confirm", **locals()))[name]


def list(
    name: str,
    message: str,
    *,
    choices: Iterable[str],
    default: Optional[Union[str, int]] = None,
    flag: Optional[str] = None,
):
    """Prompt the user for a selection from a list of options"""
    return daemon_request.prompt(dict(type="list", **locals()))[name]


def autocomplete(
    name: str,
    message: str,
    *,
    choices: Iterable[str],
    default: Optional[Union[str, int]] = None,
    flag: Optional[str] = None,
):
    """Prompt the user for a selection from a list of options, with autocomplete on the values"""
    return daemon_request.prompt(dict(type="autocomplete", **locals()))[name]


def checkbox(
    name: str,
    message: str,
    *,
    choices: Iterable[str],
    default: Optional[Iterable[Union[str, int]]] = None,
    flag: Optional[str] = None,
):
    """Prompt the user for a selection of any number members of a list of strings"""
    return daemon_request.prompt(dict(type="checkbox", **locals()))[name]


def editor(name: str, message: str, default: Optional[str] = None):
    """Prompt the user for a multiline freeform string"""
    return daemon_request.prompt(dict(type="editor", **locals()))[name]


VARIANT_DATETIME = "datetime"
VARIANT_DATE = "date"
VARIANT_TIME = "time"


def datetime(
    name: str,
    message: str,
    *,
    variant: str = VARIANT_DATETIME,
    default=None,
    minimum=None,
    maximum=None,
    flag: Optional[str] = None,
):
    """Prompt the user for a date and/or time"""
    return daemon_request.prompt(dict(type="datetime", **locals()))[name]
