# Simple function for writing in the terminal
def main(args, flags, core):

    # Loop through our arguments and print each one
    for arg in args:
        print(arg)

    # In case we wanted a line break...
    if not args:
        print()
