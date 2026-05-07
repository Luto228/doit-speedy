import sys
import os

def main(words):
    length = len(words)
    if length < 1 or length > 5:
        print("\n--- Project Auto-Starter ---")
        print("Usage: github doit <repo_name> [public on/off] [readme on/off] [license/off] [gitignore/off]")
        print("\nSetup: alias github='/your_path/main.py' in .bashrc")
        sys.exit(1)
    name = words[0]
    command = f'gh repo create {name}'
    if length >= 2:
        if words[1] == 'on':
            command += ' --public'
        elif words[1] == 'off':
            command += ' --private'
    if length >= 3:
        if words[2] == 'on':
            command += ' --add-readme'
    if length >= 4:
        if words[3] != 'off':
            command += f' --license {words[3].lower()}'
    if length == 5:
        if words[4] != 'off':
            command += f' --gitignore {words[4]}'

    os.system(command) 