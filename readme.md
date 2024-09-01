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

[Download Binary for Linux](https://github.com/aust21/file-manager/releases/download/v1.1.2-beta/filemanager)

[Download Binary for Windows](https://github.com/aust21/file-manager/releases/download/v1.1.2-beta/filemanager.exe)

### For Windows

in development :)

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

## Contributors

- Austin - kngobeni223@gmail.com
