import json
import sys
import os
import grpc

from .context import Context, HttpContext
from .event_pb2_grpc import EventHandlerStub
from .event_pb2 import ExecActionRequest


WORKSPACE = os.getenv("SCRIPT_WORKSPACE")
RUN_TYPE = os.getenv("RUN_TYPE")
READ_PIPE = int(os.getenv("READ_PIPE", "0"))
CONTEXT = os.getenv("EXEC_CONTEXT", "{}")


class ContextError(Exception):
    pass


class ActionResponseError(Exception):
    pass


def _context() -> dict:
    context = json.loads(CONTEXT)

    # try:
    #     r = os.fdopen(READ_PIPE)
    #     json_context = json.load(r)
    # except Exception as e:
    #     print(e)

    # file_path = f"{WORKSPACE}/context.json"
    # with open(file_path, 'r', encoding='utf8') as f:
    #     json_context = json.load(f)

    return context


class ScriptManager:

    def __init__(self) -> None:

        context = _context()

        if len(context) == 0:
            raise

        # http | action | task | live
        self.exec_type = ""

        # method of http exec
        self.http_method = None
        # self.context = get_http_context()

    def http_response(self, response: dict) -> None:
        if type(response) != dict:
            raise TypeError("Response must be a dictionary")

        sys.stderr.write("__response__=" + json.dumps(response) + "||")

    def action(self, act: str, data: dict = None, with_response: bool = False,
               with_callback: bool = False, callback=None, after=None, unit="minute") -> dict:
        """
        The action function send a event to the system to execute an action exec
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

        channel = grpc.insecure_channel("localhost:8080")
        event = EventHandlerStub(channel)

        reply = event.ExecAction()
        response = {}

        if not reply.success:
            print(reply.message)
            raise ActionResponseError
        else:
            response = json.loads(reply.response)
