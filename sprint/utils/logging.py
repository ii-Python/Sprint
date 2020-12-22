# Modules
from .colors import colored

# Logger functions
def error(errType, errMessage):
    print(colored(f"[{errType}] {errMessage}", "red"))

def warn(warnType, warnMessage):
    print(colored(f"[{warnType}] {warnMessage}", "yellow"))
