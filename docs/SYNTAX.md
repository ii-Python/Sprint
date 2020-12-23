# Sprint Syntax
---

This page of the Sprint documentation talks about the syntax of Sprint and how it operates.

The basic syntax is `[command] <positional arguments> <flags> <keypair arguments>` which is true for all commands.

---
### Basic syntax

For example, to display some text to the console:
```
write "Hello, world!"
```
In this case `"Hello, world!"` is interpreted as a positional argument since it is not prefixed with a flag character. It is also worth noting that Sprint will automatically convert positional arguments into their appropriate Python datatypes (strings, integers, floats, etc).

---
### Flags and keypairs
Sprint also has a method of using flags, similiar to command switches in Windows. These flags **must** be prefixed with `--` and then should proceed with the name of the flag. Flags can contain any character as long as it is not whitespace.

Flags can also contain values, which turns them into a keypair. To create a keypair you could simply use `--key=value`. In this case Sprint will automatically convert the value to its appropriate datatype but the key will always remain as a string.

```
; Basic flags
write "Hello, world!" --quiet  ; Example, there is no quiet flag

; Keypairs
wait --delay=5  ; No more positional time delays :D
```
