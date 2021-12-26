
class HttpContext:

    def __init__(self) -> None:
        self.trigger_id = None
        self.api_name = None
        self.namespace = None
        self.group = None
        self.method = None
        self.query_string = {}
        self.body = {}


class Context:

    def __init__(self) -> None:
        self.script_id = None
        self.script_name = None
        # trigger|script
        self.run_type = None
        # http|task|action
        self.trigger_type = None

        # HTTP Context
        self.http_context = None

        # data stored in the system
        # http data context persist on namespace level
        # task data context persist on trigger level
        # action data context persist on trigger level
        # script does not store context data
        self.context_store = {}

    def set_value(self, key: str, value):
        pass

    def get_value(self, key) -> any:
        pass

