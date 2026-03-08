from ultralytics import YOLO

model = YOLO("yolo11m.pt")

results = model.train(
    data="data.yaml",
    epochs=70,
    imgsz=640,
    batch=2
)