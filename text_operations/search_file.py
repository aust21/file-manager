import sys, os
from halo import Halo

def take_filename():
	extensions = [".pdf", ".txt"]
	file_name = input("Enter file name (filename must have file extension): ")
	if file_name.endswith(".pdf") or file_name.endswith(".txt"):
		return file_name
	print("File name should end with `.pdf` or `.txt`")


@Halo(text="This may take a while...Super highly advanced virtual bots are searching for your file :)")
def find_file(file_name, search_path):
	for root, dirs, files in os.walk(search_path):
		if file_name in files:
			return True, os.path.join(root, file_name)
	return False, None

if __name__ == "__main__":
	file_name = take_filename
	file_path = find_file(file_name, "C:\\")
