# organize_file_types_script

## Description
This script will organize files in a directory of your choice by file type, reading its extension.

The files will be COPIED, not moved, to preserve the originals in case of any errors. You 
can manually delete the original files afterward.

This script will not copy directories, because of the potential size increase and subdirectories implied.
Size might scale very quickly working with folders and sub-folders.

## How To Use
(Follow steps One and Two only for options Number One and Number Two down below)
1. Download python in your computer from: https://www.python.org/downloads/
2. Make sure you install the following dependency: `pip install shutil`
3. Download this repository as a .zip file for your convenience, or clone it if you prefer it.
4. Extract the files from the .zip file.
5. At this point you have 3 options:
   1. ***Number One*** (**run the script with Python**):
      1. Extract the `script.py` file into the folder you want to organize
      2. Execute the script from the command line by opening a terminal in the folder you want to organize
      3. Type `python script.py` and press enter to run the program
      4. Run it and follow the instructions
   2. ***Number Two*** (**create a standalone executable file from the script with `pyinstaller`**):
      1. Install pyinstaller by typing `pip install pyinstaller` in the command line. Make sure you have installed python
          previously, otherwise, you can't install pyinstaller
      2. Add pyinstaller to your environment variables.
      3. Extract the `script.py` file into any folder
      4. Open a terminal in the folder where you extracted the `script.py` file
      5. Type `pyinstaller --onefile script.py` and press enter to run the program and create an executable file from 
      the script itself
      6. Move the `script.exe` file to the folder you want to organize
      7. Run it and follow the instructions
   3. ***Number Three*** (**run the included executable file**):
      1. I advise against this option unless you trust the creator of the repository (including this one)
      2. Download the `script.exe` file from the repository
      3. Place the exe file in the folder you want to organize
      4. Run it and follow the instructions

## Security Warning!
As mentioned in the `Number Three` option, don't download or run any .exe files from a repository you don't fully trust,
since you might get a virus infection or bigger problems by doing so.

With that said, feel free to check the code in the `script.py` file to make sure it's safe to run and analyze 
the included .exe, since it's a direct build from that script using the method mentioned in option `Number Two`

## Disclaimer
I am not responsible for any damage o data loss you might suffer, since this script is provided as-is, without any
hidden alterations the user might not be aware of.

The source code is open for anyone to check and analyze, so feel free to do so.

I have tested this process in my personal computer and no data loss was suffered, specifically because the handled 
files are not being moved, but copied.

Security-wise, I provided every possible warning discouraging the user from running executable files from this and
any repository they don't fully trust, so damages caused by this action are not under my responsibility.

The user is fully allowed and encouraged to download only the script.py file first to analyze it, since it does 
not pose any threat the user by itself.

## Wrap-Up
Thank you for checking out this small but useful script! I hope you find it useful as well.

If you have any questions, suggestions or comments, feel free to contact me at:
- Email: `nacho.ponce25@gmail.com`
- Telegram: `@tommyHellraiser`