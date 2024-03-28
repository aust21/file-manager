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

	def get_path(self, filename):
		return f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\{filename}"


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
			filename = "c++.txt"
			fl = open(self.get_path(filename), "w"); fl.close()
			res = rm.remove_file(True, self.get_path(filename), filename)
			output.assert_called_once_with("File deleted successfully.")


	@patch("text_operations.search_file.take_filename")
	@patch("text_operations.removeFile.search_path")
	def test_search_file_exist(self, mock_input, mock_path):
		mock_input.return_value = "I_love_Mr_Ballen.txt"
		mock_path.return_value = f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\"
		path = mock_path.return_value
		filename = mock_input.return_value
		fl = open(self.get_path(filename), "w"); fl.close()
		search_path = self.get_path(filename)
		self.assertEqual((True, self.get_path(filename)), sf.find_file(filename, path))
		os.remove(self.get_path(filename))


	@patch("text_operations.search_file.take_filename")
	def test_search_file_doesnt_exist(self, mock_input):
		mock_input.return_value = "myfile.txt"
		filename = mock_input.return_value
		self.assertTrue((False, None) == sf.find_file(filename, "C:\\3-28-2024T11:50.pdf"))



if __name__ == "__main__":
	unittest.main()