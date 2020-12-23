# Modules
from ..utils.logging import error
from ..utils.bases import BaseCommand

# Command class
class Function(BaseCommand):

    def __init__(self, core):
        self.core = core

    def func(self, arguments):

        # Check the provided option
        try:
            opt = arguments["pos"][0]

        except (KeyError, IndexError):
            return error("ArgumentError", "Nothing provided to process.")

        if opt == "assign":

            # Create a new function
            arguments = arguments["pos"][1:]
            if len(arguments) < 2:
                return error("ArgumentError", "Missing required name and function data.")

            name = arguments[0]
            data = arguments[1]

            # Save to our local database
            self.core.functions[name] = data
            return

        # Execute function
        if opt not in self.core.functions:
            return error("FunctionError", f"'{opt}' is not a defined function.")

        data = self.core.functions[opt]
        self.core.execute(data)
