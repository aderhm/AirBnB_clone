#!/usr/bin/python3
"""
This file defines the HBnB console.
"""

import cmd
from models import base_model, storage


class HBNBCommand(cmd.Cmd):
    """
    This class defines the HBnB command interpreter.
    """

    prompt = "(hbnb) "
    __classes = ["BaseModel"]

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

    def do_create(self, arg):
        """Creates a new instance of a given class and prints its id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel":
                print("{}".format(base_model.BaseModel().id))
                storage.save()            


if __name__ == '__main__':
    HBNBCommand().cmdloop()
