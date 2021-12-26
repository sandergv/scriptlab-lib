
import json
import os
from .context import Context, HttpContext
from .script_manager import ScriptManager

WORKSPACE = os.getenv("SCRIPT_WORKSPACE")
RUN_TYPE = os.getenv("RUN_TYPE")
READ_PIPE = int(os.getenv("READ_PIPE", "0"))
POST_REQUEST = os.getenv("POST_REQUEST", '{"message": "error"}')


def get_post_body() -> dict:
    body = json.loads(POST_REQUEST)
    return body


def get_context() -> Context:
    json_context = {}
    try:
        r = os.fdopen(READ_PIPE)
        json_context = json.load(r)
    except Exception as e:
        print(e)

    # file_path = f"{WORKSPACE}/context.json"
    # with open(file_path, 'r', encoding='utf8') as f:
    #     json_context = json.load(f)

    context = Context()
    context.script_id = json_context["script_id"]
    context.script_name = json_context["script_name"]
    context.run_type = json_context["run_type"]
    context.trigger_type = json_context["trigger_type"]

    if context.trigger_type == 'http':
        http_context = HttpContext()

    return context
