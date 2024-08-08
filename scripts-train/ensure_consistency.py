import os
import shutil

def ensure_class_consistency(train_dir, val_dir, test_dir):
    train_classes = set(os.listdir(train_dir))
    val_classes = set(os.listdir(val_dir))
    test_classes = set(os.listdir(test_dir))

    missing_val_classes = train_classes - val_classes
    missing_test_classes = train_classes - test_classes

    for cls in missing_val_classes:
        os.makedirs(os.path.join(val_dir, cls), exist_ok=True)
        
    for cls in missing_test_classes:
        os.makedirs(os.path.join(test_dir, cls), exist_ok=True)

# Assuming the directories
train_dir = '/content/organized/train'
val_dir = '/content/organized/validation'
test_dir = '/content/organized/test'

# Ensure consistency
ensure_class_consistency(train_dir, val_dir, test_dir)