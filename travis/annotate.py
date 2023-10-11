#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2023--, Travis development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import pandas as pd
import networkx as nx
import re
import argparse
import os

def validate_key(key):
    # Remove any non-alphanumeric characters from the key
    key = re.sub(r'\W+', '_', key)
    return key

def sanitize_value(value):
    # Remove any special characters that may cause issues in the graph
    sanitized_value = str(value).replace('"', '')
    return sanitized_value

def annotate(graph_file, dataframe_file, graph_column, dataframe_column):
    # Check if input files exist
    if not os.path.exists(graph_file):
        print(f"Error: The specified graph file '{graph_file}' does not exist.")
        return
    if not os.path.exists(dataframe_file):
        print(f"Error: The specified dataframe file '{dataframe_file}' does not exist.")
        return

    # Read the graph file
    graph = nx.read_gml(graph_file)

    # Read the dataframe
    dataframe = pd.read_csv(dataframe_file, delimiter="\t", header=0)

    # Iterate through each node and add the necessary data attributes
    for node in graph.nodes():
        name = graph.nodes[node][graph_column]
        if name:
            additional_data = dataframe[dataframe[dataframe_column] == name]
            if not additional_data.empty:
                # Convert the selected row to a dictionary
                additional_data = additional_data.iloc[0].to_dict()
                validated_dict = {
                    validate_key(key): sanitize_value(value)
                    for key, value in additional_data.items()
                }
                graph.nodes[node].update(validated_dict)

    # Save the updated graph
    updated_graph_file = graph_file.replace(".gml", "_updated.gml")
    nx.write_gml(graph, updated_graph_file)
    print(f"Graph file with updated values saved to '{updated_graph_file}'.")

def main():
    print("Running annotate.py")
    parser = argparse.ArgumentParser(description='Attribute adder')
    parser.add_argument('--graph', required=True, help='Path to the graph file')
    parser.add_argument('--metadata', required=True, help='Path to the dataframe')
    parser.add_argument('--graph_name', required=True, help='Reference for the graph')
    parser.add_argument('--metadata_column', required=True, help='Reference column for the dataframe')
    args = parser.parse_args()

    annotate(args.graph, args.metadata, args.graph_name, args.metadata_column)
    
if __name__ == '__main__':
    main()
