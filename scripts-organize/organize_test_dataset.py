import os
import json
import shutil

def load_class_mappings(annotations_file_path):
    with open(annotations_file_path, 'r') as f:
        annotations = json.load(f)
    class_mappings = {category['id']: category['name'] for category in annotations['categories']}
    return class_mappings

def load_test_annotations(annotations_file_path):
    with open(annotations_file_path, 'r') as f:
        annotations = json.load(f)
    return annotations

def organize_test_images(annotations, src_folder, dest_folder, class_mappings):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for image_info in annotations['images']:
        image_id = image_info['id']
        file_name = image_info['file_name']
        
        class_id = next((ann['category_id'] for ann in annotations['annotations'] if ann['image_id'] == image_id), None)
        
        if class_id is not None:
            class_name = class_mappings.get(class_id, 'unknown')
            print(f'Image {file_name} has class_id {class_id} mapped to class_name {class_name}')  # Debug info
        else:
            class_name = 'unknown'
            print(f'Image {file_name} has no class_id, defaulting to unknown')  # Debug info

        class_folder = os.path.join(dest_folder, class_name)
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)

        src_image_path = os.path.join(src_folder, file_name)
        dest_image_path = os.path.join(class_folder, file_name)

        print(f'Checking if image file exists at {src_image_path}')  # Debug info
        if os.path.exists(src_image_path):
            print(f'Copying {src_image_path} to {dest_image_path}')  # Debug info
            shutil.copyfile(src_image_path, dest_image_path)
        else:
            print(f'Image file {src_image_path} does not exist')  # Debug info

# Paths to the source folders and the annotations file
src_test_folder = 'datasets/test'
annotations_file_path = './datasets/test/_annotations.coco.json'

# Destination folder for organized dataset
dest_test_folder = 'organized/test'

# Load class mappings
class_mappings = load_class_mappings(annotations_file_path)
print(f'Class mappings: {class_mappings}')  # Debug info

# Load test annotations
test_annotations = load_test_annotations(annotations_file_path)

# Organize test images
print('Organizing test images...')  # Debug info
organize_test_images(test_annotations, src_test_folder, dest_test_folder, class_mappings)
