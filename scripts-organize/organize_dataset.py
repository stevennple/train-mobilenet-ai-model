import os
import json
import shutil

def load_class_mappings(meta_file_path):
    with open(meta_file_path, 'r') as f:
        meta = json.load(f)
    class_mappings = {item['id']: item['title'] for item in meta['classes']}
    return class_mappings

def organize_images(src_folder, dest_folder, class_mappings):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    ann_folder = os.path.join(src_folder, 'ann')
    img_folder = os.path.join(src_folder, 'img')

    for ann_file in os.listdir(ann_folder):
        ann_path = os.path.join(ann_folder, ann_file)
        with open(ann_path) as f:
            annotation = json.load(f)
            if annotation['objects']:
                class_id = annotation['objects'][0]['classId']
                class_name = class_mappings.get(class_id, 'unknown')
                print(f'Annotation {ann_file} has class_id {class_id} mapped to class_name {class_name}')  # Debug info
            else:
                class_name = 'unknown'
                print(f'Annotation {ann_file} has no objects, defaulting to unknown')  # Debug info

            class_folder = os.path.join(dest_folder, class_name)
            if not os.path.exists(class_folder):
                os.makedirs(class_folder)

            image_file = ann_file.replace('.jpg.json', '.jpg')
            src_image_path = os.path.join(img_folder, image_file)
            dest_image_path = os.path.join(class_folder, image_file)

            if os.path.exists(src_image_path):
                print(f'Copying {src_image_path} to {dest_image_path}')  # Debug info
                shutil.copyfile(src_image_path, dest_image_path)
            else:
                print(f'Image file {src_image_path} does not exist')  # Debug info

# Paths to the source folders and the meta.json file
src_train_folder = 'datasets/train'
src_val_folder = 'datasets/validation'
meta_file_path = 'datasets/meta.json'

# Destination folders for organized dataset
dest_train_folder = 'organized/train'
dest_val_folder = 'organized/validation'

# Load class mappings
class_mappings = load_class_mappings(meta_file_path)

# Organize images
organize_images(src_train_folder, dest_train_folder, class_mappings)
organize_images(src_val_folder, dest_val_folder, class_mappings)
