#!/usr/bin/env python

import sys

from .annotate import main as annotate
from .pathfinder import main as pathfinder
from .plot import main as plot

def main():
    if len(sys.argv) < 2:
        print("Available commands: pathfinder, annotate, plot")
    else:
        command = sys.argv[1]
        if command == "pathfinder":
            pathfinder_main()
        elif command == "annotate":
            attribute_main()
        elif command == "plot":
            plot_main()
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
