import os
import shutil

def copy_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get the list of files in the source folder
    file_list = os.listdir(source_folder)

    # Iterate over each file in the source folder
    for file_name in file_list:
        # Construct the source and destination file paths
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)

        # Copy the file to the destination folder
        shutil.copyfile(source_file, destination_file)

# Specify the source and destination folder paths
source_folder = "F:/data1"
destination_folder = "F:/data1"

# Copy files from the source folder to the destination folder
copy_files(source_folder, destination_folder)
