#!/usr/bin/python3
"""This a Python made console command interpreter"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    my_classes = {
        "BaseModel": BaseModel
    }

    def do_EOF(self, line=None):
        """This method exit the console when Ctrl-D (EOF) is pressed"""
        print()
        return True

    def do_quit(self, line=None):
        """This method exit the console at the given of quit command"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """This method create a new instance of a given object and save it"""
        if line == "":
            print("** class name missing **")
            return False

        command_list = line.split()
        command = command_list[0]
        if command not in self.my_classes.keys():
            print("** class doesn't exist **")
            return False

        new_obj = self.my_classes[command]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """
        This method print string representation of an
        instance based on the class name and id
        """
        if line == "":
            print("** class name missing **")
            return False

        command_list = line.split()
        command = command_list[0]
        command_id = command_list[1]
        if command not in self.my_classes.keys():
            print("** class doesn't exist **")
            return False
        
        if command_id == None:
            print("** instance id missing **")
            return False
        
        print(FileStorage.all())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
