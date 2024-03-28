import operations.voice_input as vc


def remove_file(file_name):
	pass



if __name__ == "__main__":
	engine = vc.speech_engine()
	text = vc.get_command(engine)
	file_name = vc.retrive_filename(text)
	remove_file(file_name)