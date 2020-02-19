from . import daemon_request
from typing import Optional


def print(text: str):
    """Print a string to the user"""
    daemon_request.print({"text": text})


def spinner_start(text: str):
    """Start a spinner with the given label"""
    daemon_request.start_spinner({"text": text})


def spinner_stop(text: Optional[str] = None):
    """Stop the running spinner, if one is running"""
    daemon_request.stop_spinner({} if text is None else {"text": text})


def progress_bar_start(length: int, initial: int = 0, message: Optional[str] = None):
    """Start a progress bar with the given length"""
    daemon_request.start_progress(
        {"length": length, "initial": initial, "text": message}
    )


def progress_bar_advance(increment: int = 1):
    """Advance the running progress bar by increment"""
    daemon_request.advance_progress({"increment": increment})


def progress_bar_stop(message: Optional[str] = None):
    """Stop the current progress bar"""
    daemon_request.stop_progress({} if message is None else {"text": message})
