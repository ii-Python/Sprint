# Sprint
### The command shell written in Python
---

**Please note:** I realize this is not a scripting language **or** integrated shell, this is more of a project I came up with during quarantine and decided to make. It's written completely in Python meaning it has absolutely no access to lower-level interfaces and has limited capabilities.


It's also worth noting this is still in alpha, lots of bugs are likely to occur and there is no finished functionality that is going to stay for long. Sprint also relies completely on third-party Python libraries since I'm not planning on anybody else using this or having to deal with cross-compatibility.

---

## Installation
Installing Sprint is just like installing any other software, use git.

**Recommended Method:**
```
git clone https://github.com/ii-Python/Sprint
cd Sprint

python3 -m pip install -r reqs.txt
```

**Running:**
```
run.py [path]
```

## Explanation
Sprint is a Python-based script that is supposed to mimic a command shell (ex. bash). Everything is done inside of its "runtime" which includes loading commands and executing their matched functions.

Sprint has multiple error classes similiar to Python such as `RuntimeError`, `ReadError`, `PermissionError`, etc. The error format is `[ErrorType] Error message here`. If the error occurs from within a file, the error message will also contain the filename and the line number.

The amount of commands and functionality is limited, but it still has a few features including `write`, `wait`, `clear`, and more. Later on I might make a full-on documentation for this but that depends on if I have time to continue working on this project.
