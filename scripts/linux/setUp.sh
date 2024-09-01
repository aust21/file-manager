#!/bin/bash

# install nautilus
sudo apt-get install -y nautilus

# Copy the filemanager binary to ~/.local/bin
cp -r ~/Downloads/filemanager ~/.local/bin

# Make the filemanager binary executable
chmod +x ~/.local/bin/filemanager

# Copy the filemanager binary to /usr/local/bin with root permissions
sudo cp ~/Downloads/filemanager /usr/local/bin/filemanager

# Make the filemanager binary executable in /usr/local/bin
sudo chmod +x /usr/local/bin/filemanager

echo "filemanager setup complete."

filemanager
