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
    this function execute every other command (that isn't implemented to nemsh)
    '''
    try:
        if len(command.split()) == 1:
            subprocess.run(command, check=True)
        else:
            subprocess.run(command.split(), check=True)
    except subprocess.CalledProcessError as err:
        print(f"[error]: {err}")
    except FileNotFoundError:
        print(f"[error: command not found. ({command})")

# implementing simple shell commands (echo, cd, improved ls)
def echo(args):
    '''
    this function prints echo output to stdout
    '''
    if len(args) == 1 and args[0][0] == "$":
        print(os.getenv(args[0][1:]))
    else:
        print(" ".join(args))

def change_dir(directory):
    '''
    this is nemsh's cd implementation
    '''
    try:
        os.chdir(directory[0])
    except (NotADirectoryError, FileNotFoundError):
        print("[error] No such file or directory.")
    except IndexError:
        print("Usage: cd <directory>")

def export_var():
    '''
    this function adds environment variables support
    '''
    var_name = input("\x1b[32m>\x1b[0m variable name: ")
    var_val = input("\x1b[32m>\x1b[0m value: ")
    os.environ[var_name] = var_val
        
# shell loop
def sh_loop():
    '''
    the shell loop
    '''
    while True:
        command = input(f"\x1b[32m{os.getcwd()}\x1b[0m ({os.getlogin()}@{os.uname()[1]}) $ ")
        if not command:
            continue
        args = command.split()

        if len(args) == 1 and args[0] == "exit":
            sys.exit()
        elif len(args) == 2 and args[0] == "exit":
            try:
                if int(args[1]) > 255:
                    print("[e] exit codes are between 0-255")
                else:
                    sys.exit(args[1])
            except ValueError:
                print("[e] exit code expected to be int")
        elif args[0] == "cd":
            change_dir(args[1:])
        elif args[0] == "echo":
            echo(args[1:])
        elif args[0] == "export":
            export_var()
        else:
            exec_cmd(command)

if __name__ == "__main__":
    try:
        sys.path.append(f"/home/{os.getlogin()}/.config/nemsh/")
        import rc
        rc.main()
    except Exception:
        # pass because user may not have the rc file (it is not necessary to have one)
        pass
    sh_loop()
