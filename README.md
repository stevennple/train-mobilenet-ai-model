# MobileNet Training Scripts
This repository contains a collection of scripts used to train the MobileNet AI model included with the TensorFlow library. These scripts cover dataset organization, model building, training, and evaluation processes.

# Scripts Overview
## 1. organize_dataset.py <br />
This script organizes the training and validation datasets into respective class folders based on annotations.

Functions:
- load_class_mappings(meta_file_path): Loads class mappings from a meta file.
- organize_images(src_folder, dest_folder, class_mappings): Organizes images into class folders.

## 2. organize_test_dataset.py <br />
This script organizes the test dataset into respective class folders based on annotations.

Functions:
- load_class_mappings(annotations_file_path): Loads class mappings from an annotations file.
- load_test_annotations(annotations_file_path): Loads test annotations.
- organize_test_images(annotations, src_folder, dest_folder, class_mappings): Organizes test images into class folders.

## 3. build_compile_model.py <br />
This script builds and compiles the MobileNet model with additional dense layers.

Functions:
- Builds the model using MobileNet as the base and adds custom layers.
- Compiles the model with Adam optimizer and categorical cross-entropy loss.

## 4. ensure_consistency.py <br />
This script ensures that the class folders in the training, validation, and test datasets are consistent.

Functions:
- ensure_class_consistency(train_dir, val_dir, test_dir): Ensures consistency of class folders across datasets.

## 5. prep_data_generators.py <br />
This script prepares the data generators for training, validation, and testing.

Functions:
- Configures ImageDataGenerator for training, validation, and testing datasets.
- Creates data generators for each dataset.

## 6. train_model.py <br />
This script trains the MobileNet model using the prepared data generators and saves the best model.

Functions:
- Loads and compiles the model.
- Configures callbacks for checkpointing and early stopping.
- Trains the model and evaluates its performance on the test dataset.
- Saves the final trained model.

## 7. resume_training.py
This script is used to resume training from the last checkpoint in case of a crash.

Functions:
- Loads and compiles the model.
- Loads the latest checkpoint if available.
- Configures callbacks for checkpointing and early stopping.
- Resumes training from the last saved epoch.
- Evaluates the model and saves the final trained model.

# Usage
## 1. Ensure TensowFlow is installed in current Python environment:
- pip install tensorflow

## 2. Organize Datasets:
- Run organize_dataset.py to organize training and validation datasets.
- Run organize_test_dataset.py to organize the test dataset.

## 3. Build and Compile Model:
- Run build_compile_model.py to build and compile the MobileNet model.

## 4. Ensure Consistency:
- Run ensure_consistency.py to ensure class folders are consistent across datasets.

## 5. Prepare Data Generators:
- Run prep_data_generators.py to set up data generators for training, validation, and testing.

## 6. Train Model:
- Run train_model.py to train the model, evaluate its performance, and save the best version.

## 7. Resume Training:
- In case of a crash, run resume_training.py to resume training from the last checkpoint.

# Dependencies
- TensorFlow
- Keras
- JSON
- OS
- Shutil

# License
This project is licensed under the MIT License.