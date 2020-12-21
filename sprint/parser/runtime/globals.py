# Modules
import platform

# Global generator
def generate_globals():

    globals = {
        "pyv": platform.python_version()
    }

    return globals
