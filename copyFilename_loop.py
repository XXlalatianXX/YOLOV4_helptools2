import os
import shutil

dataset_folder = "E:/All"
output_folder = "E:/Data"

# Define the number of loops and the suffixes
num_loops = 8
suffixes = [1,2,3,4,5,6,7,8]

os.makedirs(output_folder, exist_ok=True)

image_files = [
    f for f in os.listdir(dataset_folder) if f.lower().endswith('.jpg')
]

image_files.sort()

for suffix in suffixes:
    for i, image_file in enumerate(image_files, start=1):
        image_path = os.path.join(dataset_folder, image_file)
        annotation_file = os.path.splitext(image_file)[0] + ".txt"
        annotation_path = os.path.join(dataset_folder, annotation_file)

        # Get the base filename without extension
        base_name = os.path.splitext(image_file)[0]

        # Append the suffix to the base filename
        new_base_name = f"{base_name}_{suffix}"

        new_image_name = f"{new_base_name}.jpg"
        new_annotation_name = f"{new_base_name}.txt"

        new_image_path = os.path.join(output_folder, new_image_name)
        new_annotation_path = os.path.join(output_folder, new_annotation_name)

        shutil.copy(image_path, new_image_path)
        shutil.copy(annotation_path, new_annotation_path)

        print(f"Copied {i}: {image_file} -> {new_image_name}")
        print(f"Copied {i}: {annotation_file} -> {new_annotation_name}")

    print(f"Completed Loop {suffix}")

print("Dataset Copying Completed")