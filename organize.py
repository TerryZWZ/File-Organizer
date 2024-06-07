import os
import shutil

def organize_files(dir) :

    # A dictionary to map file extensions to folder names
    file_type_folders = {
        'jpg': 'Images',
        'jpeg': 'Images',
        'png': 'Images',
        'bmp': 'Images',
        'tiff': 'Images',
        'webp': 'Images',
        'gif': 'GIFs',
        'pdf': 'PDFs',
        'docx': 'Documents',
        'doc': 'Documents',
        'txt': 'TextFiles',
        'rtf': 'TextFiles',
        'md': 'TextFiles',
        'csv': 'Spreadsheets',
        'xls': 'Spreadsheets',
        'xlsx': 'Spreadsheets',
        'ppt': 'PowerPoints',
        'pptx': 'PowerPoints',
        'exe': 'Executables',
        'bat': 'Executables',
        'sh': 'Executables',
        'mp3': 'Audio',
        'wav': 'Audio',
        'flac': 'Audio',
        'mp4': 'Videos',
        'avi': 'Videos',
        'mkv': 'Videos',
        'mov': 'Videos',
        'zip': 'Archives',
        'rar': 'Archives',
        '7z': 'Archives',
        'tar': 'Archives',
        'iso': 'DiskImages'
    }
    
    # Defining "other" folder for other file types
    other_folder = 'Other'

    # Creating folders
    for folder in set(file_type_folders.values()) :
        if not os.path.exists(os.path.join(dir, folder)) :
                os.mkdir(os.path.join(dir, folder))

    # Creating "other" folder
    if not os.path.exists(os.path.join(dir, other_folder)) :
         os.mkdir(os.path.join(dir, other_folder))

    # Moving files to respective folders
    for filename in os.listdir(dir) :
         if os.path.isfile(os.path.join(dir, filename)) :
              file_extension = filename.split('.')[-1].lower()
              folder_name = file_type_folders.get(file_extension, other_folder)
              shutil.move(os.path.join(dir, filename), os.path.join(dir, folder_name, filename))

    # Prompt user
    print("Files Organized")

# Prompt user for directory
user_directory = input("Enter the path of the directory to organize: ")

# Checking if directory exists
if os.path.exists(user_directory) and os.path.isdir(user_directory) :
    organize_files(user_directory)
else :
        print("Directory does not exist")
