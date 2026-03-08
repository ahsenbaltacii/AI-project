from PIL import Image, ImageFilter
import os
import shutil

base_dir = "data/val"
output_dir = "data/val_blur"

os.makedirs(os.path.join(output_dir,"images"),exist_ok=True)
os.makedirs(os.path.join(output_dir,"labels"),exist_ok=True)

images_path = os.path.join(base_dir,"images")
labels_path = os.path.join(base_dir,"labels")

blur_radius = 1.5
suffix = "_blur"

for filename in os.listdir(images_path):

    if filename.lower().endswith((".jpg",".jpeg",".png")):

        img_path = os.path.join(images_path,filename)
        img = Image.open(img_path)

        blurred = img.filter(ImageFilter.GaussianBlur(blur_radius))

        name,ext = os.path.splitext(filename)
        new_filename = name + suffix + ext

        blurred.save(os.path.join(output_dir,"images",new_filename))

        label_name = name + ".txt"
        src_label = os.path.join(labels_path,label_name)

        if os.path.exists(src_label):

            new_label = name + suffix + ".txt"
            shutil.copy2(src_label, os.path.join(output_dir,"labels",new_label))

print("Blur augmentation finished")