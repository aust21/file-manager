import unittest
import text_operations
import text_operations.removeFile as rf
import os
from io import StringIO

from unittest.mock import patch

class TestRemove(unittest.TestCase):

    def setUp(self):
        try:
            os.mkdir("C:\\Users\\Austin\\Desktop\\testFileProgram")
        except FileExistsError:
            pass


    @patch("builtins.input", side_effect=["python.java"])
    def test_file_doesnt_exist(self, mock_input):
        with patch("text_operations.removeFile.search_path") as path:
            path.return_value = "C:\\Users\\Austin\\Desktop\\testFileProgram\\"
            with patch('sys.stdout', new=StringIO()), patch('sys.stderr', new=StringIO()):
                actual = rf.remove_file(False, path, "python.java")
                self.assertEqual(actual, f"There no file named 'python.java'")


if __name__ == "__main__":
    unittest.main()
