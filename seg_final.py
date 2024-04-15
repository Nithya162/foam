import os
import random
import shutil

# Set the paths
source_folder = r"C:\yolov8\DATA\IMAGES"
train_folder = r"C:\yolov8\DATA\TRAIN"
val_folder = r"C:\yolov8\DATA\VAL"
test_folder = r"C:\yolov8\DATA\TEST"


# List all images
all_images = os.listdir(source_folder)
random.shuffle(all_images)

# Define proportions for train, validation, and test sets
train_split = 0.7
val_split = 0.2
test_split = 0.1

# Calculate the number of images for each set
num_images = len(all_images)
num_train = int(num_images * train_split)
num_val = int(num_images * val_split)
num_test = num_images - num_train - num_val

# Create folders if they don't exist
for folder in [train_folder, val_folder, test_folder]:
    os.makedirs(folder, exist_ok=True)

# Move images to train folder
for img in all_images[:num_train]:
    src = os.path.join(source_folder, img)
    dst = os.path.join(train_folder, img)
    shutil.copy(src, dst)

# Move images to validation folder
for img in all_images[num_train:num_train + num_val]:
    src = os.path.join(source_folder, img)
    dst = os.path.join(val_folder, img)
    shutil.copy(src, dst)

# Move images to test folder
for img in all_images[num_train + num_val:]:
    src = os.path.join(source_folder, img)
    dst = os.path.join(test_folder, img)
    shutil.copy(src, dst)

print("Data split and randomized successfully!")