import text_operations.search_file as sf


def show_file_contents(file_exists, file_path):
	pass


if __name__ == "__main__":
	file_name = sf.take_filename()
	file_exists, file_path = sf.find_file(file_name, "C:\\") 
	show_file_contents(file_exists, file_path)
