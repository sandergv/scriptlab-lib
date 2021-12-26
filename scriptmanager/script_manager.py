import json
import sys
import os

from scriptmanager.context import Context, HttpContext

WORKSPACE = os.getenv("SCRIPT_WORKSPACE")
RUN_TYPE = os.getenv("RUN_TYPE")
READ_PIPE = int(os.getenv("READ_PIPE", "0"))
TRIGGER_CONTEXT = os.getenv("TRIGGER_CONTEXT", "{}")


def get_http_context() -> HttpContext:
    json_context = json.loads(TRIGGER_CONTEXT)

    # try:
    #     r = os.fdopen(READ_PIPE)
    #     json_context = json.load(r)
    # except Exception as e:
    #     print(e)

    # file_path = f"{WORKSPACE}/context.json"
    # with open(file_path, 'r', encoding='utf8') as f:
    #     json_context = json.load(f)

    context = HttpContext()
    context.script_id = json_context["script_id"]
    context.script_name = json_context["script_name"]
    context.run_type = json_context["run_type"]
    context.trigger_type = json_context["trigger_type"]
    context.trigger_id = json_context["trigger_id"]
    context.api_name = json_context["api_name"]
    context.namespace = json_context["namespace"]
    context.group = json_context["group"]
    context.method = json_context["method"]
    context.query_string = json_context["query_string"]
    context.body = json_context["body"]

    return context


class ScriptManager:

    base_url = "http://localhost:8910/__internal"

    def __init__(self) -> None:

        self.context = get_http_context()

    def http_response(self, response: dict) -> None:
        if type(response) != dict:
            raise TypeError("Response must be a dictionary")

        sys.stderr.write("__response__=" + json.dumps(response) + "||")

    def action(self, act: str, data: dict = None, with_response: bool = False,
               with_callback: bool = False, callback=None, after=None, unit="minute") -> dict:
        """
        The action function send a signal to the system to execute an action trigger
        with the given configuration.

        :param act: unique action name
        :param data: Dict with the request data if is necessary
        :param with_response: wait for the action response
        :param with_callback: execute a callback function when the
        :param callback:
        :param after:
        :param unit:
        :return:
        """
