# Modules
from os import getcwd
from ..utils.bases import BaseCommand

# Command class
class Location(BaseCommand):

    def __init__(self, core):
        self.core = core

    def loc(self, arguments):

        # Print our location
        print("Sprint is currently in:")
        print(getcwd())
