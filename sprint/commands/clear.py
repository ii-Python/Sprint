# Modules
import subprocess
from os import name
from ..utils.bases import BaseCommand

# Command class
class Clear(BaseCommand):

    def __init__(self, core):
        self.core = core

    def clear(self, arguments):

        # Locate our command
        command = "clear"
        if name == "nt":
            command = "cls"

        # Execute
        subprocess.run([command])
