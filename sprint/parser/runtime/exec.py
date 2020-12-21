# Modules
import inspect
import importlib

from os import listdir
from os.path import exists, isfile

from ...utils.logging import error, warn

# Line executer
class Executer(object):

    def __init__(self, core):
        self.core = core
        self.commands = {}

        self.load_commands()

        # Easy access for commands
        self.core.executer = self

    def load_commands(self, directory = "sprint/parser/commands"):

        # Check directory existance
        if not exists(directory):
            self.error("FileError", "The command directory could not be found.")

        # Locate all of our commands
        for file in listdir(directory):

            # Ensure this is a python file
            if not file.endswith(".py"):
                continue

            # Try to load it
            try:
                m = importlib.import_module(directory.replace("/", ".") + "." + file[:-3])

                # Scan for our main function
                for name, function in inspect.getmembers(m, inspect.isfunction):
                    if name == "main":

                        # Load the function into our command list
                        self.commands[file[:-3]] = {
                            "function": function
                        }

            except Exception as err:
                error("LoadError", f"The '{file}' command failed to import properly.\nPython traceback: {err}")

    def execute(self, line, base, arguments, flags):

        # Check that the command exists
        if base not in self.commands:
            self.core.flogger.error(line, "RuntimeError", f"The command '{base}' was not found.")

        # Run the command
        command = self.commands[base]
        func = command["function"]

        try:
            func(arguments, flags, self.core)

        except Exception as err:
            self.core.flogger.error(line, "ExecutionError", f"\nAn internal command error occured:\n{err}")

        except KeyboardInterrupt:
            self.core.flogger.error(line, "ExecutionError", "Killed with CTRL+C, have a nice day.")
            exit()
