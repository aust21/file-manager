import unittest
import main
import text_operations
import text_operations.removeFile as rm
import text_operations.viewFile as vf
import text_operations.writeFile as wf
import text_operations.search_file as sf
import os
from unittest.mock import patch

class TestMainCase(unittest.TestCase):

	def setUp(self):
		self.file_name = "MrBallen_Presents-The_Strange_Dark_Mysterious.txt"
		self.file_path = f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\{self.file_name}"
		with open(self.file_path, "w") as fl:
			fl.write("If you are fan of the strange dark and mysterious delivered in story format,\n"
			"tell the like button you're taking it on a vacation oversees but ship it off to space instead...")


	def test_commands(self):
		self.assertEqual("""Command                       Action
-------------------------------------------------------------------
-> open <filename>                  opens file
-> create <filename>                creates and write to a new file
-> read <filename>                  reads out file contents
-------------------------------------------------------------------
-------------------------------------------------------------------""", main.commands())

	@patch("text_operations.search_file.take_filename")
	def test_delete_file_doesnt_exist(self, mock_input):
		with patch("builtins.print") as output:
			mock_input.return_value = "myfile.txt"
			file_name = mock_input.return_value
			res = rm.remove_file(False, None, file_name)
			output.assert_called_once_with(f"There no file named '{file_name}'")


	def test_delete_file_success(self):
		with patch("builtins.print") as output:
			res = rm.remove_file(True, self.file_path, self.file_name)
			output.assert_called_once_with("File deleted successfully.")


	@patch("text_operations.search_file.take_filename")
	@patch("text_operations.removeFile.search_path")
	def test_search_file_exist(self, mock_input, mock_path):
		mock_input.return_value = "I_love_Mr_Ballen.txt"
		mock_path.return_value = f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\"
		path = mock_path.return_value
		filename = mock_input.return_value
		search_path = self.file_path
		self.assertEqual((True, self.file_path), sf.find_file(self.file_name, path))


	@patch("text_operations.search_file.take_filename")
	def test_search_file_doesnt_exist(self, mock_input):
		mock_input.return_value = "myfile.txt"
		filename = mock_input.return_value
		self.assertTrue((False, None) == sf.find_file(filename, "C:\\3-28-2024T11:50.pdf"))


if __name__ == "__main__":
	unittest.main()
