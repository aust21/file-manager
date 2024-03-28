import sys, os

def take_filename():
	return input("Enter file name (filename must have file extension): ")

def find_file(file_name, search_path):
	for root, dirs, files in os.walk(search_path):
		if file_name in files:
			return True, os.path.join(root, file_name)
	return False, None


def remove_file(can_remove, file_path, file_name):
	if can_remove:
		os.remove(file_path)
		print("File deleted successfully.")
	else:
		print(f"There no file named '{file_name}'")
	

if __name__ == "__main__":
	file_name = take_filename()
	can_remove, file_path = find_file(file_name, "C:\\")
	print(remove_file(can_remove, file_path, file_name))