import os
from pathlib import Path

def organise_downloads(download_path):
    # dictionary to define folder names for each file type
    file_types_folders = {
        '.pdf': 'PDFs',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.txt': 'Text Files',
        '.docx': 'Documents',
        '.xlsx': 'Excel Files',
        '.mp4': 'Videos',
        '.mov': 'Videos',
        '.mp3': 'Audio',
        '.zip': 'Archives',
        '.tar.gz': 'Archives',
        '.rar': 'Archives'
    }

    # ensure the downloads directory exists
    if not os.path.exists(download_path):
        print(f"The path {download_path} does not exist.")
        return

    # visit each file in the download directory
    for file in os.listdir(download_path):
        file_path = Path(download_path) / file
        if file_path.is_file(): 
            file_extension = file_path.suffix.lower()  
            folder_name = file_types_folders.get(file_extension, 'Other')
            folder_path = Path(download_path) / folder_name
            folder_path.mkdir(exist_ok=True)  
            new_file_path = folder_path / file
            file_path.rename(new_file_path)  
            print(f"Moved {file_path} to {new_file_path}")

# change the path to your actual downloads directory
downloads_path = '/Users/your_user_name/Downloads'
organise_downloads(downloads_path)
