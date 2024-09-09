import sys, os, shutil
sys.path.append(os.getcwd())
from modules import *
import operations.search_file as sf
from pathlib import Path

PATH = sf.sys_path()

def get_organise_path(directory_) -> str:
    for root, dirs, files in tqdm(os.walk(PATH), desc="Searching"):
        if directory_ in dirs:
            sf.open_files(os.path.join(root, directory_))
            answer = input("Confirm this is the correct directory [yes or no]: ")
            if answer.lower() == "yes":
                return True, os.path.join(root, directory_)
            continue
    return False, ""

def create_dir(directory_to_organise) -> None:
    os.chdir(directory_to_organise)
    for item in os.listdir():
        if item.startswith(".") or item == "FileManager":
            continue
        
        # this moves files, not directories
        if os.path.isfile(item):
            # Check for documents
            if item.endswith(".txt") or item.endswith(".pdf"):
                Path("documents").mkdir(exist_ok=True)
                shutil.move(item, "documents")

            # Check for images
            elif item.endswith(".PNG") or item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg"):
                Path("images").mkdir(exist_ok=True)
                shutil.move(item, "images")

            # Check for compressed files
            elif item.endswith(".zip") or item.endswith(".rar") or item.endswith(".gz"):
                Path("compressed files").mkdir(exist_ok=True)
                shutil.move(item, "compressed files")

            # Check for audio files
            elif item.endswith(".mp3") or item.endswith("mp4a"):
                Path("audio files").mkdir(exist_ok=True)
                shutil.move(item, "audio files")

            # Check for video files
            elif item.endswith(".mp4") or item.endswith(".mkv") or item.endswith(".gif"):
                Path("video files").mkdir(exist_ok=True)
                shutil.move(item, "video files")

            # Move everything else to 'other files'
            else:
                Path("other files").mkdir(exist_ok=True)
                shutil.move(item, "other files")
        else:
            # Ignore directories, do not move them
            print(f"Skipping directory: {item}")


def main(folder_dir):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    if folder_dir.lower() == "home" or folder_dir.startswith("."):
        print("Organising such files could cause unexpected events on your computer")
        return
    folder_found = get_organise_path(folder_dir)
    if folder_found[0]:
        path_to_organise = folder_found[1]
        create_dir(path_to_organise)
    else:
        print(f"Folder {folder_dir} not found.")

if __name__ == "__main__":
    main("Downloads")