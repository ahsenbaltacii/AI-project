from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(
    "test/images",
    save=True,
    conf=0.1,
    line_width=1,
    batch=2,
    show_conf=True,
    show_boxes=True
)