#!/bin/python3

'''
main source code of nemsh
'''
import subprocess
import os
import sys

# executing NOT built-in commands
def exec_cmd(command):
    '''
    this function executes command of nemsh
    '''
    try:
        if len(command.split()) == 1:
            subprocess.run(command,check=True)
        else:
            subprocess.run(command.split(), check=True)
    except subprocess.CalledProcessError as err:
        print(f"[e]: {err}")
    except FileNotFoundError:
        print(f"[e]: command not found. ({command})")

# implementing simple shell commands (echo, cd, improved ls)
def echo(args):
    '''
    this function prints echo output to stdout
    '''
    print(" ".join(args))

def change_dir(directory):
    '''
    this is a cd equivalent of nemsh
    '''
    try:
        os.chdir(directory[0])
    except (NotADirectoryError, FileNotFoundError):
        print("[e] No such file or directory, make sure you did not misspell")
    except IndexError:
        print("Usage: cd <directory>")

# shell loop
def sh_loop():
    '''
    main function
    '''
    while True:
        command = input(f"{os.getcwd()} $ ")
        if not command:
            continue
        args = command.split()

        if args[0] == "exit":
            sys.exit()
        elif args[0] == "cd":
            change_dir(args[1:])
        elif args[0] == "echo":
            echo(args[1:])
        else:
            exec_cmd(command)

if __name__ == "__main__":
    sh_loop()
