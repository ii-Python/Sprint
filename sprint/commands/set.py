# Modules
from readchar import readkey
from ..utils.logging import error
from ..utils.bases import BaseCommand

# Command class
class Set(BaseCommand):

    def __init__(self, core):
        self.core = core
        self.func_name = "set_"

    def process_value(self, value):

        # Check for custom values
        if value == "keypress":
            value = readkey()

        # Return to process
        return value

    def set_(self, arguments):

        # Locate our values
        values = arguments["vals"]

        if arguments["pos"]:

            try:
                vals = arguments["pos"]
                key = vals[0]

                value = self.process_value(vals[1])

                # Exceptions are handled inside of the function
                if not value:
                    return

                values[key] = self.core.parser.convert_datatype(value, add_quotes = True)

            except IndexError:
                return error("ArgumentError", "Missing required values for set statement.")

        # Missing arguments
        if not values:
            return error("ArgumentError", "Missing required values for set statement.")

        # Join together our environ variables
        self.core.globals = self.core.globals | values
