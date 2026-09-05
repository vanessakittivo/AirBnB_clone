#!/usr/bin/python3
"""Command interpreter for the AirBnB project."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command interpreter."""

    prompt = "(hbnb) "


if __name__ == "__main__":
    HBNBCommand().cmdloop()
