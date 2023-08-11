#!/usr/bin/python3
"""Defines the entry point of our command interprator."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
import re
from shlex import split


def tokenizer(arg):
    """Parsses the arguments into valid tokens.
    Args:
        :: arg: string containing user input from terminal.
    """

    braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if braces:
        tokens = split(arg[:braces.span()[0]])
        token = [brace.strip(",") for brace in tokens]
        token.append(braces.group())
        return token
    elif brackets:
        tokens = split(arg[:brackets.span()[0]])
        token = [bracket.strip(",") for bracket in tokens]
        token.append(brackets.group())
        return token
    else:
        return [tokens.strip(",") for tokens in split(arg)]


class HBNBCommand(cmd.Cmd):
    """Defines the console intrprator.
       Attr:
           :: prompt(str): The consoles prompt."""

    prompt = "(hbnb) "
    __classnames = {
        "BaseModel",
        "User",
        "Place",
        "City",
        "State",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """Specifies the default behaviour incase of unrecognised input.
        Args:
            :: arg(str): user input.
        """

        argnames = {
            "show": self.do_show,
            "all": self.do_all,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
            }

        dotpattern = r"\."
        argpattern = r"\((.*?)\)"
        dotrslt = re.search(dotpattern, arg)
        if dotrslt is None:
            print("*** Unknown syntax: {}".format(arg))
            return False
        else:
            args = [arg[:dotrslt.span()[0]], arg[dotrslt.span()[1]:]]
            argrslt = re.search(argpattern, args[1])
            if argrslt is not None:
                args1 = [args[1][:argrslt.span()[0]], argrslt.group()[1:-1]]
                if args1[0] in argnames.keys():
                    command = "{} {}".format(args[0], args1[1])
                    return argnames[args1[0]](command)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """Does nothing on empty line + Enter key."""
        pass

    def do_EOF(self, arg):
        """Quits the program on EOF signal."""
        return True

    def do_quit(self, arg):
        """Exits the console/program.
        Usage: $ quit
        """
        return True

    def do_create(self, arg):
        """Creates and prints id of a new instance.
        Usage: $ create <class name>
        """
        args = tokenizer(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints a str representation of an instance.
        Usage: $ show <classname> <instance id>
        """
        args = tokenizer(arg)
        allinstances = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in allinstances:
            print("** no instance found **")
        else:
            print(allinstances["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an intance based on the class name and id.
        usage: $ destroy <classname> <instance id>
        """

        args = tokenizer(arg)
        allinstances = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in allinstances:
            print("** no instance found **")
        else:
            del allinstances["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances.
        Usage: $ all <class name>(optional)"""

        args = tokenizer(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        else:
            allinstances = storage.all()
            tempstr = []
            for instance in allinstances.values():
                if len(args) > 0 and args[0] == instance.__class__.__name__:
                    tempstr.append(instance.__str__())
                elif len(args) == 0:
                    tempstr.append(instance.__str__())
            print(tempstr)

    def do_update(self, arg):
        """Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> <attribute value>
        """

        allinstances = storage.all()
        args = tokenizer(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in allinstances:
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            parentobj = allinstances["{}.{}".format(args[0], args[1])]
            if args[2] in parentobj.__class__.__dict__.keys():
                attr_type = type(parentobj.__class__.__dict__[args[2]])
                parentobj.__dict__[args[2]] = attr_type(args[3])
            else:
                parentobj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            parentobj = allinstances["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if (key in parentobj.__class__.__dict__.keys() and
                        type(parentobj.__class__.__dict__[key]) in
                        {int, float, str}):
                    attr_type = type(parentobj.__class__.__dict__[key])
                    parentobj.__dict__[key] = attr_type(value)
                else:
                    parentobj.__dict__[key] = value
        storage.save()

    def do_count(self, arg):
        """Prints the number of instances of a class.
        Usage: $ count <class> / $ <class>.count()
        """

        args = tokenizer(arg)
        allinstances = storage.all()
        count = 0
        for instance in allinstances.values():
            if args[0] == instance.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
