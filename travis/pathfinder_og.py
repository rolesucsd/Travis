#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2023--, Travis development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import networkx as nx
import pandas as pd
import numpy as np
import copy
from collections import Counter
import argparse


pathDict = {}
memberDict = {}

def traverse(graph, start, end, path, members):
    """
    A recursive function to find all possible paths in a graph.

    Parameters
    ----------
    graph: a graph object of networkx
        This object has the following attributes:
            graph.degree : list
                The amount of edges per node
    start: str
        str reference of the current node
    end: str
        str reference of the end node
    path: list
        order or nodes in current path
    members: list
        details genomeIDs currently being followed in path
    """    
    if nx.get_node_attributes(graph, 'name')[start] not in path:
        # Add the new node to the path
        path.append(nx.get_node_attributes(graph, 'name')[start])

        # If the path is greater than 30, stop traversing
        # Or if we've reached the end of the path, end the path here
        if start == end:
            name = 'path' + str(len(pathDict))
            pathDict[name] = copy.deepcopy(path)
            memberDict[name] = copy.deepcopy(members)

        # If not, go through all neighbors of the current node
        elif len(path) <= 30:
            for neighbour in nx.all_neighbors(graph, start):
                # Check if the neighbour is already in the path
                if nx.get_node_attributes(graph, 'name')[neighbour] not in path:
                    # Find the members in common between old and new edge
                    newMembers = graph.get_edge_data(start, neighbour)['genomeIDs'].split(';')
                    intersectionMembers = [c for c in members if c in newMembers]

                    # There must be at least one member in common to continue
                    if len(intersectionMembers) >= 1:
                        traverse(graph, neighbour, end, path, intersectionMembers)

        path.pop()
    return 0

def pathfinder(file, start, end):
    """
    Load graph and starting node
    """

    G = nx.read_gml(file)
    G = G.to_undirected()

    # Find the node based on the name in string form
    start_key = next(x for x, y in G.nodes(data=True) if y['name'] == start)
    end = next(x for x, y in G.nodes(data=True) if y['name'] == end)

    # Compare genomeIDs between edge and potential next edge
    path = []
    traverse(G, start_key, end, path, nx.get_node_attributes(G, 'genomeIDs')[start_key].split(';'))
    print(path)

    os.makedirs(output_folder, exist_ok=True)

    # Create an empty list to store the final data
    formatted_data = []

    # Process each path and its corresponding gene list
    for path_name, gene_list in pathDict.items():
        for position, gene in enumerate(gene_list, start=1):
            formatted_data.append({
                'Gene': gene,
                'Path': path_name,
                'Position': position
        })

    formatted_df = pd.DataFrame(formatted_data)
    formatted_df.to_csv(os.path.join(output_folder, f"{start}_path_full.csv"), sep='\t', index=False)

    df = pd.DataFrame({k: Counter(v) for k, v in pathDict.items()}).fillna(0).astype(int)
    df.to_csv(os.path.join(output_folder, f"{start}_path.csv"), sep='\t')
    nodes = df.index
    node_keys = []
    for i in nodes:
        new_key = next(x for x, y in G.nodes(data=True) if y['name'] == i)
        node_keys.append(new_key)
    G_sub = G.subgraph(node_keys)
    nx.write_gml(G_sub, os.path.join(output_folder, f"{start}_graph.gml"))

    df = pd.DataFrame(columns=['Path', 'Member'])
    for key, value in memberDict.items():
        df2 = {'Path': key, 'Member': value}
        df = df.append(df2, ignore_index=True)
    df = df.explode('Member').reset_index(drop=True)

    df.to_csv(os.path.join(output_folder, f"{start}_member.csv"), sep='\t', index=False)


def main():
    print("Running pathfinder.py")
    parser = argparse.ArgumentParser(description='Path Finder')
    parser.add_argument('--graph', required=True, help='Path to the graph file')
    parser.add_argument('--start', required=True, help='Start gene')
    parser.add_argument('--stop', required=True, help='Stop gene')
    parser.add_argument('--output', required=True, help='Output folder')
    args = parser.parse_args()

    pathfinder(args.graph, args.start, args.stop, args.output)

if __name__ == '__main__':
    main()