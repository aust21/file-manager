import sys, os
sys.path.append(os.getcwd())
import text_operations.search_file as sf


def show_file_contents(file_exists, file_path):
	if file_exists:
		with open(file_path, "r") as fl:
			content = fl.readlines()
			print("".join(content))
	else:
		print("Cannot open the file, make sure it exists.")


if __name__ == "__main__":
	file_name = sf.take_filename()
	file_exists, file_path = sf.find_file(file_name, "C:\\") 
	show_file_contents(file_exists, file_path)
