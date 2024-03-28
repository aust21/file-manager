import unittest
import main
import text_operations
import text_operations.removeFile as rm
import text_operations.viewFile as vf
import text_operations.writeFile as wf
import text_operations.search_file as sf
import os
# import platform

from unittest.mock import patch

class TestMainCase(unittest.TestCase):
	def test_commands(self):
		self.assertEqual("""Voice Command                       Action
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
			res = rm.remove_file("delete data structures and algorithms text")
			output.assert_called_once_with("File deleted successfully.")


	@patch("text_operations.search_file.take_filename")
	@patch("text_operations.removeFile.search_path")
	def test_search_file_doesnt_exist(self, mock_input, mock_path):
		mock_input.return_value = "myfile.txt"
		mock_path.return_value = f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\"
		path = mock_path.return_value
		filename = mock_input.return_value
		fl = open(f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\{filename}", "w")
		fl.close()
		search_path = f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\{filename}"
		self.assertEqual((True, f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\{filename}"), sf.find_file(filename, path))
		os.remove(f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\{filename}")



if __name__ == "__main__":
	unittest.main()