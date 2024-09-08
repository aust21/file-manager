# File Manager

File Manager CLI Tool

## Overview

File Manager CLI Tool is a command line tool that provides useful file operations. While not a command tool (in development :), it offers operations like creating files, editing files, locating files and deleting files.

## Features

- Create new files
- Locate files
- Delete files
- Share files on the browser

## Usage

You can download the latest binary from the links:

[Download Binary for Linux](https://github.com/aust21/file-manager/releases/download/v1.1.3/filemanager)

[Download Binary for Windows](https://github.com/aust21/file-manager/releases/download/v1.1.2-beta/filemanager.exe)

### For Windows

[Download the set-up script](scripts/windows/setUp.ps1)

1. Open the Powershell
```bash
cd $HOME\Downloads
```
2. Run the Script
```bash
.\setUp.ps1
```

### For Linux

[Download the set-up script](scripts/linux/setUp.sh)

```bash
cd ~/Downloads
```

- Make the script executable

```bash
chmod +x setUp.sh
```

- Run the script to set up

```bash
./setUp.sh
```

### Troubleshooting Installation
- If you faced any issues with installing the program, visit the [wiki](https://github.com/aust21/file-manager/wiki/installation#troubleshooting) and see if the issue has been solved.
- If the issue can't be resolved, please open an issue.

### Commands
You can run the program with any of the commands

- To view commands

```bash
filemanager
```

- To search for a file

```bash
filemanager search filename
```

- To remove for a file

```bash
filemanager remove filename
```

- To share for a file

```bash
filemanager share filename
```

- To create a file

```bash
filemanager write filename
```

- To organise a folder

```bash
filemanager organise folder_name
```

## Documentation
- [Please visit the Wiki](https://github.com/aust21/file-manager/wiki/File-Manager-Wiki) to learn more about the project.

- [Please visit the release page](https://github.com/aust21/file-manager/releases/tag/v1.1.3) for a detailed description about this release.

## Screenshots

![main](assets/readmeImages/Screenshot%20from%202024-09-01%2017-28-11.png)

## Future Plans

In the future, I plan to:

- Add more features to automate file management

## Unistalling the program
For Linux
1. Remove the binary from /usr/local/bin:
```
sudo rm /usr/local/bin/filemanager
```

2. Remove the binary from ~/.local/bin:
```
rm ~/.local/bin/filemanager
```

For Windows
1. [Download](scripts/windows/uninstall-filemanager.ps1) the uninstall script
2. Open the powershell and locate the script
```bash
cd $Home\Downloads
```
3. Run the script
```bash
powershell -ExecutionPolicy Bypass -File .\uninstall-filemanager.ps1
```

## Contributors

- Austin - kngobeni223@gmail.com
