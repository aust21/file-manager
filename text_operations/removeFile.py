import sys, os
sys.path.append(os.getcwd())
import text_operations.search_file as sf
import search_file as sf


def remove_file(can_remove, file_path, file_name) -> None:
	if can_remove:
		os.remove(file_path)
		return "File deleted successfully."
	return f"There no file named '{file_name}'"



def main() -> None:
	file_name = sf.take_filename()
	search = sf.sys_path()
	can_remove, file_path = sf.find_file(file_name, search)
	print(remove_file(can_remove, file_path, file_name))


if __name__ == "__main__":
	main()
