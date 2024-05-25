import sys, os
import platform
sys.path.append(os.getcwd())
import text_operations.search_file as sf


def remove_file(can_remove, file_path, file_name) -> None:
	if can_remove:
		os.remove(file_path)
		return "File deleted successfully."
	return f"There no file named '{file_name}'"


def search_path() -> str:
	return "C:\\"


def main() -> None:
	file_name = sf.take_filename()
	search = search_path()
	can_remove, file_path = sf.find_file(file_name, search)
	print(remove_file(can_remove, file_path, file_name))


if __name__ == "__main__":
	main()
