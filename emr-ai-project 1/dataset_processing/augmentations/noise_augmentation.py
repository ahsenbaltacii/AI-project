from PIL import Image
import numpy as np
import os
import shutil

base_dir = "data/train"
output_dir = "data/train_noise"

os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels"), exist_ok=True)

images_path = os.path.join(base_dir, "images")
labels_path = os.path.join(base_dir, "labels")

noise_level = 0.001
suffix = "_noise"

def salt_and_pepper_noise(image, amount):
    img_array = np.array(image)
    row, col, ch = img_array.shape

    num_salt = int(amount * img_array.size * 0.5)
    num_pepper = int(amount * img_array.size * 0.5)

    coords = [np.random.randint(0, i - 1, num_salt) for i in img_array.shape[:2]]
    img_array[coords[0], coords[1], :] = 255

    coords = [np.random.randint(0, i - 1, num_pepper) for i in img_array.shape[:2]]
    img_array[coords[0], coords[1], :] = 0

    return Image.fromarray(img_array)

for filename in os.listdir(images_path):

    if filename.lower().endswith((".jpg",".jpeg",".png")):

        img_path = os.path.join(images_path,filename)
        img = Image.open(img_path).convert("RGB")

        noisy_img = salt_and_pepper_noise(img,noise_level)

        name,ext = os.path.splitext(filename)
        new_filename = name + suffix + ext

        noisy_img.save(os.path.join(output_dir,"images",new_filename))

        label_name = name + ".txt"
        src_label = os.path.join(labels_path,label_name)

        if os.path.exists(src_label):

            new_label = name + suffix + ".txt"
            shutil.copy2(src_label, os.path.join(output_dir,"labels",new_label))

print("Noise augmentation finished")