from scriptmanager.context import Context


class ScriptManager:

    base_url = "http://localhost:8910/__internal"

    def __init__(self, context: Context) -> None:

        self.context = context

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
