import os
import sys

def main(words):
    command = None
    lword = len(words)
    if lword < 1 or lword == 2:
        print("\n--- Find projects ---")
        print("Usage: github find <repo_name> OR <repo_name> from <autor_name>")
        print("\nSetup: alias github='/your_path/main.py' in .bashrc")
        sys.exit(1)
    if lword == 1:
        try:
            project_name = words[0]
            os.system(f"gh search repos {project_name} --limit 5 && xdg-open https://github.com/search?q={project_name}")
        except Exception:
            raise ValueError(f"Something went wrong...")
    elif lword > 2 and words[1] == "from":
        try :
            project_name = words[0]
            autor_name = words[2]
            os.system(f"gh search repos{project_name} --limit 5 && xdg-open https://github.com/{autor_name}/{project_name}")
        except Exception:
            raise ValueError(f"Something went wrong...")
    else:
        print("\n--- Find projects ---")
        print("Usage: github find <repo_name> OR <repo_name> from <autor_name>")
        print("\nSetup: alias github='/your_path/main.py' in .bashrc")