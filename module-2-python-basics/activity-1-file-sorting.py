"""
Module 2 — Activity: File Sorting with os and shutil
Student: Bondoc, Julien Mark
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I have developed an automated Python code which
will clean up a dirty target folder by sorting
out the files in this folder according to the
types of the file extensions. The code scans
through all the files in the folder, recognizes
the type of the file (for example, jpg, pdf, mp3, docx),
creates a new subfolder for each file type
(if there is none created before), and moves
the file into this subfolder.
============================================
KEY VOCABULARY
============================================
- os module: A built-in Python module which contains
functions to interact with the operating system by
reading folders or verifying paths' existence.

- shutil module: The abbreviation for "shell utilities"
that is a built-in library to work with files on a higher
level including copy, move, or delete operations.

- file path: The string that specifies the location of
the file/folder in your computer system directory structure
(e.g., C:/Users/Julien/Downloads/file.pdf).

- directory: The official name of the folder where
files are stored.

- file extension: The part at the end of a filename
that indicates its type (.py, .png).
============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

target_folder = r"C:\Users\Julien\Downloads"
os.chdir(target_folder)
for item in os.listdir(target_folder):
    if os.path.isfile(item):
        filename, extension = os.path.splitext(item)
        folder_name = extension[1:].upper()
        if not folder_name:
            folder_name = "OTHERS"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        shutil.move(item, os.path.join(folder_name, item))
        print(f"Moved: {item} -> {folder_name}/")
print("File sorting complete!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Moving files to directories that don't exist
or working with subdirectories.

One major problem in writing file sorters
is not checking whether the item is a file
using the os.path.isfile(). When you try to
use the os.splitext() method on a directory
and move it into itself, the script gives an
error. The other one is moving the file
without making sure that the destination
path exists, thereby giving you an incorrect
file name and moving it in.

How to avoid it: Always ensure the item is
a file and make sure that the destination
path exists before moving the file.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
