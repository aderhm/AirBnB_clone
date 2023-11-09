#!/usr/bin/python3
"""
This file defines the HBnB console.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines the HBnB command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """The signal to exit the program (EOF or Ctrl+D).
        """
        print("")
        return True

    def emptyline(self):
        """Do nothing when receiving an empty line.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
