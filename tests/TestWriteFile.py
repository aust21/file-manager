import unittest
from unittest.mock import patch
import text_operations
import text_operations.writeFile as wf
import os
from fpdf import FPDF

class TestWrite(unittest.TestCase):

	def setUp(self):
		self.invalid_file_name = "py.java"
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
		# with open(f"{self.file_path_inv}\\content.txt", "rb") as fl:
		# 	self.txt = fl.read().decode("latin-1")

	@unittest.skip("Tested")
	def test_file_manager_exists(self):
		self.assertTrue(os.path.exists(self.file_path))


	@unittest.skip("Tested")
	@patch("builtins.print")
	def test_invalid_file_exension(self, mock_print):
		actual = wf.write_to_file(False, None, self.file_path)
		mock_print.assert_called_once_with("Invalid file name.")



	@patch("builtins.input", side_effect = ["I'm a fan of the strange, dark and mysterious delivered in story format....\n", ""])
	@patch("builtins.print")
	def test_valid_file_extension_inv_prefix(self, mock_print, mock_input):
		create_txt = wf.create_txt_read_file(self.txt_file, "txt", self.file_path_inv)
		actual = wf.write_to_file(True, self.content, self.file_path_inv)
		mock_print.assert_called_once_with("File created.")
		self.assertTrue(os.path.exists(f"{self.file_path_inv}\\{self.txt_file}"))
		os.remove(f"{self.file_path_inv}\\{self.txt_file}")
		self.assertFalse(os.path.exists(f"{self.file_path_inv}\\{self.txt_file}"))


if __name__ == "__main__":
	unittest.main()
