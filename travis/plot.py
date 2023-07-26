#!/usr/bin/env python

import argparse
import subprocess
import os

def main():
    print("Running plot.py")

    parser = argparse.ArgumentParser(description='Path Finder')
    parser.add_argument('--path', required=True, help='Path to full path output file')
    parser.add_argument('--metadata', required=True, help='Dataframe with columns Gene, Length, Label')
    parser.add_argument('--output', required=True, help='Output folder')
    args = parser.parse_args()

    # Check if input files exist
    if not os.path.exists(args.path):
        print(f"Error: The specified path file '{args.path}' does not exist.")
        return
    if not os.path.exists(args.metadata):
        print(f"Error: The specified metadata file '{args.metadata}' does not exist.")
        return

    # Check if the R script file exists
    r_script = "gggenes.R"
    if not os.path.exists(r_script):
        print(f"Error: The R script '{r_script}' does not exist.")
        return

    # Add the rest of the logic for the attribute addition script

    arguments = [args.path, args.metadata, args.output]
    subprocess.run(["Rscript", r_script] + arguments)

if __name__ == '__main__':
    main()
