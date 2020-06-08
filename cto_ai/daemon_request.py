import requests
import os
import json


def _port():
    port = os.environ.get("SDK_SPEAK_PORT", None)
    if port is None:
        raise RuntimeError(
            "The CTO.ai Ops SDK requires a daemon process to be running; this does not appear to be the case."
        )
    return port


def _make_requester(endpoint):
    return lambda data: requests.post(
        f"http://127.0.0.1:{_port()}/{endpoint}", json=data
    ).raise_for_status()


print = _make_requester("print")
start_spinner = _make_requester("start-spinner")
stop_spinner = _make_requester("stop-spinner")
start_progress = _make_requester("progress-bar/start")
advance_progress = _make_requester("progress-bar/advance")
stop_progress = _make_requester("progress-bar/stop")
track = _make_requester("track")
set_state = _make_requester("state/set")
set_config = _make_requester("config/set")


def _make_sync_requester(endpoint):
    def requester(body):
        response = requests.post(f"http://127.0.0.1:{_port()}/{endpoint}", json=body)

        response.raise_for_status()
        response_data = response.json()

        return response_data["value"]

    return requester


get_state = _make_sync_requester("state/get")
get_all_state = _make_sync_requester("state/get-all")
get_config = _make_sync_requester("config/get")
get_all_config = _make_sync_requester("config/get-all")
delete_config = _make_sync_requester("config/delete")
events = _make_sync_requester("events")


def _make_async_requester(endpoint):
    def requester(body):
        response = requests.post(f"http://127.0.0.1:{_port()}/{endpoint}", json=body)

        response.raise_for_status()
        response_data = response.json()

        with open(response_data["replyFilename"]) as infile:
            return json.load(infile)

    return requester


prompt = _make_async_requester("prompt")
get_secret = _make_async_requester("secret/get")
set_secret = _make_async_requester("secret/set")
