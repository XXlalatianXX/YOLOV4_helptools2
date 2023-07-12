import os

folder_path = "E:/Python/Augmentation1"

file_list = os.listdir(folder_path)
file_list.sort()  # Sort the file list in ascending order

for file_name in file_list:
    if file_name.endswith(".py"):
        file_path = os.path.join(folder_path, file_name)
        print(f"Running file: {file_name}")
        exit_code = os.system(f"python {file_path}")
        if exit_code != 0:
            print(f"Error running file: {file_name}")
            break
exit()