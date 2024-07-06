import sys
import os
import argparse


sys.path.append(os.getcwd())

from modules import *
import text_operations.removeFile as removefile
import text_operations.search_file as search
import text_operations.viewFile as viewFile
import text_operations.writeFile as writeFile
import text_operations.shareFiles as shareFiles
import helpCommands

def main():
    parser = argparse.ArgumentParser(prog='filemanager', description="File Manager CLI")
    subparsers = parser.add_subparsers(title='commands', dest='command')
    
    # Remove file command
    parser_remove = subparsers.add_parser('remove', help='Remove a file')
    parser_remove.add_argument('file_name', help='Name of the file to remove')
    parser_remove.set_defaults(func=lambda args: removefile.main(args.file_name))
    
    # Search file command
    parser_search = subparsers.add_parser('search', help='Search for a file')
    parser_search.add_argument('file_name', help='Name of the file to search')
    parser_search.set_defaults(func=lambda args: search.main(args.file_name))
    
    # View file command
    parser_view = subparsers.add_parser('view', help='View a file')
    parser_view.add_argument('file_name', help='Name of the file to view')
    parser_view.set_defaults(func=lambda args: viewFile.main(args.file_name))
    
    # Write file command
    parser_write = subparsers.add_parser('write', help='Write to a file')
    parser_write.add_argument('file_name', help='Name of the file to write')
    parser_write.set_defaults(func=lambda args: writeFile.main(args.file_name))

    # Share file command
    parser_share = subparsers.add_parser('share', help='Share a file')
    parser_share.add_argument('file_name', help='Name of the file to share')
    parser_share.set_defaults(func=lambda args: shareFiles.main(args.file_name))


    # Help file command
    parser_help = subparsers.add_parser('help', help='Show help')
    parser_help.set_defaults(func=helpCommands.entry())
    
    # Parse arguments
    args = parser.parse_args()
    
    if args.command:
        args.func(args)
    else:
        helpCommands.entry()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass
