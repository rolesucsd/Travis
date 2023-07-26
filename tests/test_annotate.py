import unittest
import os
from annotate import annotate

class TestAnnotateScript(unittest.TestCase):
    def test_missing_files(self):
        # Test when input files are missing
        with self.assertRaises(SystemExit) as cm:
            annotate("missing_graph.gml", "missing_dataframe.txt", "graph_name", "dataframe_column")
        self.assertEqual(cm.exception.code, 1)

    def test_invalid_files(self):
        # Test when input files are invalid
        with open("invalid_graph.gml", "w") as f:
            f.write("Invalid GML content")
        with open("invalid_dataframe.txt", "w") as f:
            f.write("Invalid dataframe content")
        with self.assertRaises(SystemExit) as cm:
            annotate("invalid_graph.gml", "invalid_dataframe.txt", "graph_name", "dataframe_column")
        self.assertEqual(cm.exception.code, 1)

    def test_valid_files(self):
        # Test when input files are valid
        with open("valid_graph.gml", "w") as f:
            f.write("Valid GML content")
        with open("valid_dataframe.txt", "w") as f:
            f.write("Valid dataframe content")
        result = annotate("valid_graph.gml", "valid_dataframe.txt", "graph_name", "dataframe_column")
        # Add assertions to check the expected behavior

        # Clean up temporary files after testing
        os.remove("valid_graph.gml")
        os.remove("valid_dataframe.txt")

if __name__ == '__main__':
    unittest.main()
