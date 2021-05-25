#!/usr/bin/python3
"""A module containing the HBNB cmd interpretor"""


import cmd
import string
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):

    """A class:
        The class creates a console for updating the storage engine
    """
    class_lst = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"]
    prompt = "(hbnb) "

    def default(self, line):
        """ Default overload:
            Splits argument into class, command, id, and arguments
            Uses command to call class method
            Uses id to call instance of class
            Uses arguments to change instance
            Update loops to update each given attribute in dictionary
        """
        try:
            line_lst = line.split(".")
            cls = line_lst[0]
            cmd_str = "".join(line_lst[1:])
            cmd_lst = cmd_str.split("(")
            cmd = cmd_lst[0]
            args = cmd_lst[1][:-1]
            if cmd == "destroy":
                self.do_destroy(cls + " " + args)
            if cmd == "show":
                self.do_show(cls + " " + args)
            if cmd == "all":
                self.do_all(cls)
            if cmd == "count":
                count = eval(cls + "." + cmd)
                print("{}".format(count))
            if cmd == "update":
                args_lst = args.split(", ", 1)
                if ":" not in args_lst[1]:
                    args_lst = args.split(",")
                    self.do_update(cls + " " + args_lst[0][1:-1] +
                                   " " + args_lst[1][2:-1] + args_lst[2])
                else:
                    c_lst = ["{", "'", ":", '"', "}"]
                    idnum = args_lst[0][1:-1]
                    dic = args_lst[1]
                    dic_str = ""
                    for c in dic:
                        if c in c_lst:
                            continue
                        else:
                            dic_str += c
                    attr_lst = dic_str.split(", ")
                    for item in attr_lst:
                        print(item)
                        kv_lst = item.split(" ")
                        k = kv_lst[0] + " "
                        v = '"' + kv_lst[1] + '"'
                        print(cls + " " + idnum + " " + k + v)
                        self.do_update(cls + " " + idnum + " " + k + v)
        except:
            print("*** Unknown syntax: {}".format(line))

    def do_EOF(self, arg):
        return True

    def help_EOF(self):
        print("syntax: EOF")
        print("-- termintaes the HBNBCommand loop")

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print("syntax: quit")
        print("-- termintaes the HBNBCommand loop")

    def emptyline(self):
        pass

    def do_create(self, arg):
        if arg in self.class_lst:
            class_method = eval(arg + "()")
            class_method.save()
            print("{}".format(class_method.id))
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def help_create(self):
        print("syntax: create 'class name'")
        print("-- creates an instance of the input class")

    def do_show(self, arg):
        args = arg.split()
        sig = 0
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.class_lst:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for key in models.storage._FileStorage__objects:
                if args[1] in key and args[0] in key:
                    print(str(models.storage._FileStorage__objects[key]))
                    sig = 1
                    break
            if sig == 0:
                print("** no instance found **")

    def help_show(self):
        print("syntax: show 'class name' 'instance id'")
        print("-- prints the string representation of input object")

    def do_destroy(self, arg):
        args = arg.split()
        sig = 0
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.class_lst:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            argstr = args[0] + "." + args[1]
            for key in models.storage._FileStorage__objects:
                if argstr in key:
                    new_key = key
                    sig = 1
                    break
            if sig == 0:
                print("** no instance found **")
            else:
                del models.storage._FileStorage__objects[new_key]
                models.storage.save()
                count = eval(args[0] + ".count")
                count -= 1

    def help_destroy(self):
        print("syntax: destroy 'class name' 'object id'")
        print("-- deletes the input object")

    def do_all(self, arg):
        lst = []
        if arg:
            if arg in self.class_lst:
                for k in models.storage._FileStorage__objects:
                    if arg in k:
                        lst.append(
                            str(models.storage._FileStorage__objects[k]))
            else:
                print("** class doesn't exist **")
        else:
            for k in models.storage._FileStorage__objects:
                lst.append(str(models.storage._FileStorage__objects[k]))
        if lst != []:
            print(lst)

    def help_all(self):
        print("syntax: all 'class name'")
        print("-- prints the string representation of all instances"
              " by input class name")

    def do_update(self, arg):
        sig = 0
        if arg:
            args = arg.split()
        else:
            print("** class name missing **")
            return
        if args[0] not in self.class_lst:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            for k in models.storage._FileStorage__objects:
                if args[1] in k and args[0] in k:
                    key = k
                    sig = 1
            if sig == 0:
                print("** no instance found **")
                return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            dic = models.storage._FileStorage__objects[key]
            try:
                attr = getattr(dic, args[2])
                if isinstance(attr, int):
                    setattr(dic, args[2], int(args[3][1:-1]))
                elif isinstance(attr, float):
                    setattr(dic, args[2], float(args[3][1:-1]))
                elif isinstance(attr, str):
                    setattr(dic, args[2], str(args[3][1:-1]))
            except:
                setattr(dic, args[2], str(args[3][1:-1]))
            models.storage.save()

    def help_update(self):
        print("syntax: update 'class name' 'object id' 'attribute'"
              " 'attribute value'")
        print("-- updates an instance based on class name and id")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
