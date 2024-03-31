import unittest
from unittest.mock import patch
import text_operations
import text_operations.writeFile as wf
import os
import pypdf
from pypdf import PdfWriter


class TestWrite(unittest.TestCase):

	def setUp(self):
		self.invalid_file_name = "code.austin"
		self.valid_file_name_inv_prefix = "invaustin.pdf"
		self.valid_file_name = "austin.pdf"
		self.content = "I'm a fan of the strange, dark and mysterious delivered in story format...."
		self.file_path = f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager"
		self.file_path_inv = f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager\\inv"
		self.file_path_st = f"C:\\Users\\{os.getenv('USERNAME')}\\Documents\\FileManager\\stock-taking"
		self.writer = PdfWriter()
		self.page1 = self.writer.add_blank_page(width=8.27 * 72, height=11.7 * 72)
		self.writer.write(f"{self.file_path_inv}\\{self.valid_file_name}")


	def test_file_manager_exists(self):
		self.assertTrue(os.path.exists(self.file_path))


	@unittest.skip("tested")
	@patch("builtins.print")
	def test_invalid_file_exension(self, mock_print):
		actual = wf.write_to_file(False)
		mock_print.assert_called_once_with("Invalid file name.")


	@patch("builtins.print")
	def test_valid_file_extension_inv_prefix(self, mock_print):
		actual = wf.write_to_file(True, True, self.content)
		content = "Hello, this is page 1"
		# self.page1.drawText(100, 700, content)
		self.writer.write(self.content)
		# new_page.write(self.content)
		# mock_print.assert_called_once_with("New page added")



if __name__ == "__main__":
	unittest.main()