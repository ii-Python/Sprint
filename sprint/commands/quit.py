# Modules
from ..utils.logging import error
from ..utils.bases import BaseCommand

# Command class
class Quit(BaseCommand):

    def __init__(self, core):
        self.core = core

    def quit(self, arguments):

        # Check for a status code
        code = 0
        if arguments["pos"]:
            code = arguments["pos"][0]

        if "code" in arguments["vals"]:
            code = arguments["vals"]["code"]

        # Ensure its valid
        if not isinstance(code, int):
            return error("ArgumentError", "Specified value is not an integer.")

        # Exit properly
        exit(code)
