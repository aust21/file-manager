import unittest
import main
import operations
import operations.removeFile as rm
import operations.viewFile as vf
import operations.writeFile as wf
import operations.voice_input as vi
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


	def test_delete_file_doesnt_exist(self):
		with patch("builtins.print") as output:
			res = rm.remove_file("delete myfile pdf")
			output.assert_called_once_with("There no file named 'myfile.pdf'")


	def test_delete_file_success(self):
		with patch("builtins.print") as output:
			res = rm.remove_file("delete data structures and algorithms text")
			output.assert_called_once_with("File deleted successfully.")


	@patch("operations.voice_input.get_command")
	def test_voice_to_text(self, text):
		text.return_value = "open myfile txt"
		output = text.return_value
		actual_output = construct_command(output)
		self.assertEqual("open myfile.txt", actual_output)


if __name__ == "__main__":
	unittest.main()