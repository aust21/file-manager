import sys, os
sys.path.append(os.getcwd())
import text_operations.search_file as sf


def remove_file(can_remove, file_path, file_name) -> None:
	if can_remove:
		sf.open_files(file_path)
		is_file = input("Wait for the pop us window to open and confirm this is the file [y or n]: ").lower()
		if is_file == "y" or is_file == "yes":
			os.remove(file_path)
			return "File deleted successfully."
		else:
			return "Please try to locate the file manually and delete it"
	return f"There no file named '{file_name}'"



def main(file_name) -> None:
	# file_name = sf.take_filename()
	search = sf.sys_path()
	can_remove, file_path = sf.find_file(file_name, search)
	print(remove_file(can_remove, file_path, file_name))