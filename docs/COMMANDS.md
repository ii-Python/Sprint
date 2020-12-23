# Sprint Commands
---

Sprint by default comes with various commands helpful for interacting with the host operating system. This page will primarily focus on creating custom commands.

**⚠️ The normal path for sprint commands is `sprint/commands`.**

---
### Creating a new command
In order to create a command, first create your file inside of the sprint command folder. This filename should be the name of the command with a `.py` python extension.

For example, if you wanted to make a `tutorial` command your path would be `sprint/commands/tutorial.py`.

---
#### Constructing the command class
Sprint commands are built inside of Python classes which subclass Sprints BaseCommand class. Before creating this command class, you should important the `BaseCommand` class first:
```python
from ..utils.bases import BaseCommand
```

Now that you have the base class imported, you can create your command class. The name of this class doesn't matter as long as it does not match anything imported. I will just call the class `TutorialCommand` for simplicity:
```python
from ..utils.bases import BaseCommand

class TutorialCommand(BaseCommand):

    def __init__(self, core):
        self.core = core
```

Initialized sprint commands always are referenced the `core` object which internally is the sprint `storage` object containing functions, globals, etc. **Make sure you are always ready to receive this!**

#### Creating the main function
To identify the correct command to run, sprint will scan through command classes until it finds a function with the same name as the filename. For example, if our `TutorialCommand` class had a `main` function along with a `tutorial` function, sprint would identify the `tutorial` function as the command and would silently ignore the `main` function.

This function takes one positional argument which is the provided arguments passed in from the interpreter.
```python
from ..utils.bases import BaseCommand

class TutorialCommand(BaseCommand):

    def __init__(self, core):
        self.core = core

    def tutorial(self, arguments):
        print("Hello from the tutorial command!")
        print("Provided arguments: " + str(arguments))
```

The arguments provided are a dictionary containing the following:
```json
{
    "pos": [
        "Positional argument #1",
        "Positional argument #2",
        "How about another?"
    ],
    "flags": [
        "setup",
        "quiet",
        "another-flag"
    ],
    "vals": {
        "key": "value",
        "key2": "value2"
    }
}
```

For more information on the provided arguments, it is recommended to follow up this document with `ARGUMENTS.md`.
