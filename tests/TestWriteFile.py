import unittest
from unittest.mock import patch
import text_operations
import text_operations.writeFile as wf
import os
from fpdf import FPDF

class TestWrite(unittest.TestCase):

	def setUp(self):
		self.invalid_file_name = "code.austin"
		self.valid_file_name_inv_prefix = "invaustin.pdf"
		self.valid_file_name = "austin.pdf"
		self.hidden_file_name = ".austin.txt"
		self.content = "I'm a fan of the strange, dark and mysterious delivered in story format...."
		self.file_path = f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager"
		self.file_path_inv = f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager\\inv"
		self.hidden_file_dir = f"{self.file_path_inv}\\.austin.txt"
		self.file_path_st = f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager\\stock-taking"
		try:
			os.mkdir(self.file_path_inv)
		except FileExistsError:
			pass
		with open(f"{self.file_path_inv}\\content.txt", "rb") as fl:
			self.txt = fl.read().decode("latin-1")


	def test_file_manager_exists(self):
		self.assertTrue(os.path.exists(self.file_path))


	@unittest.skip("tested")
	@patch("builtins.print")
	def test_invalid_file_exension(self, mock_print):
		actual = wf.write_to_file(False)
		mock_print.assert_called_once_with("Invalid file name.")


	@patch("builtins.print")
	def test_valid_file_extension_inv_prefix(self, mock_print):
		create_txt = wf.create_txt_read_file(self.hidden_file_name, "txt)
		actual = wf.write_to_file(True, True, self.hidden_file_dir)
		self.assertTrue(os.path.exists(f"{self.file_path_inv}\\{self.valid_file_name}"))
		os.remove(self.hidden_file_dir)
		assertFalse(os.path.exists(self.hidden_file_dir))
		mock_print.assert_called_once_with("File created.")


if __name__ == "__main__":
	unittest.main()
