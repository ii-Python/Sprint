# Modules
from readchar import readkey

# Set function for changing environment variables
# within the runtime
def main(args, flags, core):

    # Make sure we have our args
    if not args:
        core.logger.error("RuntimeError", "Missing environ key and value to set.")

    if not len(args) > 1:
        core.logger.error("RuntimeError", f"Missing environment value for key '{args[0]}'.")

    # Collection
    key = args[0]
    value = args[1]

    # Special values
    if value == "input":
        value = input()

    elif value == "keypress":
        value = readkey()  # External library because why not

    # Set our value
    core.environment[key] = value
