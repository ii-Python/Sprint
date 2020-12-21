# Modules
from time import sleep

# Simple wait function
# Just uses time.sleep for now
def main(args, flags, core):

    # Locate our time
    if not args:
        core.logger.error("RuntimeError", "Expecting an integer to wait for!")

    sleep(args[0])
