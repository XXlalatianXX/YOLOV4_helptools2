import os
import shutil

source_folder = "E:/All"
target_folder = "E:/Data"

os.makedirs(target_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith(".JPG"):
        new_filename = filename[:-4] + ".jpg"
        shutil.move(os.path.join(source_folder, filename), os.path.join(target_folder, new_filename))
        print(f"Moved and renamed: {filename} -> {os.path.join(target_folder, new_filename)}")
    elif filename.endswith(".TXT"):
        new_filename = filename[:-4] + ".txt"
        shutil.move(os.path.join(source_folder, filename), os.path.join(target_folder, new_filename))
        print(f"Moved and renamed: {filename} -> {os.path.join(target_folder, new_filename)}")