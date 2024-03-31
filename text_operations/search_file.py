import sys, os
from halo import Halo

def take_filename():
	return input("Enter file name (filename must have file extension): ")
	

@Halo(text="This may take a while...Super highly advanced virtual bots are searching for your file :)")
def find_file(file_name, search_path):
	for root, dirs, files in os.walk(search_path):
		if file_name in files:
			return True, os.path.join(root, file_name)
	return False, None
