#!/usr/bin/python3
"""
This file defines the HBnB console.
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    This class defines the HBnB command interpreter.
    """

    prompt = "(hbnb) "
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

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
        Usage: create <class>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class> <id>
        """
        o_dict = storage.all()
        args = arg.split(" ")
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in o_dict:
            print("** no instance found **")
        else:
            print(o_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Usage: destroy <class> <id>
        """
        o_dict = storage.all()
        args = arg.split(" ")
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in o_dict:
            print("** no instance found **")
        else:
            del o_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(slef, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all or all <class>
        """
        o_dict = storage.all()
        if arg:
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            else:
                all_insts = [f'{value}' for key, value in o_dict.items()
                             if key.startswith(arg)]
        else:
            all_insts = [f'{value}' for key, value in o_dict.items()]
        print(all_insts)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        o_dict = storage.all()
        args = shlex.split(arg)
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in o_dict:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = o_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value_type(args[3].strip('"'))
            else:
                obj.__dict__[args[2]] = args[3].strip('"')
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
