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
                return error("ArgumentError", f"Invalid value for wait: '{arg}'.")

        # Check for another delay
        delay = 0
        if "delay" in arguments["vals"]:
            delay = arguments["vals"]["delay"]

            if not isinstance(delay, (int, float)):
                # Not a valid integer/float
                return error("ArgumentError", f"Invalid value for wait: '{arg}'.")

        if delay > 0:
            sleep(delay)
