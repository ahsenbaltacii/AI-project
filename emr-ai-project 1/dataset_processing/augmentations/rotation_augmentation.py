from PIL import Image
import os

image_folder = "data/train/images"
save_folder = "data/train_rotated"

os.makedirs(save_folder,exist_ok=True)

for filename in os.listdir(image_folder):

    if filename.lower().endswith((".jpg",".jpeg",".png")):

        img_path = os.path.join(image_folder,filename)
        img = Image.open(img_path)

        rotated = img.rotate(15,expand=True)

        name,ext = os.path.splitext(filename)
        new_filename = name + "_rotation" + ext

        rotated.save(os.path.join(save_folder,new_filename))

print("Image rotation finished")