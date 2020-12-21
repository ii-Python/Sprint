# Modules
from .colors import colored

# Logger functions
def error(errType, errMessage):
    print(colored(f"[{errType}] {errMessage}", "red"))
    exit()

def warn(warnType, warnMessage):
    print(colored(f"[{warnType}] {warnMessage}", "yellow"))

# Logging class
class Logger(object):

    def __init__(self, filename, nofile = False):
        self.filename = filename
        self.nofile = nofile

    def error(self, lineNum, errType, errMessage):

        if not self.nofile:
            errMessage = f"{self.filename}:{lineNum} {errMessage}"

        error(errType, errMessage)

    def warn(self, lineNum, warnType, warnMessage):

        if not self.nofile:
            warnMessage = f"{self.filename}:{lineNum} {warnMessage}"

        error(warnType, warnMessage)
