import unittest
import text_operations.viewFile as vf
import os

from unittest.mock import patch

class TestViewClass(unittest.TestCase):
	def setUp(self):
		self.file_name = "MrBallen_Presents-The_Strange_Dark_Mysterious.txt"
		self.file_path = f"C:\\Users\\{os.getenv('USERNAME')}\\Desktop\\{self.file_name}"
		with open(self.file_path, "w") as fl:
			fl.write("If you are fan of the strange dark and mysterious delivered in story format, take\n"
			"the like button skydiving but give it a faulty parachute....")
		
	def tearDown(self):
		os.remove(self.file_path)


	@patch("builtins.print")
	def test_view_file_exists(self, mock_print):		
		output = vf.show_file_contents(True, self.file_path)
		mock_print.assert_called_once_with("""If you are fan of the strange dark and mysterious delivered in story format, take
the like button skydiving but give it a faulty parachute....""")


	@patch("builtins.print")
	def test_view_file_doesnt_exist(self, mock_print):
		output = vf.show_file_contents(False, self.file_path + "e")
		mock_print.assert_called_once_with("Cannot open the file, make sure it exists.")



if __name__ == "__main__":
	unittest.main()