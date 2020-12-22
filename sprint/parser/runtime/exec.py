# Modules
from ...utils.logging import error

# Line executer
class Executer(object):

    def __init__(self, core, commands):
        self.core = core
        self.commands = commands

    def execute(self, base, arguments):

        # Check that the command exists
        if base not in self.commands:
            return error("RuntimeError", f"The command '{base}' was not found.")

        # Run the command
        command = self.commands[base]
        func = command["function"]

        try:
            func(arguments)

        except Exception as err:
            error("ExecutionError", f"\nAn internal command error occured:\n{err}")

        except KeyboardInterrupt:
            error("ExecutionError", "Killed with CTRL+C.")
