import cmd
"""A basic console called BnkeTia"""
class Console(cmd.Cmd):
    prompt = "BnB$ "
Console().cmdloop()
