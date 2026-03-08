from PIL import Image
import os
import shutil

base_dir = r"C:\Users\AHSEN\Desktop\seg\train"
target_size = (640, 640)

save_path = base_dir + "_resized"

os.makedirs(os.path.join(save_path, "images"), exist_ok=True)
os.makedirs(os.path.join(save_path, "labels"), exist_ok=True)

images_path = os.path.join(base_dir, "images")
labels_path = os.path.join(base_dir, "labels")

for filename in os.listdir(images_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(images_path, filename)
        img = Image.open(img_path)
        img_resized = img.resize(target_size)

        img_resized.save(os.path.join(save_path, "images", filename))

        label_name = os.path.splitext(filename)[0] + ".txt"
        src_label = os.path.join(labels_path, label_name)
        dst_label = os.path.join(save_path, "labels", label_name)

        if os.path.exists(src_label):
            shutil.copy2(src_label, dst_label)

print("Resize completed")