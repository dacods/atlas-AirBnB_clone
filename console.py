#!/usr/bin/python3
"""Command Interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Class defining the Command interpreter for HBNB"""
    prompt = '(hbnb) '

    def do_quit(self, command_arg):
        """Function to quit the command and exit"""
        return (True)

    def do_EOF(self, command_arg):
        """Function to use EOF(end of file)
        command to exit -- Ctrl+D"""
        print()
        return (True)

    def emptyline(self):
        """Function to does nothing on an empty line
        + ENTER"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
