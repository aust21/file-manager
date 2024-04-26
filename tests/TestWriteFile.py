import unittest
from unittest.mock import patch
import text_operations
import text_operations.writeFile as wf
import os
from fpdf import FPDF

class TestWrite(unittest.TestCase):

	def setUp(self):
		self.invalid_file_name = "java.py"
		self.valid_file_name_inv_prefix = "invaustin.pdf"
		self.valid_file_name = "austin.pdf"
		self.txt_file = "austin.txt"
		self.content = "I'm a fan of the strange, dark and mysterious delivered in story format...."
		self.file_path = f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager"
		self.file_path_inv = f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager\\inv"
		try:
			os.mkdir(self.file_path_inv)
		except FileExistsError:
			pass

	# @unittest.skip("Tested")
	def test_file_manager_exists(self):
		self.assertTrue(os.path.exists(self.file_path))


	@patch("builtins.input", side_effect = ["I'm a fan of the strange, dark and mysterious delivered in story format....\n\n", ""])
	@patch("builtins.print")
	def test_valid_file_extension_inv_prefix(self, mock_print, mock_input):
		create_txt = wf.create_txt_read_file(self.txt_file, "txt", self.file_path_inv)
		actual = wf.write_to_file(self.valid_file_name, self.content, self.file_path_inv)
		self.assertEqual("File created.", actual)
		self.assertTrue(os.path.exists(f"{self.file_path_inv}\\{self.txt_file}"))
		os.remove(f"{self.file_path_inv}\\{self.txt_file}")
		self.assertFalse(os.path.exists(f"{self.file_path_inv}\\{self.txt_file}"))


if __name__ == "__main__":
	unittest.main()
