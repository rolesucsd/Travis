#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2023--, Travis development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import argparse
import subprocess

def main():
    print("Running plot.py")

    parser = argparse.ArgumentParser(description='Path Finder')
    parser.add_argument('--path', required=True, help='Path to full path output file')
    parser.add_argument('--metadata', required=True, help='Dataframe with columns Gene, Length, Label')
    parser.add_argument('--output', required=True, help='Output folder')
    args = parser.parse_args()

    arguments = [args.path, args.metadata, args.output]
    subprocess.run(["Rscript", "gggenes.R"] + arguments)

if __name__ == '__main__':
    main()
