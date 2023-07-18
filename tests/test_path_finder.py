import unittest
import os
from path_finder import uploadGraph


class TestPathFinder(unittest.TestCase):

    def test_uploadGraph(self):
        graph_file = 'path/to/graph.gml'
        start_gene = 'start_gene'
        stop_gene = 'stop_gene'
        output_folder = 'path/to/output_folder'

        # Call the function being tested
        uploadGraph(graph_file, start_gene, stop_gene, output_folder)

        # Assert that the expected output files are created
        expected_files = [
            f"{start_gene}_path_full.csv",
            f"{start_gene}_path.csv",
            f"{start_gene}_graph.gml",
            f"{start_gene}_member.csv"
        ]
        for file in expected_files:
            expected_path = os.path.join(output_folder, file)
            self.assertTrue(os.path.exists(expected_path),
                            f"Expected file {file} not found in the output folder.")

    def test_uploadGraph_case2(self):
        graph_file = 'path/to/graph.gml'
        start_gene = 'gene1'
        stop_gene = 'gene2'
        output_folder = 'path/to/output_folder'

        # Call the function being tested
        uploadGraph(graph_file, start_gene, stop_gene, output_folder)

        # Assert that the expected output files are created
        expected_files = [
            f"{start_gene}_path_full.csv",
            f"{start_gene}_path.csv",
            f"{start_gene}_graph.gml",
            f"{start_gene}_member.csv"
        ]
        for file in expected_files:
            expected_path = os.path.join(output_folder, file)
            self.assertTrue(os.path.exists(expected_path),
                            f"Expected file {file} not found in the output folder.")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()