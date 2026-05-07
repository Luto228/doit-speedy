#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: github <command> [args]")
        print("Commands: doit, find")
        return

    if sys.argv[1] == "doit":
        import doit
        doit.main(sys.argv[2:])
    elif sys.argv[1] == "find":
        import find
        find.main(sys.argv[2:])
    else:
        print(f"Unknown command: {sys.argv[1]}")

if __name__ == "__main__":
    main()