import unittest
import main
import text_operations
import text_operations.removeFile as rm
import text_operations.viewFile as vf
import text_operations.writeFile as wf
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

	@patch("text_operations.removeFile.take_filename")
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



if __name__ == "__main__":
	unittest.main()