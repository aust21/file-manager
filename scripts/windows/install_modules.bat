@echo off
set packages=rich fpdf tqdm

for %%p in (%packages%) do (
    echo Installing %%p...
    pip install %%p
)

echo All packages installed successfully.
pause
