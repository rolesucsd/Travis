# Graph Attribute Adder

This script allows you to add additional data attributes from a dataframe to a graph file.

## Prerequisites

- Python 3.x
- pandas library
- networkx library

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies by running the following command:

```sh
pip install pandas networkx
```

## Usage

Run the script with the following command:

```sh
python script.py --graph <path_to_graph_file> --dataframe <path_to_dataframe> --graph_name <graph_column> --dataframe_column <dataframe_column>
```

Replace `<path_to_graph_file>` with the path to your graph file in GML format.  
Replace `<path_to_dataframe>` with the path to your dataframe file in TSV format.  
Replace `<graph_column>` with the name of the column in the graph that corresponds to the desired attribute.  
Replace `<dataframe_column>` with the name of the column in the dataframe that corresponds to the desired attribute.

The script will add the specified attribute to each node in the graph based on matching values between the graph and the dataframe.

## Output

The script will save the updated graph file with the added attributes. The output file will have a similar name to the input graph file, with "_updated" appended to it.

## License

This script is distributed under the terms of the Modified BSD License. See the `COPYING.txt` file included with this software for more information.

