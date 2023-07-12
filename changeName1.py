import os
import shutil

dataset_folder = "E:/Dataset"
output_folder = "E:/Dataset1"
print("hello")

os.makedirs(output_folder, exist_ok=True)

def get_next_name(current_name):
    print("hello")
    if not current_name:
        return "A"

    name = list(current_name)
    for i in range(len(name)-1, -1, -1):
        if name[i] != "Z":
            name[i] = chr(ord(name[i]) + 1)
            return "".join(name)
        else:
            name[i] = "A"

    return "".join(name) + "A"

image_files = [f for f in os.listdir(dataset_folder) if f.endswith('.jpg')]

image_files.sort()

current_name = None

for i, image_file in enumerate(image_files, start=1):
    print("hello")
    image_path = os.path.join(dataset_folder, image_file)
    annotation_file = os.path.splitext(image_file)[0] + ".txt"
    annotation_path = os.path.join(dataset_folder, annotation_file)

    # Get the next name in the sequence
    current_name = get_next_name(current_name)

    new_image_name = f"{current_name}.jpg"
    new_annotation_name = f"{current_name}.txt"

    new_image_path = os.path.join(output_folder, new_image_name)
    new_annotation_path = os.path.join(output_folder, new_annotation_name)

    shutil.move(image_path, new_image_path)
    shutil.move(annotation_path, new_annotation_path)

    print(f"Moved {i}: {image_file} -> {new_image_name}")
    print(f"Moved {i}: {annotation_file} -> {new_annotation_name}")