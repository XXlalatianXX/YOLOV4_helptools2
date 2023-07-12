import os
import shutil

dataset_folder = "C:/darknet_use/data/obj"
output_folder = "C:/darknet_use/data/obj1"

os.makedirs(output_folder, exist_ok=True)

image_files = [f for f in os.listdir(dataset_folder) if f.endswith('.jpg')]

image_files.sort()

for i, image_file in enumerate(image_files, start=1):
    image_path = os.path.join(dataset_folder, image_file)
    annotation_file = os.path.splitext(image_file)[0] + ".txt"
    annotation_path = os.path.join(dataset_folder, annotation_file)

    # Get the base filename without extension
    base_name = os.path.splitext(image_file)[0]

    # Find the last occurrence of " - Copy" in the base filename
    last_copy_index = base_name.rfind(" - Copy")

    # Remove the extra copies from the base filename
    new_base_name = base_name[:last_copy_index] if last_copy_index != -1 else base_name

    new_image_name = f"{i}.jpg"
    new_annotation_name = f"{i}.txt"

    new_image_path = os.path.join(output_folder, new_image_name)
    new_annotation_path = os.path.join(output_folder, new_annotation_name)

    shutil.move(image_path, new_image_path)
    shutil.move(annotation_path, new_annotation_path)

    print(f"Moved {i}: {image_file} -> {new_image_name}")
    print(f"Moved {i}: {annotation_file} -> {new_annotation_name}")