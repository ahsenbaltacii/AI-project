from PIL import Image, ImageEnhance
import os
import shutil

base_dir = r"C:\Users\AHSEN\Desktop\seg\train"
predict_path = r"C:\Users\AHSEN\Desktop\seg\train\brightness"

os.makedirs(os.path.join(predict_path, "images"), exist_ok=True)
os.makedirs(os.path.join(predict_path, "labels"), exist_ok=True)

images_path = os.path.join(base_dir, "images")
labels_path = os.path.join(base_dir, "labels")

brightness_increase = 1.15
suffix = "_+15_brightness"

for filename in os.listdir(images_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(images_path, filename)
        img = Image.open(img_path)

        enhancer = ImageEnhance.Brightness(img)
        img_bright = enhancer.enhance(brightness_increase)

        name, ext = os.path.splitext(filename)
        new_filename = name + suffix + ext

        img_bright.save(os.path.join(predict_path, "images", new_filename))

        label_name = name + ".txt"
        src_label = os.path.join(labels_path, label_name)

        if os.path.exists(src_label):
            new_label_name = name + suffix + ".txt"
            dst_label = os.path.join(predict_path, "labels", new_label_name)
            shutil.copy2(src_label, dst_label)

print("Brightness augmentation completed")