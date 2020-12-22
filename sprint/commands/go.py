# Modules
from os import chdir
from os.path import exists, isdir

from ..utils.logging import error
from ..utils.bases import BaseCommand

# Command class
class Go(BaseCommand):

    def __init__(self, core):
        self.core = core

    def go(self, arguments):

        # Fetch path
        path = None
        if arguments["pos"]:
            path = arguments["pos"][0]

        if not path:
            return error("ArgumentError", "No path specified to move to.")

        # Ensure its valid
        if not exists(path):
            return error("PathError", "The specified path does not exist.")

        elif not isdir(path):
            return error("PathError", "The specified path is not a directory.")

        # Move to our directory
        try:
            chdir(path)

        except PermissionError:
            return error("PermissionError", "Permission denied to access folder.")
