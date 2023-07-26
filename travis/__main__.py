#!/usr/bin/env python

import argparse
import sys

from .annotate import main as annotate
from .pathfinder import main as pathfinder
from .plot import main as plot

def main():
    if len(sys.argv) < 2 or not sys.argv[1].startswith("travis-"):
        print("Please use 'travis' followed by a valid command.")
        print("Available commands: pathfinder, annotate, plot")
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

    command = sys.argv[1][7:]  # Remove "travis-" prefix to get the command
    if command == 'pathfinder':
        pathfinder()
    elif command == 'annotate':
        annotate()
    elif command == 'plot':
        plot()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: pathfinder, annotate, plot")
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

if __name__ == "__main__":
    main()
