# Modules
from ..utils.logging import error
from ..utils.bases import BaseCommand

# Command class
class Set(BaseCommand):

    def __init__(self, core):
        self.core = core

    def set(self, arguments):

        # Locate our values
        values = arguments["vals"]

        if arguments["pos"]:

            try:
                vals = arguments["pos"]

                key = vals[0]
                value = vals[1]

                values[key] = value

            except IndexError:
                return error("ArgumentError", "Missing required values for set statement.")

        # Missing arguments
        if not values:
            return error("ArgumentError", "Missing required values for set statement.")

        # Join together our environ variables
        self.core.globals = self.core.globals | values
