#!/usr/bin/env python3
import sys
import os

def main():
    length = len(sys.argv)
    if length < 2 or length > 6:
        print("\n--- Project Auto-Starter ---")
        print("Usage: doit <repo_name> [public on/off] [readme on/off] [license/off] [gitignore/off]")
        print("\nSetup: alias doit='/your_path/main.py' in .bashrc")
        sys.exit(1)
    name = sys.argv[1]
    command = f'gh repo create {name}'
    if length >= 3:
        if sys.argv[2] == 'on':
            command += ' --public'
        elif sys.argv[2] == 'off':
            command += ' --private'
    if length >= 4:
        if sys.argv[3] == 'on':
            command += ' --add-readme'
    if length >= 5:
        if sys.argv[4] != 'off':
            command += f' --license {sys.argv[4].lower()}'
    if length == 6:
        if sys.argv[5] != 'off':
            command += f' --gitignore {sys.argv[5]}'
    os.system(command)
if __name__ == "__main__":
    main()