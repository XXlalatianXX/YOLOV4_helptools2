import os

dataset_folder = "E:/All"

def remove_files_with_copy_pattern(folder_path):
    for filename in os.listdir(folder_path):
        if "- Copy" in filename:
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

remove_files_with_copy_pattern(dataset_folder)