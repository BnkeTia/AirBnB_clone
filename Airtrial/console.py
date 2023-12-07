#!/usr/bin/python3
import cmd
"""A basic console called BnkeTia"""


class Console(cmd.Cmd):
    intro = "Welcome to BB console, edit your website, Kings"
    prompt = "BnB$ "

    def yo_help(self, arg):
        """Show help message"""
        super().do_help(arg)


    def yo_quit(self, arg):
        """Setting condition to exit the console"""
        print("logging out...")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def default(self, line):
        """Called on an uknown command"""
        print(f"Uknown command: {line}. Type 'help' for compartible commands")

if __name__ == "__main__":

    Console().cmdloop()
