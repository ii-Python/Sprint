# Modules
from ..utils.bases import BaseCommand

# Command class
class Write(BaseCommand):

    def __init__(self, core):
        self.core = core

    def write(self, arguments):

        # Print our our arguments
        for arg in arguments["pos"]:
            print(arg)

        # Just in case nothing was provided
        if not arguments["pos"]:
            print()  # Blank line
