import sys, os
sys.path.append(os.getcwd())
import operations.search_file as sf


def remove_file(can_remove, file_path, file_name) -> None:
	if can_remove:
		sf.pop_up("File found, file location pop up will open.", "File Manager | Remove File")
		sf.open_files(file_path)
		is_file = input("Wait for the pop us window to open and confirm this is the file [y or n]: ").lower()
		if is_file == "y" or is_file == "yes":
			os.remove(file_path)
			return "File deleted successfully."
		else:
			return "Please try to locate the file manually and delete it"
	sf.pop_up("File not found, That's all we know.", "File Manager | Remove File")
	return f"There no file named '{file_name}'"



def main(file_name) -> None:
	search = sf.sys_path()
	can_remove, file_path = sf.find_file(file_name, search)
	print(remove_file(can_remove, file_path, file_name))