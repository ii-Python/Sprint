# Modules
import sprint
import platform

# Credit message
print(sprint.colored(f"Sprint v{sprint.__version__} by iiPython", "yellow"))
print(sprint.colored(f"Python version {platform.python_version()}, running on {platform.system()}", "yellow"))
print()

# Main loop
while True:

    try:
        cmd = input(sprint.colored("Sprint >>> ", "green"))

    except KeyboardInterrupt:
        print()  # Stop weird line break issues
        continue

    # Run our command
    parser = sprint.SprintParser(cmd)
    parser.execute()
