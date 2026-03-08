import os
import math
from PIL import Image

image_folder = "data/val/images"
label_folder = "data/val/labels"

save_image_folder = "data/val_rotated/images"
save_label_folder = "data/val_rotated/labels"

os.makedirs(save_image_folder,exist_ok=True)
os.makedirs(save_label_folder,exist_ok=True)

angle_deg = 15
angle = math.radians(-angle_deg)

for filename in os.listdir(label_folder):

    if not filename.endswith(".txt"):
        continue

    label_path = os.path.join(label_folder,filename)

    image_name = os.path.splitext(filename)[0] + ".jpg"
    image_path = os.path.join(image_folder,image_name)

    if not os.path.exists(image_path):

        image_name = os.path.splitext(filename)[0] + ".png"
        image_path = os.path.join(image_folder,image_name)

        if not os.path.exists(image_path):
            continue

    with Image.open(image_path) as img:

        w,h = img.size
        rotated_img = img.rotate(angle_deg,expand=False)

        new_image_name = os.path.splitext(image_name)[0] + "_rotated.png"
        rotated_img.save(os.path.join(save_image_folder,new_image_name))

    new_lines = []

    with open(label_path,"r") as f:

        for line in f.readlines():

            parts = line.strip().split()

            cls = parts[0]
            coords = list(map(float,parts[1:]))

            cx,cy = w/2,h/2
            new_coords = []

            for i in range(0,len(coords),2):

                x_norm,y_norm = coords[i],coords[i+1]

                px = x_norm * w
                py = y_norm * h

                dx = px - cx
                dy = py - cy

                new_x = dx*math.cos(angle) - dy*math.sin(angle)
                new_y = dx*math.sin(angle) + dy*math.cos(angle)

                new_px = new_x + cx
                new_py = new_y + cy

                new_coords.append(new_px/w)
                new_coords.append(new_py/h)

            new_line = cls + " " + " ".join(map(str,new_coords)) + "\n"
            new_lines.append(new_line)

    new_label_name = os.path.splitext(filename)[0] + "_rotated.txt"

    with open(os.path.join(save_label_folder,new_label_name),"w") as f:
        f.writelines(new_lines)

print("Rotation with label transform finished")