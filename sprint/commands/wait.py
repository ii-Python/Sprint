# Modules
from time import sleep
from ..utils.logging import error
from ..utils.bases import BaseCommand

# Command class
class Wait(BaseCommand):

    def __init__(self, core):
        self.core = core

    def wait(self, arguments):

        # Loop through EACH argument
        for arg in arguments["pos"]:
            if isinstance(arg, (int, float)):
                sleep(arg)

            else:
                # Not a valid integer/float
                error("ArgumentError", f"Invalid value for wait: '{arg}'.")
