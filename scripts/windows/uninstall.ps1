# Define the path for the custom directory where filemanager.exe was installed
$customBinPath = "C:\Program Files\filemanager"

# Check if the directory exists
if (Test-Path -Path $customBinPath) {
    # Remove the filemanager.exe file
    Remove-Item -Path "$customBinPath\filemanager.exe" -Force
    Write-Host "Removed filemanager.exe from $customBinPath."

    # Remove the custom directory if it's empty
    Remove-Item -Path $customBinPath -Force -Recurse
    Write-Host "Removed $customBinPath directory."
} else {
    Write-Host "The directory $customBinPath does not exist."
}

# Retrieve the current PATH environment variable
$currentPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)

# Check if the custom directory is in the PATH
if ($currentPath -like "*$customBinPath*") {
    # Remove the custom directory from the PATH
    $newPath = $currentPath -replace ";?$customBinPath", ""
    [System.Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::Machine)
    Write-Host "Removed $customBinPath from system PATH."
} else {
    Write-Host "$customBinPath is not in the system PATH."
}

Write-Host "Uninstallation complete."
