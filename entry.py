import sys, os
sys.path.append(os.getcwd())


import text_operations.removeFile as removefile
import text_operations.search_file as search
import text_operations.viewFile as viewFile
import text_operations.writeFile as writeFile

def main():
    if len(sys.argv) < 2:
        print("Usage: cli.py <command> [args]")
        sys.exit(1)

    command = sys.argv[1]
    file_name = sys.argv[2]

    if command == "removefile":
        removefile.main()
    elif command == "search":
        search.main(file_name)
    elif command == "viewFile":
        viewFile.main()
    elif command == "writeFile":
        writeFile.main()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except:
        print("File manager closed.")
