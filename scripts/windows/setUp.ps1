# Retrieve the current user's username
$currentUsername = [System.Environment]::UserName

# Define the path for the new directory
$customBinPath = "C:\Program Files\filemanager"

# Check if the directory exists, if not, create it
if (-Not (Test-Path -Path $customBinPath)) {
    New-Item -Path $customBinPath -ItemType Directory
}

# Define the source path of the filemanager.exe using the current user's username
$fileManagerExePath = "C:\Users\$currentUsername\Downloads\filemanager.exe"

# Define the destination patha
$destinationPath = Join-Path -Path $customBinPath -ChildPath "filemanager.exe"

# Copy the executable to the new directory
Copy-Item -Path $fileManagerExePath -Destination $destinationPath -Force

# Retrieve the current PATH environment variable
$currentPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)

# Check if the custom directory is already in the PATH
if ($currentPath -notlike "*$customBinPath*") {
    # Add the custom directory to the PATH
    $newPath = "$currentPath;$customBinPath"
    [System.Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::Machine)
    Write-Host "Added $customBinPath to system PATH."
} else {
    Write-Host "$customBinPath is already in the system PATH."
}

Write-Host "Setup complete. You can now use 'filemanager' from any command line."
