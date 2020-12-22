# Modules
import sprint

# Credit message
print(sprint.colored(f"Sprint v{sprint.__version__} by iiPython", "yellow"))
print()

# Main loop
while True:

    try:
        cmd = input(sprint.colored(">>> ", "green"))

    except KeyboardInterrupt:
        print()  # Stop weird line break issues
        continue

    # Run our command
    parser = sprint.SprintParser(cmd)
    parser.execute()
