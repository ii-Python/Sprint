# Custom quit function meant for
# exiting with a specific exit code
def main(args, flags, core):

    # Locate our exit code
    code = 1
    if args:
        code = args[0]

    exit(code)
