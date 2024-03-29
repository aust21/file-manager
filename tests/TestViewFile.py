import unittest
import main
import text_operations
import text_operations.removeFile as rm
import text_operations.viewFile as vf
import text_operations.writeFile as wf
import text_operations.search_file as sf
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

	def test_view_file_exists(self):		
		output = vf.show_file_contents(True, self.file_path)
		self.assertEqual("""If you are fan of the strange dark and mysterious delivered in story format, take
the like button skydiving but give it a faulty parachute....""", output)